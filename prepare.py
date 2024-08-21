import cv2
import numpy as np

root = "./images"

def crop(image):
    # 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 흰색 배경을 검정색 글자와 분리 (임계처리)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # 가장 큰 윤곽선 찾기
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # 윤곽선의 경계 상자 찾기
        x, y, w, h = cv2.boundingRect(contours[0])
        for cnt in contours[1:]:
            x1, y1, w1, h1 = cv2.boundingRect(cnt)
            x = min(x, x1)
            y = min(y, y1)
            w = max(w, x1 + w1 - x)
            h = max(h, y1 + h1 - y)

        # 경계 상자를 이용해 이미지 자르기
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    else:
        print("crop fail")
        return image


def transparent(image_path, output_path, cutoff=150):
    # 이미지 읽기 (알파 채널 포함)
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # 이미지가 RGBA 형식이 아닌 경우, 알파 채널 추가
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # 흰색 배경을 투명하게 만들기 위한 마스크 생성
    lower_white = np.array([cutoff, cutoff, cutoff, 255], dtype=np.uint8)
    upper_white = np.array([255, 255, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(image, lower_white, upper_white)

    # 마스크의 흰색 부분을 투명하게 설정
    image[mask == 255] = [255, 255, 255, 0]

    # 투명 배경으로 변환된 이미지 저장
    cv2.imwrite(output_path, image)


def run():
    for i in range(1, 41):
        # 이미지 파일 읽기
        image = cv2.imread(root + "/input/" + str(i) + ".PNG")

        # 가장자리 여백 자르기
        image = crop(image)
        cv2.imwrite(root + "/crop/" + str(i) + ".PNG", image)

        # 흰 배경 투명화
        transparent(root + "/crop/" + str(i) + ".PNG", root + "/transparent/" + str(i) + ".PNG")
        # rescale_image_width(image, 20, 20)
        # image.save("./crops/" + str(i) + ".PNG")
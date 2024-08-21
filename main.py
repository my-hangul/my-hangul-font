import prepare

image_size = 30

def run():
    try:
        # 1. 이미지 전처리 (크롭 & 배경 없애기)
        prepare.run()
        #
        # # 2. 조합
        # jamo1.run()
        # jamo2.run()
        # jamo3.run()
        #
        # # 3. 이미지 크기 조정
        # images.transletters()
        #
        # # 4. 이미지 병합
        # images.concat()
        #
        # # 5. TTF 폰트 생성
        # images.png_to_ttf(image_size, image_size)

        # 6. TTF 파일 저장

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    run()
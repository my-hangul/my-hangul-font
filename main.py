import prepare
import jamo1
import jamo2
import jamo3
import images
import os

image_size = 30

def run():
    try:
        # 1. 이미지 전처리 (크롭 & 배경 없애기)
        prepare.run()

        # 2. 조합
        jamo1.run()
        jamo2.run()
        jamo3.run()

        # 3. 이미지 크기 조정
        prepare.transletters()

        # 4. 이미지 병합
        folder = './images/letters2'
        image_paths = [os.path.join(folder, f)
                       for f in os.listdir(folder) if f.endswith('.PNG')]
        image_paths = sorted(image_paths)
        images.concat_images(image_paths, (image_size, image_size), (84, 133))

        # 5. TTF 폰트 생성
        images.png_to_ttf(image_size, image_size)

        # 6. TTF 파일 저장

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    run()
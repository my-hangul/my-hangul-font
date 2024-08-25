# 1 자음 + 모음
from PIL import Image

path = './images/combinations'


def rescale_image_ratio(image, rescale_width=None, rescale_height=None):
    width, height = image.size

    if rescale_width is not None:
        # Calculate new height preserving aspect ratio
        aspect_ratio = width / height
        new_width = int(rescale_width)
        new_height = int(new_width / aspect_ratio)
    elif rescale_height is not None:
        # Calculate new width preserving aspect ratio
        aspect_ratio = height / width
        new_height = int(rescale_height)
        new_width = int(new_height / aspect_ratio)
    else:
        raise ValueError("Either 'rescale_width' or 'rescale_height' must be provided.")

    return image.resize((new_width, new_height), Image.LANCZOS)


# ㅏ ㅐ ㅑ ㅒ ㅣ
def combine_letters_1():
    for j in [20, 21, 22, 23, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_height=90)

            background.paste(consonant, (30, 30))
            background.paste(vowel, (int(30 + consonant.width * 1.1), int(30 + consonant.height * 0.5 - 45)))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅓ ㅔ ㅕ ㅖ
def combine_letters_2():
    for j in [24, 25, 26, 27]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_height=90)

            background.paste(vowel, (int(30 + consonant.width), int(30 + consonant.height * 0.5 - 45)))
            background.paste(consonant, (30, 30))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅗ ㅛ
def combine_letters_3():
    for j in [28, 32]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_width=90)

            background.paste(consonant, (30, 30))
            background.paste(vowel, (20, 30 + consonant.height))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅜ ㅠ ㅡ
def combine_letters_4():
    for j in [33, 37, 38]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_width=90)

            background.paste(consonant, (30, 30))
            background.paste(vowel, (20, int(30 + consonant.height * 1.1)))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅘ ㅙ ㅚ ㅞ ㅝ ㅟ ㅢ
def combine_letters_5():
    # ㅗ + ㅏ ㅐ ㅣ
    index = 29
    for j in [20, 21, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/28.PNG')
            vowel2 = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_width=80)
            vowel2 = rescale_image_ratio(vowel2, rescale_height=consonant.height + vowel.height)

            background.paste(consonant, (20, 30))
            background.paste(vowel, (15, 30 + consonant.height))
            background.paste(vowel2, (int(15 + vowel.width * 1.1), 30))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(index).zfill(2) + ".PNG")
        index += 1

    # ㅜ + ㅓ ㅔ ㅣ
    index = 34
    for j in [24, 25, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
            vowel = Image.open('./images/transparent/33.PNG')
            vowel2 = Image.open('./images/transparent/' + str(j) + '.PNG')

            consonant = rescale_image_ratio(consonant, rescale_width=70)
            vowel = rescale_image_ratio(vowel, rescale_width=80)
            vowel2 = rescale_image_ratio(vowel2, rescale_height=consonant.height + vowel.height)

            background.paste(consonant, (20, 30))
            background.paste(vowel, (15, 30 + consonant.height))
            background.paste(vowel2, (15 + vowel.width, 30))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(index).zfill(2) + ".PNG")
        index += 1

    # ㅡ + ㅣ
    for i in range(1, 20):
        background = Image.open('./images/background.png')
        consonant = Image.open('./images/transparent/' + str(i) + '.PNG')
        vowel = Image.open('./images/transparent/38.PNG')
        vowel2 = Image.open('./images/transparent/40.PNG')

        consonant = rescale_image_ratio(consonant, rescale_width=70)
        vowel = rescale_image_ratio(vowel, rescale_width=80)
        vowel2 = rescale_image_ratio(vowel2, rescale_height=int(consonant.height * 1.1 + vowel.height))

        background.paste(consonant, (20, 30))
        background.paste(vowel, (15, int(30 + consonant.height * 1.1)))
        background.paste(vowel2, (15 + vowel.width, 30))
        background.save(path + '/letter_' + str(i).zfill(2) + "_39.PNG")


def run():
    print('jamo1 시작')
    combine_letters_1()
    combine_letters_2()
    combine_letters_3()
    combine_letters_4()
    combine_letters_5()
    print('jamo1 끝')
import os
from PIL import Image


input_folder = './images/transparent'
output_folder = './images/combinations'

def load_image(file_path):
    try:
        img = Image.open(file_path)
    except FileNotFoundError:
        print(f"Failed to load image: {file_path}\nPlease check the file path and try again.")
        exit(1)
    return img.convert('RGBA')


def rescale_image_width(image, rescale_width, rescale_height):
    width, height = image.size
    new_width = int(rescale_width)
    new_height = int(rescale_height)
    return image.resize((new_width, new_height), Image.LANCZOS)

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


def combine_letters3(input_folder, output_folder):
    print("Loading images..")

    rescale_width = 20

    consonants_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    consonants_1 = [(i, load_image(os.path.join(input_folder, f'{i}.PNG'))) for i in consonants_index]
    consonants = [(c_value, rescale_image_ratio(img, rescale_width=47)) for
                                        c_value, img in consonants_1]
    consonants_2 = [(c2_value, rescale_image_ratio(img, rescale_width=55)) for
                                        c2_value, img in consonants_1]
    #ㅏ, ㅐ, ㅑ, ㅒ, ㅣ
    vowels_1_index = [20, 21, 22, 23, 40]
    vowels_1_1 = [(j, load_image(os.path.join(input_folder, f'{j}.PNG'))) for j in vowels_1_index]
    vowels_1 = [(v1_value, rescale_image_ratio(img, rescale_height=55)) for
                                        v1_value, img in vowels_1_1]
    #ㅓ, ㅔ, ㅕ, ㅖ
    vowels_2_index = [24, 25, 26, 27]
    vowels_2_1 = [(k, load_image(os.path.join(input_folder, f'{k}.PNG'))) for k in vowels_2_index]
    vowels_2 = [(v1_value, rescale_image_ratio(img, rescale_height=55)) for
                                        v1_value, img in vowels_2_1]
    #ㅗ, ㅛ
    vowels_3_index =[28, 32]
    vowels_3_1 = [(m, load_image(os.path.join(input_folder, f'{m}.PNG'))) for m in vowels_3_index]
    vowels_3 = [(v1_value, rescale_image_width(img, 80, 32)) for
                                        v1_value, img in vowels_3_1]
    #ㅜ, ㅠ
    vowels_4_index = [33, 37]
    vowels_4_1 = [(n, load_image(os.path.join(input_folder, f'{n}.PNG'))) for n in vowels_4_index]
    vowels_4 = [(v1_value, rescale_image_width(img, 80, 32)) for
                                        v1_value, img in vowels_4_1]
    #ㅘ, ㅙ, ㅚ
    vowels_5_index = [29, 30, 31]
    vowels_5 = [(o, load_image(os.path.join(input_folder, f'{o}.PNG'))) for o in vowels_5_index]
    rescaled_vowels_5 = [(m, rescale_image_width(img, 80, 65)) for m, img in vowels_5]

    #ㅝ, ㅞ, ㅟ, ㅢ
    vowels_6_index = [34, 35, 36, 39]
    vowels_6 = [(o, load_image(os.path.join(input_folder, f'{o}.PNG'))) for o in vowels_6_index]
    rescaled_vowels_6 = [(m, rescale_image_width(img, 80, 65)) for m, img in vowels_6]

    #ㅡ
    vowels_7_index = [38]
    vowels_7_1 = [(o, load_image(os.path.join(input_folder, f'{o}.PNG'))) for o in vowels_7_index]
    vowels_7 = [(m, rescale_image_ratio(img, rescale_width=80)) for m, img in vowels_7_1]

    final_consonants_index = [1, 3, 6, 8, 10]
    final_consonants = [(l,load_image(os.path.join(input_folder, f'{l}.PNG'))) for l in final_consonants_index]
    rescaled_final_consonants = [(m, rescale_image_width(img, 40, 35)) for m, img in final_consonants]
    second_final_consonants_index = [1, 7, 8, 10, 13, 17, 18, 19]
    second_final_consonants = [(sfc, load_image(os.path.join(input_folder, f'{sfc}.PNG'))) for
                               sfc in second_final_consonants_index]
    rescaled_second_final_consonants = [(sfc_value, rescale_image_width(img, 40, 35)) for
                                        sfc_value, img in second_final_consonants]
    print("All images loaded successfully.")
    second_final_consonant_gap = 5

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    background_file = './images/background.png'

    for sfc, (sfc_value, second_final_consonant) in enumerate(rescaled_second_final_consonants):
        for c, (c_value, consonant) in enumerate(consonants):
            for v, (v_value, vowel) in enumerate(vowels_1):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue
                    background = Image.open(background_file)

                    consonant_pos = (23, 25)
                    vowel_pos = (85, 20)
                    final_consonant_pos = (37, 83)
                    second_final_consonant_pos = (70 + second_final_consonant_gap, 85)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"

                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_2):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue
                    background = Image.open(background_file)

                    consonant_pos = (33, 25)
                    vowel_pos = (82, 20)
                    final_consonant_pos = (43, 83)
                    second_final_consonant_pos = (75 + second_final_consonant_gap, 85)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)


                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(rescaled_vowels_5):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (43, 10)
                    vowel_pos = (45, 30)
                    final_consonant_pos = (45, 85)
                    second_final_consonant_pos = (75 + second_final_consonant_gap, 85)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)

                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(rescaled_vowels_6):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (45, 10)
                    vowel_pos = (45, 38)
                    final_consonant_pos = (53, 95)
                    second_final_consonant_pos = (83 + second_final_consonant_gap, 95)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

        for c, (c_value, consonant) in enumerate(consonants_2):
            for v, (v_value, vowel) in enumerate(vowels_3):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (53, 8)
                    vowel_pos = (40, 60)
                    final_consonant_pos = (43, 95)
                    second_final_consonant_pos = (77 + second_final_consonant_gap, 98)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)

                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_4):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (50, 8)
                    vowel_pos = (40, 67)
                    final_consonant_pos = (43, 95)
                    second_final_consonant_pos = (75 + second_final_consonant_gap, 98)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_7):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (50, 8)
                    vowel_pos = (40, 75)
                    final_consonant_pos = (43, 95)
                    second_final_consonant_pos = (75 + second_final_consonant_gap, 98)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)
    print("Images combined successfully.")

def run():
    combine_letters3(input_folder, output_folder)
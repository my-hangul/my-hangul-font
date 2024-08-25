from PIL import Image, ImageOps, ImageFilter
import fontforge


Image.MAX_IMAGE_PIXELS=1000000000


def concat_images(image_paths, size, shape=None):
    print("concat 시작")
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)

    images = [ImageOps.fit(i, size, Image.LANCZOS)
              for i in images]

    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    result = Image.new('RGB', image_size)

    idx = 0
    # Paste images into final image
    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            result.paste(images[idx], offset)
            idx = idx + 1

    result.save("./concat.PNG")
    print("concat 끝")
    return result


def png_to_ttf(width, height):
    print("font 생성 시작")
    output = "font.ttf"
    image = Image.open('./concat.PNG')
    image = image.filter(ImageFilter.SHARPEN)

    factor = 10
    private_range = 0xAC00
    background = (50, 50, 50)

    font = fontforge.font()
    font.ascent = height * factor
    font.descent = 0 * factor
    font.encoding = 'KSC5601'

    font.familyname = "your-writing"
    font.fullname = "your-writing"
    font.weight = "Book"

    pixels = image.load()

    for j in range(image.height // height):
        print(j)
        for i in range(image.width // width):
            offset = i + j * (image.width // width)
            unicode = private_range + offset
            char = font.createChar(unicode)
            char.width = width * factor
            pen = char.glyphPen()

            for y in range(height):
                for x in range(width):
                    pixel = pixels[i * width + x, j * height + y]
                    if pixel <= background: # pixel이 충분히 어두울 때만 draw
                        pen.moveTo((x * factor, (height - y) * factor))
                        pen.lineTo(((x + 1) * factor, (height - y) * factor))
                        pen.lineTo(((x + 1) * factor, (height - y - 1) * factor))
                        pen.lineTo((x * factor, (height - y - 1) * factor))
                        pen.closePath()

            # Remove overlap and hinting information
            char.removeOverlap()

    font.generate(output, flags=('opentype'))
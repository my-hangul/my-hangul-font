# your-writing (my-hangul-font)

## Overview

**your-writing** is a Python-based tool designed for generating user-customized Korean fonts. This project allows users to create personalized Hangul fonts using their own handwriting, addressing the limitations of existing digital handwriting apps which struggle to reflect individual styles.

## Features

- **Image Collection**: Extracts Hangul syllables from user-provided images.
- **Image Composition**: Combines syllable images to create complete Hangul characters.
- **Font Generation**: Converts the composed characters into a font file using FontForge.

## Requirements

- Python
- Linux
- FontForge
- OpenCV
- Pillow

## Setup and Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/my-hangul/my-hangul-font.git
   cd my-hangul-font
   ```

2. **Place images of Hangul characters** (ㄱ ~ ㅎ, ㅏ ~ ㅢ) in the `images/input` folder. (total 40)

3. **Run the following command to generate the font file `font.ttf`**:
   ```bash
   python3 main.py
   ```

4. **Use the generated `font.ttf`** for web or app development, or in any digital environment to apply your customized **KOREAN handwriting style**.

## Demo Video

Watch the demo video [here](https://youtu.be/QwPoRHF2v-g) to see how the code can be utilized in **different web and app services**.

## Repository

Find the project on GitHub: [my-hangul-font](https://github.com/my-hangul/my-hangul-font.git)

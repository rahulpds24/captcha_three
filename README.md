# Captcha Solver

## Overview
This project provides a simple captcha solver that can handle both PNG and SVG captcha images. The solver fetches the captcha image from a given URL and uses OCR to extract the text.

## Features
- Supports both PNG and SVG captcha images.
- Solves captcha within 15 seconds.

## Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install requests Pillow pytesseract
   ```

## Usage
1. Create an instance of `CaptchaSolver` with the captcha image URL.
2. Call the `solve_captcha()` method to get the solved text.

## License
This project is licensed under the MIT License.
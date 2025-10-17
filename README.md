# Captcha Solver

This project is a simple captcha solver that supports both PNG and SVG captcha images. It uses Tesseract OCR to extract text from images and can solve captchas within 15 seconds.

## Features
- Supports both PNG and SVG captcha images.
- Solves captcha text within 15 seconds.
- Easy to use with a simple web interface.

## Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install requests Pillow pytesseract
   ```
3. Ensure Tesseract OCR is installed on your system.

## Usage
1. Run the application.
2. Enter the URL of the captcha image.
3. Click 'Solve Captcha' to get the solved text.

## License
This project is licensed under the MIT License.
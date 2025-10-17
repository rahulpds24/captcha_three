# Captcha Solver

## Overview
This project provides a simple captcha solver that can handle both PNG and SVG captcha images. The solver fetches the captcha from a given URL and attempts to solve it within 15 seconds.

## Features
- Supports both PNG and SVG captcha images.
- Solves captcha text using OCR (Optical Character Recognition).
- Displays the solved captcha text within 15 seconds.

## Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install requests Pillow pytesseract
   ```

## Usage
1. Create an instance of `CaptchaSolver` with the captcha URL.
2. Call the `solve_captcha` method to get the solved text.

```python
solver = CaptchaSolver('https://example.com/captcha.svg')
print(solver.solve_captcha())
```

## License
This project is licensed under the MIT License.
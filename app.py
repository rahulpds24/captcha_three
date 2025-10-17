import requests
import time
from PIL import Image
import pytesseract
import io

class CaptchaSolver:
    def __init__(self, url):
        self.url = url

    def fetch_captcha(self):
        response = requests.get(self.url)
        return Image.open(io.BytesIO(response.content))

    def solve_captcha(self):
        start_time = time.time()
        captcha_image = self.fetch_captcha()
        solved_text = pytesseract.image_to_string(captcha_image)
        elapsed_time = time.time() - start_time

        if elapsed_time > 15:
            raise Exception('Captcha solving took too long.')

        return solved_text.strip()

# Example usage:
# solver = CaptchaSolver('CAPTCHA_IMAGE_URL')
# print(solver.solve_captcha())
import requests
import time
from PIL import Image
import pytesseract
from io import BytesIO

class CaptchaSolver:
    def __init__(self, url):
        self.url = url

    def fetch_captcha(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            raise Exception('Failed to fetch captcha')

    def solve_captcha(self):
        start_time = time.time()
        captcha_image = self.fetch_captcha()
        captcha_text = pytesseract.image_to_string(captcha_image)
        elapsed_time = time.time() - start_time
        if elapsed_time > 15:
            raise Exception('Solving captcha took too long')
        return captcha_text.strip()

# Example usage:
# solver = CaptchaSolver('captcha_image_url')
# print(solver.solve_captcha())

import requests
from PIL import Image
import pytesseract
import time
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
        captcha_text = pytesseract.image_to_string(captcha_image)
        elapsed_time = time.time() - start_time
        if elapsed_time > 15:
            raise Exception('Solving time exceeded 15 seconds')
        return captcha_text.strip()

if __name__ == '__main__':
    url = 'CAPTCHA_IMAGE_URL'
    solver = CaptchaSolver(url)
    print(solver.solve_captcha())
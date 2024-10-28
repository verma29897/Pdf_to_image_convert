
from PIL import Image
import pytesseract
def extract_text_from_image(image):
    im = Image.open(image)

    text = pytesseract.image_to_string(im)
    return text







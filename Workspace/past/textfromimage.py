

import pytesseract
import sys
from PIL import Image

print(pytesseract.image_to_string(Image.open(sys.argv[1])))
print(sys.argv[1])



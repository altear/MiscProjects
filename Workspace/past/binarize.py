from PIL import ImageColor, ImageDraw, Image
import sys

thingy = Image.open(sys.argv[1])
gray = thingy.convert('L')
thingy = gray.point(lambda x: 0 if x<110 else 255, '1')
thingy.save(sys.argv[2])




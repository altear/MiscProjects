from PIL import ImageColor, ImageDraw, Image
import sys

thingy2 = Image.open(sys.argv[1])
draw = ImageDraw.Draw(thingy2)
floodedimage = ImageDraw.floodfill(thingy2, (1, 1), 1)
del draw

# write to stdout
thingy2.save(sys.argv[2])


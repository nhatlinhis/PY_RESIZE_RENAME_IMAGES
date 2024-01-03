from PIL import Image
import os
import pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
inputPath = str(dirPath) + '\input\\'
outputPath = str(dirPath) + '\output\\'

dirs = os.listdir(inputPath)

def resize():
  for item in dirs:
    img = Image.open(inputPath+item)
    width, height = img.size

    f, e = os.path.splitext(outputPath + item)
    print(f)

    # imgResize = img.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
    imgResize = img
    if imgResize.mode in ("RGBA", "P"):
      imgResize = imgResize.convert("RGB")
    imgResize.save(f + '.jpg', quality = 50)

resize()
from PIL import Image
import os
import pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
inputPath = str(dirPath) + '\input\\'

# Lấy danh sách các tệp trong thư mục input
files = os.listdir(inputPath)

def resize_and_save():
    for filename in files:
        # Đường dẫn đầy đủ của tệp
        file_path = os.path.join(inputPath, filename)

        # Mở hình ảnh
        img = Image.open(file_path)

        # Resize hình ảnh và lưu lại trên chính tệp input
        imgResize = img
    if imgResize.mode in ("RGBA", "P"):
      imgResize = imgResize.convert("RGB")
    imgResize.save(f + '.jpg', quality = 50)

resize_and_save()

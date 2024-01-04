from PIL import Image
import os
import pathlib

def resize_images_for_id_product(id_product):
    dirPath = pathlib.Path(__file__).parent.absolute()

    inputPath = f'E:\\DATASETS\\validation\\{id_product}'
    outputPath = f'F:\\DATASETS\\validation\\{id_product}'

    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    dirs = os.listdir(inputPath)

    for item in dirs:
        img = Image.open(os.path.join(inputPath, item))
        width, height = img.size

        f, e = os.path.splitext(item)
        print(f)

        imgResize = img
        if imgResize.mode in ("RGBA", "P"):
            imgResize = imgResize.convert("RGB")

        output_file_path = os.path.join(outputPath, f + '.jpg')
        counter = 1
        while os.path.exists(output_file_path):
            output_file_path = os.path.join(outputPath, f + '_' + str(counter) + '.jpg')
            counter += 1

        imgResize.save(output_file_path, quality=50)

# List of id_product values
id_products  = [
    '1012835000020', '1012835000021', '1012835000044', '1013039000213',
    '1053047000001', '1053047000016', '1053047000021', '1053047000068',
    '1053047000138', '1053047000140', '1053047000147', '1053047000162',
    '1053047000194', '1053047000196', '1053047000197', '1053047000285',
    '1053047000336', '1053047000339', '1053047000342', '1053047000424',
    '1053047000435', '1053047000589', '1053047000769', '1053047000811',
    '1053047000837', '1053047000856', '1053047000874', '1063021000015',
    '1063021000031', '1063021000035', '1063021000040', '1253021000019',
    '1253021000032', '1253021000079', '1253021000142', '1253021000144',
    '1253021000151', '1253021000157', '1253021000185', '1253021000191',
    '1253021000236', '8936094292200', '9892849000692', '9892849000923',
    '9892850000281', '1053047000734'
]

# Loop through each id_product
for id_product in id_products:
    resize_images_for_id_product(id_product)

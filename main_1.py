from PIL import Image
import os
import datetime
import pathlib

# THAY ĐỔI KÍCH THƯỚC
def resize_images(input_folder, output_folder, new_width, new_height):
    # Tạo thư mục đầu ra nếu nó chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua tất cả các tệp trong thư mục đầu vào
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Kiểm tra xem tệp có phải là ảnh không
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            try:
                # Mở ảnh và thực hiện resize
                img = Image.open(input_path)
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Tạo đường dẫn cho ảnh đã resize trong thư mục đầu ra
                output_path = os.path.join(output_folder, filename)

                # Lưu ảnh đã resize
                resized_img.save(output_path)

                print(f"Đã thay đổi kích thước: {filename}")
            except Exception as e:
                print(f"Lỗi xử lý {filename}: {str(e)}")

# Đường dẫn đầu vào và đầu ra
input_folder_path = "./input"
output_folder_path = "./output"

# Kích thước mới cho ảnh (đơn vị: pixel)
new_width = 640
new_height = 640

# Thực hiện thay đổi kích thước
resize_images(input_folder_path, output_folder_path, new_width, new_height)

# ĐỔI TÊN
def rename_images_in_folders(root_directory):
    for folder_name, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Tạo đường dẫn đầy đủ tới tệp và thư mục
                file_path = os.path.join(folder_name, filename)

                # Tạo tên mới cho tệp
                now = datetime.datetime.now()
                timestamp = now.strftime('%Y-%m-%d-%H-%M-%S')
                new_filename = f"{timestamp}_{os.path.basename(folder_name)}_ver1.jpg"

                # Kiểm tra xem tên tệp đích đã tồn tại chưa, nếu có, tạo tên mới duy nhất
                count = 1
                while os.path.exists(os.path.join(folder_name, new_filename)):
                    new_filename = f"{timestamp}_{os.path.basename(folder_name)}_ver1_{count}.jpg"
                    count += 1

                # Đổi tên tệp
                new_file_path = os.path.join(folder_name, new_filename)
                os.rename(file_path, new_file_path)

# Sử dụng ví dụ:
rename_images_in_folders(output_folder_path)

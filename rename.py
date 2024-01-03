import os
import datetime

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
root_directory = "./output"
rename_images_in_folders(root_directory)
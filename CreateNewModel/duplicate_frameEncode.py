import os
import shutil

def duplicate_frameEncode(source_folder):
        # Lặp qua các thư mục trong thư mục gốc
    for root, dirs, files in os.walk(source_folder):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            file_count = len(os.listdir(folder_path))
            remaining_files = 30 - file_count

            if remaining_files > 0:
                last_file = sorted(os.listdir(folder_path))[-1]

                # Tạo các bản sao tệp tin cuối cùng để đủ 30 tệp tin
                for i in range(1, remaining_files + 1):
                    new_filename = str(file_count+i-1) + os.path.splitext(last_file)[1]
                    new_filepath = os.path.join(folder_path, new_filename)
                    shutil.copy2(os.path.join(folder_path, last_file), new_filepath)


a = ['hello', 'no', 'langnghe']

source_folder = "C:/Users/ADMIN/Downloads/NCKH/CreateNewModel/MP_Data_reduce/"  
for x in a:
    duplicate_frameEncode(source_folder+x)

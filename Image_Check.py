from PIL import Image
import os

folder_path = 'C:/Users/grant/Desktop/Project/Project_SLS/Sign_Detection/data/train/Z'

def are_jpeg_images_in_folder_corrupted(folder_path):
    corrupted_images = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    img.verify()
            except (IOError, SyntaxError):
                corrupted_images.append(file_name)
    if not corrupted_images:
        print(None)
    else:
        print(corrupted_images)
    return corrupted_images

are_jpeg_images_in_folder_corrupted(folder_path)
import os
import random
import shutil

def move_images(source_dir, dest_dir, num_images):
    image_names = os.listdir(source_dir)
    selected_images = random.sample(image_names, num_images)
    for image_name in selected_images:
        shutil.move(os.path.join(source_dir, image_name), dest_dir)

#Change the directory for each folder which has to be moved
source_dir = 'C:/Users/grant/Desktop/Project/Project_SLS/Sign_Detection/data1/train/Z'
dest_dir = 'C:/Users/grant/Desktop/Project/Project_SLS/Sign_Detection/data1/test/Z'
num_images = 150
move_images(source_dir, dest_dir, num_images)
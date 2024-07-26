import os
import shutil

# Define paths to the input files and the images directory
train_file = '/Users/shahriyar/Desktop/programming/Python/Optriment/lists/train.txt'
test_file = '/Users/shahriyar/Desktop/programming/Python/Optriment/lists/test.txt'
classes_file = '/Users/shahriyar/Desktop/programming/Python/Optriment/lists/classes.txt'
files_file = '/Users/shahriyar/Desktop/programming/Python/Optriment/lists/files.txt'
images_dir = '/Users/shahriyar/Desktop/programming/Python/Optriment/lists/images'

# Define output directories for training and testing datasets
output_train_dir = 'data/train'
output_test_dir = 'data/test'

# Create the output directories if they do not exist
os.makedirs(output_train_dir, exist_ok=True)
os.makedirs(output_test_dir, exist_ok=True)

# Function to read file and return list of lines
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

# Read the content of the input files
train_lines = read_file(train_file)
test_lines = read_file(test_file)
classes_lines = read_file(classes_file)

# Create a dictionary for class names
class_dict = {}
for line in classes_lines:
    class_id, class_name = line.split('.')
    class_dict[class_id] = class_name

# Function to copy images to the target directory
def copy_images(file_lines, target_dir):
    for line in file_lines:
        if line:
            class_name_with_id = line.split('/')[0]
            if class_name_with_id in class_dict.values():
                class_name = class_name_with_id
            else:
                # Extract class ID to get the class name
                class_id = class_name_with_id.split('_')[0]
                class_name = class_dict.get(class_id, class_name_with_id)
            
            # Create class directory if it doesn't exist
            class_dir = os.path.join(target_dir, class_name)
            os.makedirs(class_dir, exist_ok=True)
            
            # Source and destination paths
            src = os.path.join(images_dir, line)
            dest = os.path.join(class_dir, os.path.basename(line))
            
            # Copy the image to the target directory
            if os.path.exists(src):
                shutil.copyfile(src, dest)
            else:
                print(f"Warning: {src} does not exist.")

# Copy the training and testing images to their respective directories
copy_images(train_lines, output_train_dir)
copy_images(test_lines, output_test_dir)

print("Data preparation is complete.")
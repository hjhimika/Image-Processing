import cv2
import os
import zipfile
from google.colab import files

# Function to crop image and maintain aspect ratio
def crop_and_resize(image, target_width, target_height):
    h, w = image.shape[:2]
    aspect_ratio = w / h

    if aspect_ratio > target_width / target_height:
        # Width is the limiting factor, so we scale by width
        new_width = target_width
        new_height = int(new_width / aspect_ratio)
    else:
        # Height is the limiting factor, so we scale by height
        new_height = target_height
        new_width = int(new_height * aspect_ratio)

    # Resize image to maintain aspect ratio
    resized_image = cv2.resize(image, (new_width, new_height))

    # Center crop the resized image to match the target dimensions
    start_x = max(0, (new_width - target_width) // 2)
    start_y = max(0, (new_height - target_height) // 2)
    cropped_image = resized_image[start_y:start_y+target_height, start_x:start_x+target_width]

    return cropped_image

# Function to process images in a folder
def batch_process_images(input_folder, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is not None:
                cropped_image = crop_and_resize(image, target_width, target_height)
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, cropped_image)
                print(f"Processed: {filename}")

# Example usage
input_folder = "/content/input_images"  # Replace with your input folder path
output_folder = "/content/output_images"  # Replace with your output folder path
target_width = 800  # Desired width of the output image
target_height = 600  # Desired height of the output image

# Upload images
uploaded = files.upload()

# Save uploaded files to the input folder
os.makedirs(input_folder, exist_ok=True)
for file_name in uploaded.keys():
    file_path = os.path.join(input_folder, file_name)
    with open(file_path, 'wb') as f:
        f.write(uploaded[file_name])

# Process images
batch_process_images(input_folder, output_folder, target_width, target_height)

# Zip the processed images
zip_filename = "processed_images.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files_list in os.walk(output_folder):
        for file in files_list:
            zipf.write(os.path.join(root, file), file)

# Download the zip file
files.download(zip_filename)

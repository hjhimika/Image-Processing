import cv2 

image_path = r"F:\testing_data\jpg_data\SampleJPGImage_100kbmb.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Unable to read the file at {image_path}")

h, w = image.shape[:2]
ratio = w / h

target_width = 800
target_height = 600

# if (target_width / target_height) > ratio:
#     new_width = int(target_height * ratio)
#     new_height = target_height
# else:
#     new_width = target_width
#     new_height = int(target_width / ratio)
# print(new_height,new_width)

resized_image = cv2.resize(image, (target_width, target_height))

output_path = r'F:\testing_data\jpg_data\resized_image2.jpg'
cv2.imwrite(output_path, resized_image)

#print(ratio)
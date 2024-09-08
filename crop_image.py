import cv2 

image_path = r"F:\testing_data\jpg_data\SampleJPGImage_20mbmb.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Unable to read the file at {image_path}")

h, w = image.shape[:2]
aspect_ratio = w / h

crop = image[50:180, 100:300] 

save_path = r"C:\Users\USER\Pictures\result\cropped..jpg"

cv2.imshow('Cropped image',crop)
cv2.imwrite(save_path, crop)
from PIL import Image

# Load the image
input_image_path = r"C:\Users\USER\Pictures\jpg_data\SampleJPGImage_10mbmb.jpg"
image = Image.open(input_image_path)

# Rotate the image by 45 degrees
rotated_image = image.rotate(45, expand=False)

# Save the rotated image
output_image_path = r"C:\Users\USER\Pictures\result\SampleJPGImage_45degree2.jpg"
rotated_image.save(output_image_path)

# Optional: Display the rotated image
rotated_image.show()

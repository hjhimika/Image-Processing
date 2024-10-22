# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread(r"F:\testing_data\jpg_data\SampleJPGImage_20mbmb.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not loaded. Check the file path.")
else:
    # Convert the image from BGR to RGB for correct display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image_rgb)

    # Adjust brightness and contrast
    brightness = 10
    contrast = 2.3
    image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

    # Convert adjusted image to RGB for correct display
    image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    # Save the adjusted image
    save_path = r"C:\Users\USER\Pictures\result\modified_image.jpg"
    cv2.imwrite(save_path, image2)

    # Plot the adjusted image
    plt.subplot(1, 2, 2)
    plt.title("Brightness & Contrast")
    plt.imshow(image2_rgb)

    # Show the images
    plt.show()

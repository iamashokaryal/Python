import rembg
import numpy as np
from PIL import Image

# Load the input image
input_image = Image.open('IMG_8938.JPG')

# Convert the input image to a numpy array
input_array = np.array(input_image)

# Apply background removal using rembg
output_array = rembg.remove(input_array)

# Create a PIL Image from the output array
output_image = Image.fromarray(output_array)

# Create a new white background image with the same size as the original
white_background = Image.new('RGBA', input_image.size, (255, 255, 255, 255))

# Paste the output image onto the white background
white_background.paste(output_image, (0, 0), output_image)

# Save the final output image with the white background
white_background.save('output_image_with_white_background.png')

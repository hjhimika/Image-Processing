from wand.image import Image
from wand.color import Color

with Image(filename = "C:\\Users\\USER\\Pictures\\jpg_data\\koala-300x225.jpeg") as img:
    with img.clone() as rotated:
        rotated.rotate(135, background = Color('rgb(229, 221, 112)'))
        rotated.save(filename = 'file_path')

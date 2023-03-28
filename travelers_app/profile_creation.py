from PIL import Image, ImageDraw, ImageFont
import random
import string
from django.core.files import File
from io import BytesIO

def create_profile_pic(username):
    # Set the background color to sky blue
    bg_color = (135, 206, 235)

    # Create a new image with the specified background color
    image = Image.new('RGB', (200, 200), bg_color)

    # Get the first letter of the username
    letter = username[0].upper()

    # Calculate the font size and position to center the letter in the image
    font_size = 100
    font = ImageFont.truetype('arial.ttf', font_size)
    bbox = font.getbbox(letter)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw = ImageDraw.Draw(image)
    x = (200 - w) / 2
    y = (200 - h) / 2

    # Draw the letter in white on the image
    draw.text((x, y), letter, font=font, fill=(255, 255, 255))

    # Save the image as a PNG file to a BytesIO buffer
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    image_file = File(buffer)

    # Set the filename to the username with '_profile_pic.png' extension
    image_file.name = f'{username}_profile_pic.png'

    return image_file
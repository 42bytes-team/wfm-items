import os

from PIL import Image


def convert(image):
    border = 5
    if not image:
        image = input('Image: ')
    with Image.open(image) as image_icon:
        print('Process %s' % image)
        image_icon = image_icon.convert('RGBA')
        # Resize texture
        height = 342
        image_icon = image_icon.resize((512, height), Image.ANTIALIAS)
        # Get the bounding box
        r, g, b, a = image_icon.split()
        bbox = a.getbbox()
        # Crop the image to the contents of the bounding box
        image_icon = image_icon.crop(bbox)
        # Determine the width and height of the cropped image
        (width, height) = image_icon.size
        # Add border
        width += border * 2
        height += border * 2
        # Create a new image object for the output image
        cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        # Paste the cropped image onto the new image
        cropped_image.paste(image_icon, (border, border))
        cropped_image.save(os.path.splitext(image)[0].lower() + "_f.png", "PNG")
        os.remove(image)


if __name__ == '__main__':
    for image_file in os.listdir('.'):
        if 'png' in image_file:
            print('Converting: %s' % image_file)
            convert(image_file)

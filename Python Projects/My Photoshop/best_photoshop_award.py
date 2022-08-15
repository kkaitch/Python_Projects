"""
File: best_photoshop_award.py
Name: Kaiting
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the lower bound for white pixel
WHITE_PIXEL = 650


def main():
    """
    Inspiration: I like this show. - Anya Forger 𓁹‿𓁹
    """
    fig = SimpleImage('image_contest/fig.jpeg')
    bg = SimpleImage('image_contest/bg_blank.jpg')
    bg.make_as_big_as(fig)
    combine_img = combine(bg, fig)
    combine_img.show()


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, the figure image with white background
    : return me: SimpleImage, the white background pixels are replaced by pixels of background image
    """
    for x in range(me.width):
        for y in range(me.height):
            pixel_me = me.get_pixel(x, y)
            pixel_bg = bg.get_pixel(x, y)
            total = pixel_me.red + pixel_me.green + pixel_me.blue
            if total > WHITE_PIXEL:
                pixel_me.red = pixel_bg.red
                pixel_me.green = pixel_bg.green
                pixel_me.blue = pixel_bg.blue
    return me


if __name__ == '__main__':
    main()

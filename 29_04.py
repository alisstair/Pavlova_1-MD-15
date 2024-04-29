from PIL import Image, ImageDraw, ImageFont
def crop():
    im = Image.open('Z:\\1-МД-15\\Pavlova Anna\\sobaka.jpg')
    im.show()
    c_im = im.crop((100, 100, 200, 200))
    c_im.save('Z:\\1-МД-15\\Pavlova Anna\\sobaka1.jpg')
    c_im.show()
#crop()


def cards():
    h_c = {'др': 'Z:\\1-МД-15\\Pavlova Anna\\др.jpg', 'нг': 'Z:\\1-МД-15\\Pavlova Anna\\нг.jpg', '8м': 'Z:\\1-МД-15\\Pavlova Anna\\8м.jpg'}
    h = input('праздник? ')
    if h in h_c:
        f_n = h_c[h]
        if f_n:
            im = Image.open(f_n)
            im.show()
        else:
            print('error')
    else:
        print('нет открытки для такого')
#cards()

def txt():
    im = Image.open('Z:\\1-МД-15\\Pavlova Anna\\sobaka.jpg')
    fnt = ImageFont.truetype("arial.ttf", 25)
    d = ImageDraw.Draw(im)
    n = input("имя? ")
    d.text((50, 10), f"{n}, поздравляю", font=fnt, fill='black')
    im.show()
    im.save('Z:\\1-МД-15\\Pavlova Anna\\sobaka_pozdravlyaka.png')
txt()
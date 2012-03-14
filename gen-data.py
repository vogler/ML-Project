import Image, ImageDraw, ImageFont
import random, os, shutil

folder = 'data'

if os.path.exists(folder):
    shutil.rmtree(folder)

fonts = ['arial.ttf', 'ariali.ttf', 'comicbd.ttf']#, 'HARNGTON.TTF', 'FREESCPT.TTF'] #'LHANDW.TTF', 'HoboStd.otf']
size_mu = 19
size_sig = 3
pos_sig = 0
color_sig = 100
color_bg = 'white'
rotate_sig = 25
nums = xrange(1,10)
samples = xrange(0,500)
width, height = 20, 20

def distr(a, b):
    return a+random.randint(-b, b)

def rotate(image, angle, color):
    bg = Image.new("RGB", image.size, color)
    im = image.convert("RGBA").rotate(angle)
    bg.paste(im, im)
    return bg

for num in nums:
    dir = os.path.dirname(folder + '/' + str(num) + '/')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for i in samples:
        font = ImageFont.truetype(random.choice(fonts), distr(size_mu, size_sig))
        text_width, text_height = font.getsize(str(num))
        #print text_width, text_height
        img = Image.new('RGB', (width, height), color_bg)
        draw = ImageDraw.Draw(img)
        pos = (width/2-text_width/2, height/2-text_height/3)
        pos = pos[0]+distr(0, pos_sig), pos[1]+distr(0, pos_sig)
        v = random.randint(0, color_sig)
        draw.text(pos, str(num), font=font, fill=(v,v,v))
        img = rotate(img, distr(0, rotate_sig), color_bg)
        img.save(os.path.join(dir, str(i)+'.png'))
        

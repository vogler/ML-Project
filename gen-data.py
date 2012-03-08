import Image, ImageDraw, ImageFont
import random, os, shutil

folder = 'data'

if os.path.exists(folder):
    shutil.rmtree(folder)

fonts = ['arial.ttf', 'ariali.ttf', 'comicbd.ttf']
size_mu = 20
size_sig = 3
color_sig = 100
nums = xrange(1,10)
samples = xrange(0,100)

def distr(a, b):
    return a+random.randint(-b, b)

for num in nums:
    dir = os.path.dirname(folder + '/' + str(num) + '/')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for i in samples:
        font = ImageFont.truetype(random.choice(fonts), distr(size_mu, size_sig))
        text_width, text_height = font.getsize(str(num))
        #print text_width, text_height
        width, height = 20, 20
        img = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(img)
        pos = (width/2-text_width/2, height/2-text_height/3)
        v = random.randint(0, color_sig)
        draw.text(pos, str(num), font=font, fill=(v,v,v))
        img.save(os.path.join(dir, str(i)+'.png'))
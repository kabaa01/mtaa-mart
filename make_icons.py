from PIL import Image, ImageDraw, ImageFont
import io, base64

def make_icon(size):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    # Green circle background
    d.ellipse([0,0,size-1,size-1], fill='#1A5E36')
    # Gold "M" text
    fs = int(size * 0.55)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', fs)
    except:
        font = ImageFont.load_default()
    bbox = d.textbbox((0,0), 'M', font=font)
    tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
    x = (size - tw) // 2 - bbox[0]
    y = (size - th) // 2 - bbox[1]
    d.text((x, y), 'M', fill='#F9A825', font=font)
    img.save(f'icons/icon-{size}.png')
    print(f'icon-{size}.png created')

make_icon(192)
make_icon(512)

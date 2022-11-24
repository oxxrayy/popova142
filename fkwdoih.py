from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (800,600), color=('#FAACAC'))
font = ImageFont.truetype('C:/Users/user/Desktop/arial.ttf', size=18)
draw_text = ImageDraw.Draw(im)
draw_text.text((100,100),
    'опрл',
    font=font,
    fill=('#1C0606'))        
im.show()
            

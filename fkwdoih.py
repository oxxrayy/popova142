from PIL import Image, ImageDraw, ImageFont
def f(t, i):
    im = Image.new('RGB', (800,600), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Users/user/Desktop/arial.ttf', size=22)
    draw_text = ImageDraw.Draw(im)
    draw_text.text((100,100),
    t,
    font = font,
    fill=('#7d69df'))
    im.save()

t=['В ад перед тобой, в рай после тебя',
'Вместе с тобой, что можно',
'Вместо тебя всё то, что нельзя',
'В рай только после тебя',
'В ад только перед тобой',
'В ад перед тобой, в рай после тебя',
'Вместе с тобой, что можно',
'Вместо тебя всё то, что нельзя',
'В рай только после тебя',
'В ад только перед тобой' ]
for i in range (10):
    f (t[i], i)

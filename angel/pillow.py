from PIL import Image, ImageDraw, ImageFont
from numerize import numerize
from io import BytesIO
import requests
bg_image_path = "card.png"
image_url = https://assets.mulearn.org/misc/user.png
name = Aashish Vinu
institute = College of figma engineering
i_area = Cyber security , web developing , app developing
rank = 1
karma = 13500
avatar = BytesIO(requests.get(image_url).content)
im = Image.open(avatar)
if im.size[0] < 256 or im.size[1] < 256:
    im = im.resize((256, 256))

font_name = "PlusJakartaSans-Medium"

karma_color = "rgb(255, 80, 89)"
rank_color = "rgb(143, 90, 255)"
# git_color = 'rgb(105, 105, 105)'
color = "rgb(41, 142, 165)"

bigsize = (im.size[0] * 3, im.size[1] * 3)
mask = Image.new("L", bigsize, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(im.size, Image.LANCZOS)
im.putalpha(mask)

im = im.resize((round(im.size[0] * 0.67), round(im.size[1] * 0.67)))

background = Image.open(bg_image_path)
draw = ImageDraw.Draw(background)


font = ImageFont.truetype(font_name, size=35)
draw.text((110, 250), name, fill=color, font=font)
font = ImageFont.truetype(font_name, size=21)

if len(institute) > 0:
    institute = institute[0]
    draw.text(
        (110, 290),
        institute,
        fill=color,
        font=font,
    )

# Area of Interest

font = ImageFont.truetype(font_name, size=25)
y = 120

for area in i_area:
    if len(area) > 20:
        font = ImageFont.truetype(font_name, size=20)
        # area_ = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', area[20:], 1)
        draw.text(
            (370, y), "#" + area[:19] + "\n" + area[19:], fill=color, font=font
        )
        y = y + 20
    else:
        draw.text((370, y), "#" + area, fill=color, font=font)
    y = y + 30

# Karma
font = ImageFont.truetype(font_name, size=32)
draw.text((370, 72), karma, fill=karma_color, font=font)

# Rank

font = ImageFont.truetype(font_name, size=32)
draw.text((568, 72), rank, fill=rank_color, font=font)

# github

if git is True:
    font = ImageFont.truetype(font_name, size=24)
    spacing = 15
    draw.multiline_text((175, 420), text_left, fill=rank_color,
                        font=font, spacing=spacing, align="left")
    draw.multiline_text((440, 420), text_right, fill=rank_color,
                        font=font, spacing=spacing, align="left")

background.paste(im, (116, 62), im)
out = BytesIO()
background.save(out, format="PNG")
background.show()

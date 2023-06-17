        background = Image.open("Dboard.png")
        # draw = ImageDraw.Draw(background)
        karma_color = "rgb(255, 80, 89)"
        color = "white"
        font = ImageFont.truetype("roboto.ttf", 50)
        font_karma = ImageFont.truetype("roboto.ttf", 40)
        font_college = ImageFont.truetype("roboto.ttf", 25)
        font_rank = ImageFont.truetype("roboto.ttf", 45)
        x, y = 285, 66
        i = 0
        j = 0
        c = 1
        url = "https://assets.mulearn.org/misc/user.png"
        avatar = BytesIO(requests.get(url).content)
        im = Image.open(avatar)
        bigsize = (im.size[0] * 3, im.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(im.size, Image.LANCZOS)
        im.putalpha(mask)

        im = im.resize((110, 110))

    college = "orgs"
    if len(college) > 0:
        college = college[0]
        draw.multiline_text(
            (y + 130, x),
            "\n\n" + college[:35] + "\n" + college[35:],
            fill=color,
            font=font_college,
            align="left",
        )
    r = numerize.numerize(13000)
    draw.multiline_text(
        (y + 485, x - 70),
        r,
        fill=karma_color,
        font=font_karma,
        align="left",
    )

    out = BytesIO()
    background.save(out, format="PNG")

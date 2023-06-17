        from PIL import Image, ImageDraw, ImageFont
        import requests
        from numerize import numerize
        from io import BytesIO
        background = Image.open("Dboard.png")
        karma_color = "rgb(255, 80, 89)"
        color = "white"
        font = ImageFont.truetype("PlusJakartaSans-Bold.ttf", 110) # size of name
        font_karma = ImageFont.truetype("Inter-Black.ttf", 115)  #size of karma
        font_college = ImageFont.truetype("PlusJakartaSans-Medium.ttf", 70) #size of college
        x, y = 0,0
        c = 1
        # for discord_id, data in total_students_score.items():
        # if c > 13:
        #     break
        # if discord_id is not None:

        url = "https://assets.mulearn.org/misc/user.png"
        avatar = BytesIO(requests.get(url).content)
        im = Image.open(avatar)
        bigsize = (im.size[0] * 3, im.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(im.size, Image.LANCZOS)
        im.putalpha(mask)
        im = im.resize((290, 290)) #size of image
        draw = ImageDraw.Draw(background)
        background.paste(im, (y+20, x-50), im)

        name = "Aashish Vinu"
        if len(name) > 18:
            name = name.split(" ")
            if len(name) > 1:
                name = name[0] + " " + name[1]
                if len(name) > 19:
                    name = name.split(" ")
                    name = name[0] + " " + name[1][0].capitalize()
            else:
                name = str(name[0])
        draw.multiline_text((y + 350, x - 50), name, fill=color, font=font, align="center")
        name = "College of figma engineering"
        name = name.upper()
        if len(name) > 17:
            first_line = name[:25]
            second_line = name[25:].strip()
            if second_line and second_line[0].isalpha() and first_line[-1].isalpha():
                split_index = first_line.rfind(' ')
                if split_index == -1:
                    split_index = 25
                second_line = name[split_index:].strip()
                first_line = name[:split_index].strip()
            draw.multiline_text((y + 355, x + 70), first_line + "\n" + second_line, fill=color, font=font_college,
                                align="left")
        else:
            draw.multiline_text((y + 355, x + 70), name, fill=color, font=font_college, align="center")

        r = numerize.numerize(1350)
        draw.multiline_text(
            (y + 310, x - 295),
            r,
            fill=color,
            font=font_karma,
            align="left",
        )
            # c = c + 1
            # y = y + 737
            # j = j + 1
            # if j % 3 == 0:
            #     i = i + 1
            #     j = 0
            #     y = 66
            #     x = x + 265
        out = BytesIO()
        background.save(out, format="PNG")
        background.show()
        out.seek(0)

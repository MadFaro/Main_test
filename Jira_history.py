            imgs = await file_upload("Select some pictures:", accept="image/*", multiple=False)
            image = Image.open(BytesIO(imgs['content']))
            if image.width < 300:
                image.save(f"img/{imgs['filename']}")
            else:
                new_width = 300
                aspect_ratio = image.height / image.width
                new_height = int(new_width * aspect_ratio)
                resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
                resized_image.save(f"img/{imgs['filename']}")

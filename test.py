def get_image_base64(path):
    with open(path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Пусть изображение находится по пути 'img/ban.jpg'
image_path = 'img/ban.jpg'  # относительный путь
image_data_url = f"data:image/jpeg;base64,{get_image_base64(image_path)}"

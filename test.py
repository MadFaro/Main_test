all_pins = await pin  # Получение всех данных из pin
name_up_pin = all_pins['admin_update_product_name']
price_up_pin = all_pins['admin_update_product_price']
desc_up_pin = all_pins['admin_update_product_desc']
size_up_pin = all_pins.get('admin_update_product_size')  # .get() для необязательных данных
color_up_pin = all_pins.get('admin_update_product_color')
prom_up_pin = all_pins['admin_update_product_prom']

print(name_up_pin, price_up_pin, desc_up_pin)

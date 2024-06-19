def custom_strikethrough(text):
    result = ""
    for char in text:
        result += char + "\u0336"
    return result

import pandas as pd
from transformers import T5ForConditionalGeneration, T5Tokenizer

device = 'cpu'
model_name = 'trans/'
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tokenizer = T5Tokenizer.from_pretrained(model_name)

data = pd.read_excel("test.xlsx", sheet_name="Свод")
texts = data['MSG']
categories = data['CATEGORY']

def augment_text_translate(text):
    # Разбиваем текст на части по токенам
    max_token_length = 512  # Максимальная длина последовательности токенов для модели
    parts = []
    current_part = ""
    current_token_count = 0
    for token in text.split():
        token_length = len(tokenizer.encode(token, add_special_tokens=False))
        if current_token_count + token_length <= max_token_length:
            current_part += token + " "
            current_token_count += token_length
        else:
            parts.append(current_part.strip())
            current_part = token + " "
            current_token_count = token_length
    if current_part:
        parts.append(current_part.strip())
    
    augmented_text = ""
    for part in parts:
        # Переводим часть текста на английский
        prefix_1 = 'translate to en: '
        src_text_1 = prefix_1 + part
        input_ids_1 = tokenizer(src_text_1, return_tensors="pt", max_length=max_token_length, truncation=True)
        generated_tokens_1 = model.generate(**input_ids_1.to(device))
        result_1 = tokenizer.batch_decode(generated_tokens_1, skip_special_tokens=True)
        # Переводим результат обратно на русский
        prefix_2 = 'translate to ru: '
        src_text_2 = prefix_2 + result_1[0]
        input_ids_2 = tokenizer(src_text_2, return_tensors="pt", max_length=max_token_length, truncation=True)
        generated_tokens_2 = model.generate(**input_ids_2.to(device))
        result_2 = tokenizer.batch_decode(generated_tokens_2, skip_special_tokens=True)
        augmented_text += result_2[0] + "\n"
    return augmented_text

# Открываем файл для записи в режиме 'w' (заменяет существующий файл или создает новый)
with open('augmented_data.csv', 'w', encoding='utf-8') as f:
    # Записываем заголовок
    f.write("MSG,CATEGORY\n")
    # Проход по каждой паре текст-категория и запись аугментированных данных
    for text, category in zip(texts, categories):
        f.write(f"{text},{category}\n")
        # Аугментация текста: перевод на три языка поочередно и запись в файл
        augmented_text_translate = augment_text_translate(text)
        f.write(f"{augmented_text_translate},{category}\n")

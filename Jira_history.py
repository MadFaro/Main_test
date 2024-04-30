import pandas as pd
from transformers import T5ForConditionalGeneration, T5Tokenizer

device = 'cpu'
model_name = 'trans/'
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tokenizer = T5Tokenizer.from_pretrained(model_name)

data = pd.read_excel("test1.xlsx", sheet_name="Свод")
texts = data['MSG']
categories = data['CATEGORY']

def augment_text_translate(text):
    # Разбиваем текст на части по 500 символов
    parts = [text[i:i+500] for i in range(0, len(text), 500)]
    augmented_text = ""
    for part in parts:
        # Переводим часть текста на английский
        prefix_1 = 'translate to en: '
        src_text_1 = prefix_1 + part
        input_ids_1 = tokenizer(src_text_1, return_tensors="pt", max_length=512, truncation=True)
        generated_tokens_1 = model.generate(**input_ids_1.to(device))
        result_1 = tokenizer.batch_decode(generated_tokens_1, skip_special_tokens=True)
        result_1 = result_1[0] if result_1 else ""  # Проверяем, что результат не пустой
        # Переводим результат обратно на русский
        prefix_2 = 'translate to ru: '
        src_text_2 = prefix_2 + result_1
        input_ids_2 = tokenizer(src_text_2, return_tensors="pt", max_length=512, truncation=True)
        generated_tokens_2 = model.generate(**input_ids_2.to(device))
        result_2 = tokenizer.batch_decode(generated_tokens_2, skip_special_tokens=True)
        result_2 = result_2[0] if result_2 else ""  # Проверяем, что результат не пустой
        # Добавляем переведенную часть к общему тексту
        augmented_text += result_2
    return augmented_text

output_file = "augmented_data.xlsx"  # Имя файла для сохранения результата

with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for text, category in zip(texts, categories):
        augmented_text_translate = augment_text_translate(text)
        # Записываем данные в файл по мере их обработки
        pd.DataFrame({'MSG': [text, augmented_text_translate], 'CATEGORY': [category, category]}).to_excel(writer, index=False)

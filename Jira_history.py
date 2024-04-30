Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
Token indices sequence length is longer than the specified maximum sequence length for this model (2244 > 512). Running this sequence through the model will result in indexing errors

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
    # Перевод текста на английский
    prefix_1 = 'translate to en: '
    src_text_1 = prefix_1 + text
    input_ids_1 = tokenizer(src_text_1, return_tensors="pt")
    generated_tokens_1 = model.generate(**input_ids_1.to(device))
    result_1 = tokenizer.batch_decode(generated_tokens_1, skip_special_tokens=True)
    # Перевод текста на русский
    prefix_2 = 'translate to ru: '
    src_text_2 = prefix_2 + result_1[0]
    input_ids_2 = tokenizer(src_text_2, return_tensors="pt")
    generated_tokens_2 = model.generate(**input_ids_2.to(device))
    result_2 = tokenizer.batch_decode(generated_tokens_2, skip_special_tokens=True)
    return result_2

augmented_texts = []
augmented_categories = []

for text, category in zip(texts, categories):
    augmented_texts.append(text)
    augmented_categories.append(category)
    
    augmented_text_translate = augment_text_translate(text)
    augmented_texts.append(augmented_text_translate)
    augmented_categories.append(category)

augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

augmented_data.to_excel("augmented_data.xlsx", index=False)

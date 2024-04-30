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
        augmented_text += result_2[0]
    return augmented_text


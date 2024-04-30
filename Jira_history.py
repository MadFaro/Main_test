        # Записываем данные в файл по мере их обработки
        df = pd.DataFrame({'MSG': [text, augmented_text_translate], 'CATEGORY': [category, category]})
        df.to_excel(writer, index=False, header=False, startrow=len(df) + 1 if len(df) > 0 else 0)

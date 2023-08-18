def check_phrases(text, phrases):
    normal = pymorphy2.MorphAnalyzer()
    normal_text = [normal.parse(token)[0].normal_form for token in nltk.word_tokenize(text)]
    found_phrases = []
    
    for phrase in phrases:
        normal_phrase = [normal.parse(token)[0].normal_form for token in nltk.word_tokenize(phrase)]
        if ' '.join(normal_phrase) in ' '.join(normal_text):
            found_phrases.append(phrase)
    
    return found_phrases

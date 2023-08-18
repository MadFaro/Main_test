def check_phrases(text, phrases):
    normal = pymorphy2.MorphAnalyzer()
    tokens = nltk.word_tokenize(text)
    normal_tokens = [normal.parse(token)[0].normal_form for token in tokens]
    found_phrases = []
    for phrase in phrases:
        phrase_tokens = nltk.word_tokenize(phrase)
        normal_phrase = [normal.parse(token)[0].normal_form for token in phrase_tokens]
        if all(token in normal_tokens for token in normal_phrase):
            found_phrases.append(phrase)
    return found_phrases

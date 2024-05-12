from textblob import TextBlob , Word


class Text_blob:
    
    def pos_tag(self, text):
        blob = TextBlob(text)
        print(blob.tags)

    def noun_phrase_extraction(self, text):
        blob = TextBlob(text)
        print(blob.noun_phrases)

    def sentiment_analysis(self, text):
        blob = TextBlob(text)
        print(blob.sentiment)

    def tokenize(self, text):
        blob = TextBlob(text)
        print(blob.words)

        print(blob.sentences)

    def lemmatization(self, text):
        blob = TextBlob(text)
        word = blob.words

        print(word[0].singularize())
        print(word[0].pluralize())
        print(word[0].lemmatize())
    
    def synonym_set(self, text):
        word = Word(text)
        print(word.synsets)

    def meaning_of_word(self , text):
        word = Word(text)
        print(word.definitions)

    def spelling_correction(self , text):
        word = TextBlob(text)
        print(word.correct())

    def spell_check(self , text):
        word = Word(text)
        print(word.spellcheck())

    def word_freq(self, text):
        word = TextBlob(text)
        print(word.word_counts)

    def language_translation_eng_to_hindi(self , text):
        blob = TextBlob(text)
        print(blob.translate(to='hi'))

    def language_translation_chinese_to_eng(self, text):
        blob = TextBlob(text)
        print(blob.translate(from_lang='zh-CN' , to='en'))

    def language_detection(self , text):
        blob = TextBlob(text)
        print(blob.detect_language())

    def n_grams(self, text):
        blob = TextBlob(text)
        print(blob.ngrams(n=3))




if __name__ == '__main__':
    blob = Text_blob()
    # blob.pos_tag('hello this is Virat Kholi here')
    # blob.noun_phrase_extraction('hello this is Virat Kholi here')
    # blob.tokenize('you are very very good')
    # blob.lemmatization('you are very very good')
    # blob.spelling_correction('i have a good coputer')
    # blob.word_freq('you are very very good')
    # blob.language_translation_eng_to_hindi(u'go and die')
    # blob.language_translation_chinese_to_eng(u'有总比没有好')
    # blob.language_detection(u'有总比没有好')
    blob.n_grams('hello this is Virat Kholi here')







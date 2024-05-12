#importing important libraries
import nltk
import string
import re
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import wordnet
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag , ne_chunk
from nltk.tokenize.regexp  import WhitespaceTokenizer
from nltk.tokenize.regexp  import WordPunctTokenizer
from nltk import FreqDist

#uncomment this to download stopwords
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('gutenberg')



class text_preprocess():
    def __init__(self):
        self.num_to_word = inflect.engine()
        self.translator = str.maketrans('' , '' , string.punctuation)

    def lower_case(self , text):
        print(text.lower())

    def remove_numbers_from_txt(self , text):
        result = re.sub(r'\d+' , '', text)
        print(result)
        

    def convert_num_to_text(self , text):
        word_list = text.split()
        new_str = []

        for word in word_list:
            if word.isdigit():
                word = self.num_to_word.number_to_words(word)
                new_str.append(word)
            else:
                new_str.append(word)
        temp_str = " ".join(new_str)
        print(temp_str)

    def remove_punctuation(self , text):
        print(text.translate(self.translator))

    def remove_stopwords(self, text):
        stopword = list(stopwords.words('english'))
        token = word_tokenize(text)
        word = [word for word in token if word not in stopword]
        temp_str = " ".join(word)
        print(temp_str)

    def stemming(self , text):
        stem = PorterStemmer()
        tokenize_Word = word_tokenize(text)
        stem_words = [ stem.stem(word) for word in tokenize_Word]
        print(stem_words)
        tem_str = " ".join(stem_words)
        print(tem_str)

    def lemmatization(self, text):
        lem = wordnet.WordNetLemmatizer()
        tokenize_Word = word_tokenize(text)
        lem_words = [ lem.lemmatize(word) for word in tokenize_Word]
        print(lem_words)
        tem_str = " ".join(lem_words)
        print(tem_str)

    def pos_tagging(self , text):
        tokenize_Word = word_tokenize(text)
        pos = pos_tag(tokenize_Word)
        print(pos)

    def name_entity_recognition(self, text):
        word_tokens = word_tokenize(text) 
        word_pos = pos_tag(word_tokens) 
        print(ne_chunk(word_pos))

    def white_space_tokenizer(self, text):
        token = WhitespaceTokenizer().tokenize(text)
        print(f' number of words are {len(token)}')

        # remove duplicates from sentence
        print(set(token))
        print(f' number of words after removing duplication {len(set(token))}')

    def word_punct_tokenizer(self, text):
        token = WordPunctTokenizer().tokenize(text)
        print(f' number of words including punctuation {len(token)}')

        print(f' number of words after removing duplication {len(set(token))}')

    def frequency_distribution(self, text):
        freq = FreqDist(word_tokenize(text))
        print(freq)
        print(freq['in'])

    def frequency_distribution_plot(self, text):
        freq = FreqDist(word_tokenize(text))
        freq.plot()


if __name__ == "__main__":
    nltk = text_preprocess()
    # nltk.lower_case('Hello WORLD')
    # nltk.remove_numbers_from_txt('hello 4 world')
    # nltk.remove_stopwords('you bought 6 candies and 4 are at home')
    # nltk.remove_punctuation('hello!!! , world!!!!!')
    # nltk.stemming('Data is the new revolution in the World, in a day one individual would generate terabytes of data.')
    # nltk.lemmatization('Data is the new revolution in the World, in a day one individual would generate terabytes of data.')
    # nltk.pos_tagging('Data is the new revolution in the World, in a day one individual would generate terabytes of data.')
    # nltk.name_entity_recognition('Data is the new revolution in the World, in a day one individual would generate terabytes of data.')
    nltk.frequency_distribution_plot('Data is the new revolution in the World, in a day one individual would generate terabytes of data.')




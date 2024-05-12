from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


class Blob_classifier():
    def __init__(self):
        self.cl = 0

    def train(self , train_data):
        self.cl = NaiveBayesClassifier(train)

    def json_train(self , train_json_file):
        with open('train.json', 'r') as fp:
            self.cl = NaiveBayesClassifier(fp, format="json")

    def classify_textblob(self , text):
        blob = TextBlob("Alcohol is good. But the hangover is horrible.", classifier=self.cl)
        print(blob.classify())


    def update_model(self , data):
        self.cl.update(data)

    def inference(self , text):
        self.cl.classify(text)
        print(self.cl.classify(text))

    def evaluation(self , test_data):
        print(self.cl.accuracy(test_data))

if __name__ == '__main__':
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
    ]

    test = [
        ('the beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')
    ]
    update_data = [('She is my best friend.', 'pos'),
           ("I'm happy to have a new friend.", 'pos'),
           ("Stay thirsty, my friend.", 'pos'),             
           ("He ain't from around here.", 'neg')]


    classifier = Blob_classifier()
    classifier.train(train)
    classifier.inference("This is an amazing library!")
    classifier.classify_textblob("This is an amazing library!")
    classifier.update_model(update_data)
    classifier.evaluation(test)



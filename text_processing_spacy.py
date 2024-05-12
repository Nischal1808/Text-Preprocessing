import spacy
from spacy import displacy
import spacy.cli

# spacy.cli.download('en_core_web_md')

nlp = spacy.load('en_core_web_sm')
nlp_md = spacy.load('en_core_web_md')
class Spacy():

    def tokenization(self , text):
        doc = nlp(text)
        for token in doc:
            print(token.text, token.pos_ , token.dep_)

    def part_of_Speech(self,text):
        doc = nlp(text)
        for token in doc:
            print(token.text, token.lemma_ , token.pos_ , token.tag_, token.shape_, token.is_alpha, token.is_stop)

    def dispay_dependencies(self, text):
        doc = nlp(text)
        displacy.serve(doc , style = 'dep') #dep means dependency

    def entities(self, text):
        doc = nlp(text)
        for ent in doc.ents:
            print(ent.text , ent.start_char, ent.end_char, ent.label_)

    def dispay_dependencies(self, text):
        doc = nlp(text)
        displacy.serve(doc , style = 'ent') #dep means dependency
    
    def vector(self, text):
        tokens = nlp_md(text)
        for token in tokens:
            print(token.has_vector, token.vector_norm )
    
    def similarity(self, text):
        tokens = nlp_md(text)
        for token1 in tokens:
            for token2 in tokens:
                print(token1.text, token2.text , token1.similarity(token2) )


if __name__ == '__main__':
    obj = Spacy()
    # obj.tokenization('Apple is looking at buying U.K. startup for $1 million')
    # obj.part_of_Speech('Apple is looking at buying U.K. startup for $1 million')
    # obj.dispay('Apple is looking at buying U.K. startup for $1 million')
    # obj.dispay('Apple is looking at buying U.K. startup for $1 million')
    # obj.entities('Apple is looking at buying U.K. startup for $1 million')
    # obj.dispay_dependencies('Apple is looking at buying U.K. startup for $1 million')
    # obj.vector('Apple Banana king queen sadfsdfsadfsadfsadf')
    obj.similarity('Apple Banana king queen sadfsdfsadfsadfsadf')

    


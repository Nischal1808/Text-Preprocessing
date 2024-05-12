import stanza
# stanza.download('en') #uncomment this to downlaod the english model

nlp = stanza.Pipeline('en')
doc = nlp("Afsan was born in Goa")

print(doc.sentences[0].print_dependencies())
print(doc.sentences[0].print_tokens())
print(doc.sentences[0].sentiment)


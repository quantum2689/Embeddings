import gensim.downloader as gd

# this isn't transformers.
#it will take somethime to answer 


inp = input("enter your word or number: ")

def embeddings(inp):
    model = gd.load("glove-wiki-gigaword-50")

    return model[inp]

print(embeddings(inp))

from tensorflow.keras.preprocessing.text import Tokenizer
from optimus import optimus_compare as opticmp

def unoptimized_tokenizer(data):
    tokenizer = Tokenizer(num_words = 100)
    tokenizer.fit_on_texts(data)
    word_index = tokenizer.word_index
    return word_index


def optimized_tokenizer(data):
    words = set()

    for line in data:
        for word in line.split():
            words.add(word.lower())

    draft_token = list(words)
    tokened_list = list(enumerate(draft_token))
    tokens = dict()
    for key, value in tokened_list:
        tokens[key + 1] = value 

    return tokens


data = [
    "I have a dog",
    "He is very lovely"
]

print()
opticmp('unoptimized_tokenizer', 'optimized_tokenizer', (data, ), (data, ), iterations = 10, multiplier = 10000, verbose = True)
print()

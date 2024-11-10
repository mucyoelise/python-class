sentence = input('Provide a sentence: ')
def dict_sentence():
    words = sentence.split()
    return({words[i] : words.count(words[i]) for i in range(len(words))})
print (f'Words with their respective frequency in a sentence provided:\n{dict_sentence()}')
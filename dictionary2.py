sentence = input('Provide a sentence: ')
dictionary = {}
def dict_fuct():
    for i in range(len(sentence)):
        if sentence[i].isalpha():        
            dictionary.update({sentence[i]:sentence.count(sentence[i])})
dict_fuct()
print(dictionary)
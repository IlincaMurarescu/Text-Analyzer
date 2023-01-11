import sys

import Validations
import Counters

def text_analyze(file):

    with open(file, 'r') as file:
        text=file.read()


    output_text=''

    words=Counters.count_words(text)
    output_text+=f'Cuvinte = {words} \n'

    sentences=Counters.count_sentences(text)
    output_text+=f'Propozitii = {sentences} \n'

    CNPs=Counters.count_CNPs(text)
    output_text+=f'CNP(uri) = {CNPs[0]} {CNPs[1]} \n'
    output_text+=f'Dintre care CNP(uri) unice = {CNPs[2]} {CNPs[3]} \n'


    phones=Counters.count_phone_numbers(text)
    output_text+=f'Telefoane = {phones[0]} {phones[1]} \n'
    output_text+=f'Dintre care telefoane unice = {phones[2]} {phones[3]} \n'


    output_text+='Litere: \n'
    letters=Counters.count_letters(text)

    for key in letters:
        output_text+=f'{key} = {letters[key][0]} ({letters[key][1]}%) \n'

    print(output_text)
    return  words, sentences, phones, CNPs, letters



if __name__ == '__main__':

    text_analyze(sys.argv[1])






    # with open('fisier.txt', 'r') as file:
    #     text=file.read()
    # print(Counters.count_words(text))
    # print(Counters.count_sentences(text))
    # print(Counters.count_phone_numbers(text))
    # print(Counters.count_CNPs(text))
    # print(Counters.count_letters(text))



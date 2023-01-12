import Validations
import re

def clean_of_punctuation(word):
    punctuation=[',', '.', ':', '?', '!', '*', '$', '#', '@', ';']
    if word in punctuation:
        return False
    return word.strip(',.?!:*#@;')

def count_phone_numbers(text):
    count=0
    list_phone_numbers=[]

    words=text.split()
    for word in words:
        word=clean_of_punctuation(word)
        if word is not False:
            if Validations.check_phone_number(word)==True:
                # if word not in list_phone_numbers:
                    count+=1
                    list_phone_numbers.append(word)

    unique_phones = []
    unique_phones_count = 0
    for phone in list_phone_numbers:
        if list_phone_numbers.count(phone) == 1:
            unique_phones.append(phone)
            unique_phones_count += 1

    return count, list_phone_numbers, unique_phones_count, unique_phones

def count_CNPs(text):
    count = 0
    list_CNP = []

    words = text.split()
    for word in words:
        word = clean_of_punctuation(word)
        if word is not False:
            if Validations.check_CNP(word) == True:
                # if word not in list_CNP:
                    count += 1
                    list_CNP.append(word)

    unique_CNP=[]
    unique_CNP_count=0
    for cnp in list_CNP:
        if list_CNP.count(cnp)==1:
            unique_CNP.append(cnp)
            unique_CNP_count+=1


    return count, list_CNP, unique_CNP_count, unique_CNP


def count_words(text):
    count=0

    words=text.split()
    for word in words:
        word=clean_of_punctuation(word)
        if word is not False:
                count+=1

    return count

def count_sentences(text):

    return text.count('.')+text.count('?')+text.count('!')-text.count('?!')-text.count('!!')-text.count('??')-text.count('..')-text.count('...')


def get_percentage(current_case, total_number):
    return int(current_case/total_number*100)


def count_letters(text):
    dex_count={}
    total_letters=0

    for character in text:
        if character.isalpha():
            total_letters+=1
            if character.upper() in dex_count:
                dex_count[character.upper()]+=1
            else:
                dex_count[character.upper()]=1



    for key in dex_count:
        perectange=get_percentage(dex_count[key], total_letters)
        dex_count[key]=[dex_count[key], perectange]


    dex_count=dict(sorted(dex_count.items()))

    return dex_count

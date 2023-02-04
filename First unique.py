import re
import sys


symbols_collection = []

def parse_file():
    with open('test.txt') as file:
        for str in file.readlines():
            line = re.findall('[a-zA-Z]+', str)
            print(line)
            parse_line(line)
    symbols_to_string = ''.join(symbols_collection)
    print(parse_word(symbols_to_string))

def parse_line(str):
    for word in str:
        if len(word) == len(set(word)):
            symbols_collection.append(word[0])
        else:
            symbols_collection.append(parse_word(word))

def parse_word(word):
    for symbol in list(word):
        if word.count(symbol) == 1:
            return symbol     
    return ''

parse_file()
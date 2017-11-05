# Strukov Alexandr, 11-5

from datetime import datetime

def ExistenceOfFiles(name, type):

    try:
        return open('{}.txt'.format(name), 'x+')
    except FileExistsError:
        return open('{}.txt'.format(name), '{}'.format(type))

def Number(name):

    F = open('{}.txt'.format(name), 'r+')
    line = F.readlines()
    F.close()

    i = 1
    try:
        while not str(line[-i][1]).isalpha():
            try:
                return int(line[-i][1])
            except ValueError:
                i += 1
    except IndexError:
        return 0

def AllFilesInOne(name_of_files):

    Universal = open('AllQuotes.txt', 'w')

    Universal.write('Hi, guy!' + '\n' + 'Here are your quotes:' + '\n')

    for file in name_of_files:
        Excerpt = open('{}.txt'.format(file), 'r')

        Universal.write('\n' + file + '\n')
        for line in Excerpt.readlines():
            Universal.write('\t' + str(line[:-1:]) + '\n')

        Excerpt.close()

    Universal.write('\n' + '(C) Sasha Strukov' + '\n' + datetime.today().strftime('%d-%m-%Y %H:%M:%S'))

    Universal.close()


def ShortString(String):
    if len(String) > 100:
        for char in range(100, len(String), 100):
            space = String[:char:].rfind(' ')
            String = String[:space:] + '\n  ' + String[space::]

    return String


No = [line[:-1:] for line in open('No.txt', 'r').readlines()]

print('Do you want to add some quotes?')
response = input()

while response not in No:

    Library = ExistenceOfFiles('Names_of_books', 'r+')
    library = [line[:-1:] for line in Library]

    print('Print a book, where the quote is: (Write an author or the name of the book)')
    book = input()
    if str(library).find(book) == -1:
        Library.write(book + '\n')
    else:
        book = str([word for word in library if book in word])[2:-2:]

    print('Print the phrases, you want to be written: (Print smth negative to stop)')
    phr = input()
    while phr not in No:
        Quote = ExistenceOfFiles(book, 'a+')
        phr = ShortString(phr)
        count = Number(book) + 1
        Quote.write('#{} {}\n'.format(count, phr))
        Quote.close()
        phr = input()

    print('Another book?')
    response = input()

    Library.close()

else:
    print('Do you want to see every quote, you`ve wtitten?')
    if input() not in No:
        Library = ExistenceOfFiles('Names_of_books', 'r+')
        AllFilesInOne([line[:-1:] for line in Library])
        Library.close()
    else:
        print('It`s a pity!\nBye!')

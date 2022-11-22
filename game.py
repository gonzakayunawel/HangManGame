import os, random

def run():

    word='PERRO'
    blank= str('_'*len(word))
    new_word = list(word)

    def present():
        os.system("clear")
        print('Welcome to the HangManGame')
        print('\nTry to guess the word!')
        print('\n')

    def findLetter(letter, word):
      index = [i for i,c in enumerate(word) if c == letter]
      if len(index) == 0:
        return -1
      else:
        return index[0]



    def changeWord(index, blank, letter):
      blank = list(blank)
      if index == -1:
        return 'Not Found.'
      else:
        blank[index] = letter
        return ''.join(blank)

    def separate_blank(string_user_try):
      return ' '.join(string_user_try)


    while True:

      option = input('Ingresa una letra ...')
      user_try = changeWord(findLetter(option.upper(), word), blank, option.upper())
      print(separate_blank(changeWord(findLetter(option.upper(), word), user_try, option.upper())))

if __name__ == '__main__':
    run()

# https://www.techiedelight.com/find-index-character-python-string/#:~:text=The%20standard%20solution%20to%20find%20a%20character%E2%80%99s%20position,returns%20-1%20when%20the%20character%20is%20not%20found.
# Enumarate Function


# Colab

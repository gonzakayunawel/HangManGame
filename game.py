import os

def run():

    word = 'PERRO'
    blank = str('_'*len(word))

    # Muestra el inicio y limpia la pantalla

    def present():
      os.system("clear")
      print('Welcome to the HangManGame')
      print('\nTry to guess the word!')

    # Encuentra la letra indicada en la palabra
    # Si encuentra la letra devuelve el índice de la letra en la palabra
    # Si no se encuentra devuelve -1
    # letter = la letra del usuario
    # word = la palabra a adivinar
    
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
    
    present()
    count = 0
    user_options = []
    while True:
      option = input('Please enter a letter... ')
      if findLetter(option.upper(), word) == -1:
        print('Not found.')
        count += 1
      elif count == 3:
        print('You lose')
        break
      else:
        user_options.append(changeWord(findLetter(option.upper(), word), blank, option.upper()))
        print(user_options)

if __name__ == '__main__':
    run()

# https://www.techiedelight.com/find-index-character-python-string/#:~:text=The%20standard%20solution%20to%20find%20a%20character%E2%80%99s%20position,returns%20-1%20when%20the%20character%20is%20not%20found.
# Enumarate Function


# Colab

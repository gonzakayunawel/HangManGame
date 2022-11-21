import os, random

def run():
    word='PERRO'
    lines = '_ '*len(word)
    def present():
        os.system("clear")
        print('Welcome to the HangManGame')
        print('\nTry to guess the word!')
        print('\n')
    
    

    def startGame():
        print('\n',lines)
        
    def changeWord(letter):
        new = [i for i,c in enumerate(word) if c == letter]
        
    def gaming():
        c=0
        while c <= 2:
            present()
            startGame()
            letter = input('\nEnter a letter... ')
            if letter.upper() == 'R':
                print('\nYeah! Your letter is in the word')
            else:
                print('\nSorry, try again')
                c+=1
            
            
            # if letter.upper() in word:
            #     print('\nYeah! Your letter is in the word')
            #     print(changeWord(letter.upper()))
            #     if c == 2:
            #         print('\nYou lose!')
            #         break
            # else:
            #     print('\nSorry, try again')
            #     present()
            #     print(changeWord(letter.upper()))
            #     if c == 2:
            #         print('\nYou lose!')
            #         break
        print('Game Over')
    gaming()
    
if __name__ == '__main__':
    run()
    
# https://www.techiedelight.com/find-index-character-python-string/#:~:text=The%20standard%20solution%20to%20find%20a%20character%E2%80%99s%20position,returns%20-1%20when%20the%20character%20is%20not%20found.
# Enumarate Function


# Colab
word='PERRO'
blank= str('_'*len(word))
new_word = list(word)

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
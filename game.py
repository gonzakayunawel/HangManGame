import os, random

def run():
    word='PERRO'
    lines = '_ '*len(word)
    def present():
        os.system("clear")
        print('Welcome to the HangManGame')
        print('\nTry to guess the word!')
    
    present()

    def startGame():
        print('\n',lines)
        
    startGame()
    
    def changeWord(s):
        index = word.find(s)
        new = lines.replace(lines[index], s, 1)
        return new
        
    def gaming():
        c=0
        while c <= 2:
            letter = input('\nEnter a letter...')
            if letter.upper() in word:
                print('\nYeah! Your letter is in the word')
                present()
                print(changeWord(letter.upper()))
                if c == 2:
                    print('\nYou lose!')
                    break
            else:
                print('\nSorry, try again')
                present()
                print(changeWord(letter.upper()))
                if c == 2:
                    print('\nYou lose!')
                    break
            c += 1
    gaming()
    
if __name__ == '__main__':
    run()
    
# https://www.techiedelight.com/find-index-character-python-string/#:~:text=The%20standard%20solution%20to%20find%20a%20character%E2%80%99s%20position,returns%20-1%20when%20the%20character%20is%20not%20found.
# Enumarate Function
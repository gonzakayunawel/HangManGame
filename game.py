import os, random

def run():
  words = ['perro', 'gato', 'conejo', 'caballo', 'vaca', 'cerdo', 'gallina', 
          'gallo', 'pato', 'buey', 'oveja', 'cordero', 'ganso', 'pollo', 'toro', 'yegua','potrillo', 'potro', 'burro']
  def present():
    os.system('clear')
    print('Welcome! to the HangManGame')
    print('You have to guess the word if you want to win.\nOnly have 5 trys to win.\nClue: The words are about farm animals.\nGood luck!')
    print('\n')
    
  present()
  
  def random_word():
    word = random.choice(words)
    return word
  word = random_word()
  
  def game():
    blank = '_'*len(word)
    c = 0
    user_word = ''
    while c < 5:
      user_letter = input('Insert a letter... ')
      print('\n')
      
      if word.count(user_letter.lower()) == 1:
        index = word.rfind(user_letter.lower())
        blank = list(blank)
        blank[index] = word[index]
        blank = blank
        blank = ''.join(blank)
        print('     ',blank)
        print('\n')
        print('Yeah. Your letter is in the word!')
        user_word = ''.join(blank)
        if user_word == word:
          break
      elif word.count(user_letter.lower()) == 2:
        index = word.rfind(user_letter.lower())
        blank = list(blank)
        blank[index] = word[index]
        blank = blank
        index2 = word.index(user_letter.lower())
        blank = list(blank)
        blank[index2] = word[index2]
        blank = blank
        blank = ''.join(blank)
        print('     ',blank)
        print('\n')
        print('Yeah. Your letter is in the word!')
        user_word = ''.join(blank)
        if user_word == word:
          break
      else:
        c += 1
        print('Boring, letter not found.')
  
    if user_word == word:
      print('\n')
      print('You win.')
      print('Congratulations')
    elif c == 5:
      print('\n')
      print('You lose.')
      print('The game is over.')
  
  game()

if __name__ == '__main__':
    run()

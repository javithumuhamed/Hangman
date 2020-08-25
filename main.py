import random
import os
class hangman():
    def greet(self):
        print("HELLO MAY I KNOW YOUR NAME?")
        name=input()
        print("LETS GO! ",name)
        self.start()
    def start(self):
        tries = int(input("How many tries you want ?"))
        with open("wordfile.txt") as  word_file :
            word= word_file.read().splitlines()
            random_word=random.choice(word)
            self.game(random_word,tries)
    def game (self,s,n):
        match='-'*len(s)
        answer=s
        print(match)
        success=0
        for i in range (0,n):
            if (list('@' * len(s)) == s):
                break
            gues=input('enter the guess:')
            if (gues in s ):
                match = list(match)
                match[s.index(gues)] = gues
                s = list(s)
                s[s.index(gues)] = '@'
                print(''.join(match))
                success += 1
            else:
                print("OUCH!!!")

        if(success== len(s)):
            print("YOU WON")
        else:
            print("ALAS!!!! YOU LOSE")
            print("ANSWER:",answer)

if __name__ == '__main__':
    p=hangman()
    p.greet()

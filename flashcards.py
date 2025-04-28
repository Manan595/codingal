class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):

        return self.word+'('+self.meaning+')'
    
flash=[]
print("welcome to flashcard application")


while (True):
    word=input('enter your name you want to add falshcard:')
    meaning = input('enter the meaning of the word')

    flash.append(flashcards(word,meaning))
    option = int(input('enter 0, if your want to add another flashcard othervise enter 1 :'))

    if (option):
        break

print('\nYour flashcards')
for i in flash:
    print (">",i)
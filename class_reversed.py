class class_reversed:

    def __init__(self,word_s):
      self.s=word_s

    def rervesed_word(self):
       return self.s[:: -1]
    
word = input('Enter the word to be reversed :')
rev_ob = class_reversed(word)
result = rev_ob.rervesed_word()
print('reversed string:',result)
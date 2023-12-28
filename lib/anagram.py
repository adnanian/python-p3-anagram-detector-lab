# your code goes here!
class Anagram:
    pass
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        pass
        anagrams = []
        for word in word_list:
            if sorted(self.word.lower()) == sorted(word.lower()):
                anagrams.append(word)
        return anagrams
# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def is_anagram(self, word1, word2):
        # Your anagram detection logic here
        return sorted(word1) == sorted(word2)

    def match(self, word_list):
        matching_words = [word for word in word_list if self.is_anagram(self.word, word)]
        return matching_words
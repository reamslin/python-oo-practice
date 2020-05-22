"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """Class to hold list of words

    Attributes:
    ______________________

    dictionary: file
    words: array of strings 
    word_count: int


    >>> w = WordFinder('small.txt')
    5 words read

    >>> w.random() in w.words
    True

    """
    def __init__(self, dictionary):
        """generates a WordFinder, initializes words by reading the dictionary"""
        self.dictionary = dictionary
        self.words = self.read_dictionary()
        self.word_count = len(self.words)

        print(f"{self.word_count} words read")

    def read_dictionary(self):
        """reads dictionary file, populating words array"""
        dictionary = open(self.dictionary, "r")
        words = []
        for word in dictionary:
            words.append(word.strip(' \n'))
        return words
    
    def random(self):
        """returns random word from words"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """allows for blank lines and comments
    
    >>> w = SpecialWordFinder('special.txt')
    4 words read
    
    """
    def read_dictionary(self):
        dictionary = open(self.dictionary, "r")
        words = []
        for word in dictionary:
            if not (word.strip(' \n') == '' or word.strip(' \n')[0] == '#'):
                words.append(word.strip('\n'))
        return words





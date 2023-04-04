"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self, path):
         """A class used to find random words from a dictionary
         
         Attributes:
         ---------------
         wf = WordFinder("words.txt")
         235886 words read

         wf.random() in words.txt
         'cellarage'

         wf.random() in words.txt
         'azonic'
         """
         
         dict_file = open(path)

         self.words = self.parse(dict_file)

         print (f"{len(self.words)} words read")

    def parse(self, dict_file):
         
         return [w.strip() for w in dict_file]
    
    def random(self):
         return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["parsnips", "mango", "kale", "apple"]
    mango

    >>> swf.random() in ["parsnips", "mango", "kale", "apple"]
    kale

    >>> swf.random() in ["parsnips", "mango", "kale", "apple"]
    parsnips
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
# Creating an iterator that loops over the words of a sentence (disregarding punctuation)

class Sentence:

    def __init__(self, sentence):     # learned: "input" is an aweful name for an attribute, because it's reserved for something else
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]
 
my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

# Credits: Corey Schafer @ https://www.youtube.com/watch?v=C3Z9lJXI6Qw
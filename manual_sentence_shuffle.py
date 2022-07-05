# manualle shuffeling the words of a sentence (whichout using the random.shuffle method)

import random

def manual_shuffle(unshuffled_list):
    shuffledlist = random.sample(unshuffled_list,len(unshuffled_list))
    return shuffledlist
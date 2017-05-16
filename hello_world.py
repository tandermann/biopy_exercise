#!/usr/bin/env python

def hello_world():
    print 'Hello World.'

def shuffle_sentence(sentence):
    word_list = sentence.split(' ')
    import random
    random.shuffle(word_list)
    new_sentence = ' '.join(word_list)
    return new_sentence

#hello_world()
#import os
#os.getcwd()

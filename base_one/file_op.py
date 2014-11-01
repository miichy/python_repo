#!/usr/bin/python

import cPickle as pickle

picklelist = ["one",2,"four","can you count?"]

file = open('file_op.txt','w')

pickle.dump(picklelist,file)

file.close()

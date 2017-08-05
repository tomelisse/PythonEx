from os import listdir
from os.path import isdir
from os.path import isfile

def findpaths(path):
    ''' returns the paths of all files and directories in the given path '''
    # return (path + '/' + item for item in listdir(path))
    for item in listdir(path):
        yield path + '/' + item

def printfiles(path):
    ''' prints all the files in the path '''
    if isfile(path):
        print path

def findfiles(path):
    ''' prints all the files in the tree of the given directory '''
    paths = findpaths(path)
    for path in paths:
        printfiles(path)
        if isdir(path):
            findfiles(path)

def isPy(path):
    ''' checks is the item is a .py file '''
    return path.endswith('.py')

def numPy(path, n=0):
    ''' computes the number of .py files in the directory tree '''
    paths = findpaths(path)
    for path in paths:
        if isfile(path) and isPy(path):
            n += 1
        if isdir(path):
            n += numPy(path, n)
    return n




from os import listdir
from os.path import isfile
import time

def trace(f):
    ''' decorator for tracing function calls '''
    f.indent = 0
    def g(*x):
        print f.indent*'| ' + '|--' ,f.__name__, x
        f.indent += 1
        value = f(*x)
        # print f.indent*'| ' + '|--','return ', value
        return value
    return g

def memoize(f):
    ''' caches the result of f when it's used for the 1st time '''
    ''' and reuses it when it's needed next time '''
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g   

def profile(f):
    ''' prints the time consumed in executing f '''
    ''' ??? '''
    # f.start = 1000
    # f.stop  = 0
    def g(x):
        start = time.time()
        # if start < f.start:
        #     f.start = start
        result = f(x)
        stop = time.time()
        # if stop > f.stop:
        #     f.stop = stop
        print stop - start
        return result
    return g

def vectorize(f):
    ''' returns a function which takes a list of args, '''
    ''' calls f for every element and returns the result as a list '''
    def g(l):
        result = []
        for x in l:
            result.append(f(x))
        return result
    return g


def product(a,b):
    ''' multiplies 2 numbers recursively, using only + and - '''
    if b == 0:
        return 0
    else:
        return a + product(a, b-1)

def flatten_list(l, result = []):
    ''' flattens a nested list '''
    for x in l:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)
    return result

def flatten_dict(d, pre = '', result = dict()):
    ''' flattens a nested dictionary '''
    for k, v in d.items():
        k = pre + k
        if isinstance(v, dict):
            flatten_dict(v, k + '.' , result)
        else:
            result[k] = v
    return result


def unflatten_dict(d):
    ''' unflattens a dictionary flattened by the use of flatten_dict function '''
    result = dict()
    for k, v in d.items():
        dot = k.find('.')
        if dot != -1:
            new_k = k[:dot]
            sub_k = k[dot+1:]
            if new_k not in result:
                result[new_k] = {sub_k : v}
            else:
                result[new_k][sub_k] = v
        else:
            result[k] = v
    for k, v in result.items():
        if isinstance(v, dict):
            if True in ['.' in sub_k for sub_k in v.keys()]:
                result[k] = unflatten_dict(v)
    return result

def tree_reverse(l):
    ''' reverses a nested list '''
    result = list(reversed(l))
    for i, x in enumerate(result):
        if isinstance(x, list):
            result[i] = tree_reverse(x)
    return result

def tree_map(function, l):
    ''' map a function over a nested list '''
    result = []
    for x in l:
        if isinstance(x, list):
            result.append(tree_map(function, x))
        else:
            result.append(function(x))
    return result

def path_name(path, item):
    ''' returns path of the item '''
    return path + "/" + item

def dirtree(path):
    ''' prints all the files in the given directory tree '''
    if isfile(path):
        print path
    else:
        for item in listdir(path):
            item_path = path_name(path, item)
            dirtree(item_path)

@trace
def count_change(amount, coins):
    ''' computes the number of ways to change the given amount of money '''
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    result = 0
    for i, coin in enumerate(coins):
        result += count_change(amount-coin,coins[i:])
    return result

@memoize
@trace
def permute(l):
    ''' computes all possible permutations of the given list '''
    results = []
    if len(l) == 1:
        return l[0]
    for i, x in enumerate(l):
        sub_l = permute(l[:i]+l[i+1:])
        if isinstance(sub_l, list):
            for y in sub_l:
                results.append([x]+y)
        else:
            results.append([x, sub_l])
    return results

@profile
@memoize
@trace
def fib(n):
    ''' returns nth Fibonacci number '''
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@ vectorize
def square(x): return x*x

@profile
def time_test(x):
    time.sleep(x)
    return x

def readlines(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def printlines(lines):
    for line in lines:
        print line,

def unixcommand(command):
    def g(filenames):
        lines = readlines(filenames)
        printlines(out for line in lines for out in command(line))
    return g

@unixcommand
def cat(line):
    yield line

@unixcommand
def cap(line):
    yield line.capitalize()
            

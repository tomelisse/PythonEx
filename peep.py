from itertools import chain
from itertools import izip

def peep(iterator):
    first = iterator.next()
    iterator = chain(iter([first]), iterator)
    print first, list(iterator)

def my_izip(*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    while(1):
        t = []
        for iterator in iterators:
            t.append(iterator.next())
        yield tuple(t)
    
    

def my_enumerate(iterable):
    indices = range(len(iterable))
    for i, x in izip(indices, iterable):
        yield (i,x)

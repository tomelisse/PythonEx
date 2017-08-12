from itertools import chain
from itertools import izip

def peep(iterator):
    ''' returns the first element return by a generator '''
    ''' and the very same generator '''
    first = iterator.next()
    iterator = chain(iter([first]), iterator)
    print first, list(iterator)

def my_izip(*iterables):
    ''' my version of itertools.izip '''
    iterators = [iter(iterable) for iterable in iterables]
    while(1):
        t = []
        for iterator in iterators:
            t.append(iterator.next())
        yield tuple(t)

def my_enumerate(iterable):
    ''' my version of enumerate '''
    indices = range(len(iterable))
    for i, x in izip(indices, iterable):
        yield (i,x)

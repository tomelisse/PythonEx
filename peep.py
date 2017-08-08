from itertools import chain

def peep(iterator):
    first = iterator.next()
    iterator = chain(iter([first]), iterator)
    print first, list(iterator)

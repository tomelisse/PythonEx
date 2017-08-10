''' solutions of the problem defined in: '''
''' https://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python?answertab=votes#tab-top '''
from operator import itemgetter
from itertools import groupby

def logger(f):
    ''' displays info about the called function '''
    def g(*x):
        print 'display the sublists with {} in field number {}'.format(x[2],x[1])
        return f(*x)
    return g

@logger
def grouping(l, field_number, field_value):
    ''' displays only the sublists with field_value '''
    ''' in field with number field_numer '''
    l_sorted  = sorted(l, key = itemgetter(field_number))
    for k, g in groupby(l_sorted, key = itemgetter(field_number)):
        if k == field_value:
            return list(g)

from itertools import groupby

def nth_largest_element(l, n):
    ''' finds the second largest element '''
    l_s = sorted(l, reverse = True)
    return list(groupby(l_s))[n-1][0]

def nth_largest_index():
    ''' finds the index of the nth largest element of a list '''
    n = int(input())
    l = list(map(int, input().split()))
    m = nth_largest_element(l, n)
    return l.index(m)

if __name__ == '__main__':
    print(nth_largest_index())

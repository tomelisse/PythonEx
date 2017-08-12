from itertools import count

def integers():
        """Infinite sequence of integers."""
        i = 1
        while True:
            yield i
            i = i + 1

def pyth_triplets(n):
    ''' generates n pythogorial triplets '''
    # gen = ((x,y,z) for z in integers() 
    #                for y in xrange(1,z) 
    #                for x in xrange(1,y)
    #                if x*x + y*y == z*z)
    gen = ((x,y,z) for z in count(1) 
                   for y in xrange(1,z) 
                   for x in xrange(1,y)
                   if x*x + y*y == z*z)
    triplets = []
    for i in range(n):
        triplets.append(gen.next())
    return triplets


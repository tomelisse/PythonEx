class reverse_iter:
    ''' takes a list and iterates it from the reverse direction '''
    def __init__(self, n):
        self.i = n

    def __iter_(self):
        return self

    def next(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()

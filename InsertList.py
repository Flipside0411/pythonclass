class intSet(object):
    ''' An intSet is a set of ntegers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly onece.
    '''
    def __init__(self):
        '''
        :return: Create an empy set of integers
        '''
        self.vals = []

    def insert(self, e):
        '''Assumes E is an integer and inserts e into self'''
        if not e in self.vals:
            self.vals.append(e)
    def member(self,e):
        '''Assumes e is an integer
        Raises ValueError if e is not in self'''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')

    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        return  '{' + ','.join([str(e) for e in self.vals]) + '}'

    def elem(self):
        '''Returns the numbers of elements in list'''
        return 'Liength of elements is ' + self.vals.__len__()


s = intSet()


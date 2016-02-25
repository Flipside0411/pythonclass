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
        return 'Length of elements is ' + len(self.vals())

    def intersect(self,other):
        ''' Define and intersect method that returns a new intSet
        containing elements that appear in both sets.
        '''
        if self.vals() is [] or other.vals() is []:
            return []
        res = []
        if self.vals <= other.vals:
            for e in self.vals:
                if e in other.vals:
                    res.append(e)
        else:
            for e in other.vals:
                if e in self.vals:
                    res.append(e)
        return '{' + ','.join([str(e) for e in res]) + '}'

s = intSet()


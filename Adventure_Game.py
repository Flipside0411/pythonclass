import cmd

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)


    def do_quit(self, args):
        '''Leaves the game'''
        print 'Thank you for playing'
        return True


if __name__ == '__main__':
    g = Game()
    g.cmdloop()

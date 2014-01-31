from itertools import product
from optparse import OptionParser
import sys
import os

class Wordlist:
    def __init__( self, charset, min, max ):
        self.charset = list(set(charset))
        self.min = min
        self.max = max
        self.data = []

    def generate( self ):
        for cur in range(self.min, self.max + 1):
            for word in product( self.charset, repeat=cur ):
                self.data.extend( [''.join(list(word))] )

    def get( self, filedesc ):
        for word in self.data:
            print >> filedesc , word
        if file != sys.stdin:
            file.seek(0, os.SEEK_END)
            print( '\n' + __file__ + ' List size: ' +
                   str(file.tell()) + ' bytes' )

def main():
    parser = OptionParser()
    parser.add_option('-m', '--min', help='minimum word size')
    parser.add_option('-M', '--max', help='Maximum word size')
    parser.add_option('-o', '--out',
                      help='Saves output to specified file')

    opts, args = parser.parse_args()

    if not len(args):
        print('\n'+__file__+': charset required')
        exit(-1)

    min = 1 if opts.__dict__['min'] is None else opts.__dict__['min']
    max = len(args[0]) if opts.__dict__['max'] is None else opts.__dict__['max']
    filedesc = sys.stdout if opts.__dict__['out'] else open(opts.__dict__['out'], 'w')

    wl = Wordlist( args[0], int(min), int(max) )
    wl.generate()
    wl.get( filedesc )

if __name__ == '__main__':
    main()

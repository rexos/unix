from itertools import product
from optparse import OptionParser
import sys

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
    
    def get( self, filename ):
        for word in self.data:
            print >> filename , word

def main():
    parser = OptionParser()
    parser.add_option('-m', '--min', help='minimum word size')
    parser.add_option('-M', '--max', help='Maximum word size')
    parser.add_option('-o', '--out', help='Saves output to specified file')
    
    opts, args = parser.parse_args()

    min = 1 if opts.__dict__['min'] is None else opts.__dict__['min']
    max = len(args[0]) if opts.__dict__['max'] is None else opts.__dict__['max']
    filename = sys.stdout if opts.__dict__['out'] is None else open(opts.__dict__['out'], 'w')

    wl = Wordlist( args[0], int(min), int(max) )
    wl.generate()
    wl.get( filename )

if __name__ == '__main__':
    main()

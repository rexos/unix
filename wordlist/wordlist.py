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
        self.size = self.__total()

    def generate( self ):
        counter = 0
        for cur in range(self.min, self.max + 1):
            for word in product( self.charset, repeat=cur ):
                self.data.extend( [''.join(list(word))] )
                counter = counter + 1
                self.__progress( counter )

    def get( self, filedesc ):
        for word in self.data:
            print >> filedesc , word
        if filedesc != sys.stdout:
            filedesc.seek(0, os.SEEK_END)
            print( '\n' + __file__ + ' List size: ' +
                   str(filedesc.tell()) + ' bytes' )

    def __total( self ):
        ary = range( self.min, self.max + 1 )
        length = len( self.charset )
        return sum( map( lambda x: pow(length, x), ary ) )

    def __progress( self, current ):
        val = int((current * 100) / float( self.size ))
        sys.stdout.write('\r')
        sys.stdout.write('Progress: %s%s %d%%' % ('='*(val/5), ' '*(20-(val/5)), val))
        sys.stdout.flush()


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
    filedesc = sys.stdout if opts.__dict__['out'] is None else open(opts.__dict__['out'], 'w')

    wl = Wordlist( args[0], int(min), int(max) )
    wl.generate()
    wl.get( filedesc )
    filedesc.close()

if __name__ == '__main__':
    main()

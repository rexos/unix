from itertools import product
from optparse import OptionParser
import sys
import os

class Wordlist( object ):
    def __init__( self, charset, minlen, maxlen ):
        self.charset = list(set(charset))
        self.min = minlen
        self.max = maxlen
        self.size = self.__total()

    def generate( self, filedesc ):
        counter = 0
        for cur in range(self.min, self.max + 1):
            for word in product( self.charset, repeat=cur ):
                print >> filedesc , ''.join(list(word))
                if filedesc != sys.stdout:
                    counter = counter + 1
                    self.__progress( counter )
                
        if filedesc != sys.stdout:
            filedesc.seek(0, os.SEEK_END)
            print( '\n' + __file__ + ' List size: ' +
                   str(filedesc.tell()) + ' bytes' )

    def __total( self ):
        ary = range( self.min, self.max + 1 )
        length = len( self.charset )
        return sum( [ pow(length, x) for x in ary ] )

    def __progress( self, current ):
        val = int((current * 100) / float( self.size ))
        sys.stdout.write('\r')
        sys.stdout.write('Progress: %s%s %d%%' %
                         ('='*(val/5), ' '*(20-(val/5)), val))
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

    minlen = opts.__dict__['min']
    if minlen is None:
        minlen = 1

    maxlen = opts.__dict__['max']
    if maxlen is None:
        maxlen = len(args[0])


    if opts.__dict__['out'] is None:
        filedesc = sys.stdout
    else:
        filedesc = open(opts.__dict__['out'], 'w')

    wordlist = Wordlist( args[0], int(minlen), int(maxlen) )
    wordlist.generate( filedesc )
    filedesc.close()

if __name__ == '__main__':
    main()

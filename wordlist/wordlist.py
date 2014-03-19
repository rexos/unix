from itertools import product
from optparse import OptionParser
from collections import OrderedDict
import sys
import os

class Wordlist( object ):

    def __init__( self, charset, minlen, maxlen, pattern, filedesc ):
        self.charset = list(set(charset))
        self.min = minlen
        self.max = maxlen
        self.pattern = pattern
        self.perms = {}
        self.filedesc = filedesc
        self.size = self.__total()

    def generate( self ):
        counter = 0
        for cur in range(self.min, self.max + 1):
            for word in product( self.charset, repeat=cur ):
                print >> self.filedesc , ''.join(list(word))
                if self.filedesc != sys.stdout:
                    counter = counter + 1
                    self.__progress( counter )
        if self.filedesc != sys.stdout:
            self.filedesc.seek(0, os.SEEK_END)
            print( '\n' + __file__ + ' List size: ' +
                   str(self.filedesc.tell()) + ' bytes' )
        self.filedesc.close()

    def generate_with_pattern( self, data={}, composed='', prev=0 ):
        if not prev:
            self.__create_perms()
            data = Pattern( self.pattern )
            data = data.scan()
        if data == {}:
            if self.perms.get(len(self.pattern)-prev, None):
                for word in self.perms[len(self.pattern) - prev]:
                    print >> self.filedesc, composed+(''.join(list(word)))
            else:
                print >> self.filedesc, composed
        else:
            num, val = data.popitem(last=False)
            for word in self.perms[num-prev]:
                self.generate_with_pattern( OrderedDict(data), composed +
                                            (''.join(list(word))) + val, num+1 )

    def __create_perms( self ):
        prev = 0
        for ind, val in enumerate(list(self.pattern)):
            if val != '@': 
                if not self.perms.get((ind-prev), None):
                    self.perms[ind-prev] = list(product(self.charset,
                                                        repeat=(ind-prev)))
                prev = ind + 1

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

class Pattern(object):
    def __init__( self, raw ):
        if raw is None:
            raw = ''
        self.string = raw

    def scan( self ):
        res = OrderedDict()
        for ind, val in enumerate(self.string):
            if val != '@':
                res[ind] = val
        return res


def main():
    parser = OptionParser()
    parser.add_option('-m', '--min', help='minimum word size')
    parser.add_option('-M', '--max', help='Maximum word size')
    parser.add_option('-o', '--out',
                      help='Saves output to specified file')
    parser.add_option('-p', help='Pattern to follow')

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

    pattern = opts.__dict__['p']
    wordlist = Wordlist( args[0], int(minlen),
                         int(maxlen), pattern, filedesc )
    if pattern:
        wordlist.generate_with_pattern()
    else:
        wordlist.generate()
        wordlist.filedesc.close()

if __name__ == '__main__':
    main()

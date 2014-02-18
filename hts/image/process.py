from PIL import Image
import numpy as np

im = Image.open('image.png')

morse_dict={
'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--',
'4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
'.':'.-.-.-',',':'--..--','?':'..--..',"'":'.----.','/':'-..-.','(':'-.--.-',
')':'-.--.-',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','-':'-....-',
'_':'..--.-','"':'.-..-.','$':'...-..-','':''
}

morse = dict((v,k) for k,v in morse_dict.iteritems())

mat = np.zeros(shape=(30,100))

for x in range(0,30):
    pix = []
    for y in range(0,100):
        pix.extend([im.getpixel((y,x))])
    mat[x] = pix

ascii_ary = []
offset = 0
for k in range(0,mat.shape[0]):
    for ind,val in enumerate( mat[k] ):
        if int(val) == 1:
            ascii_ary.extend([(ind+100*k) - offset])
            offset = ind + 100*k

encoded = [chr(x) for x in ascii_ary]
encoded = ''.join(encoded)
print(''.join([morse[x] for x in encoded.split(' ')]))

checksum : checksum.c checksum.h checksum_meth.c
	gcc -lssl -lcrypto checksum.c checksum_meth.c -o checksum

clean : 
	rm checksum
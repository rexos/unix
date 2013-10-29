ds : ds_source.c
	gcc -o ds ds_source.c
	cp ds /bin/ds
	rm ./ds
	rm ./ds_source.c

ds_source.c : 
	python -c "print('int main(){system(\"rm *~ *#\");return 0;}')" > ds_source.c
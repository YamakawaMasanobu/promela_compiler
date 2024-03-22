all:
	clean; \
	make debug -C ../; \
    erlc *.erl; \

clean:
	rm *.beam *.dump; \
	ls | grep -v -E 'chan.erl' | grep -v -E 'globalvarmanager.erl' | grep -v -E 'erlutility.erl' | grep -v -E 'philstarter.erl' | grep erl | xargs rm -rf
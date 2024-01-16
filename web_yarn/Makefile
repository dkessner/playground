#
# Makefile
#


build: install
	yarn webpack --mode=development

build_production:
	yarn webpack --mode=production

install:
	corepack enable
	yarn

clean:
	rm dist/main.js*


.PHONY: build install clean


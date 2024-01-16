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

serve:
	cd dist; python3 -m http.server

clean:
	rm dist/*.js*


.PHONY: build install clean


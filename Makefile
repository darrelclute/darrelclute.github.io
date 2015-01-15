PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
DCNETINPUTDIR=$(BASEDIR)/data
GHPINPUTDIR=$(BASEDIR)/ghp
DCNETOUTPUTDIR=$(BASEDIR)/dcnetoutput
GHPOUTPUTDIR=$(BASEDIR)/ghpoutput
DCNETCONFFILE=$(BASEDIR)/conf/dcnetconf.py
GHPCONFFILE=$(BASEDIR)/ghpconf.py
GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make dcnet                       (re)generate the web site          '
	@echo '   make ghp                         (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 ghp '
	@echo '                                                                       '

dcnet:
	$(PELICAN) $(DCNETINPUTDIR) -o $(DCNETOUTPUTDIR) -s $(DCNETCONFFILE) $(PELICANOPTS)

ghp:
	$(PELICAN) $(GHPINPUTDIR) -o $(GHPOUTPUTDIR) -s $(GHPCONFFILE) $(PELICANOPTS)
	ghp-import -n -p -b $(GITHUB_PAGES_BRANCH) $(GHPOUTPUTDIR)
	clean

clean:
	[ ! -d $(DCNETOUTPUTDIR) ] || rm -rf $(DCNETOUTPUTDIR)
	[ ! -d $(GHPOUTPUTDIR) ] || rm -rf $(GHPOUTPUTDIR)
	[ ! -d $(BASEDIR)/conf/cache ] || rm -rf $(BASEDIR)/conf/cache

.PHONY: dcnet dcnet-regen ghp ghp-regen help clean

PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
THEMEDIR=$(HOME)/repos/dcnet-theme
DCNETINPUTDIR=$(BASEDIR)/data
GHPINPUTDIR=$(BASEDIR)/ghp
DCNETOUTPUTDIR=$(BASEDIR)/dcnetoutput
DCNETPRODDIR=$(HOME)/content
GHPOUTPUTDIR=$(BASEDIR)/ghpoutput
DCNETCONFFILE=$(BASEDIR)/conf/dcnetconf.py
GHPCONFFILE=$(BASEDIR)/conf/ghpconf.py
RESUMEDIR=$(BASEDIR)/resume
RESUMEPDF=$(RESUMEDIR)/resume.pdf
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
	@echo '   make prod                        (re)generate the production site   '
	@echo '   make ghp                         (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 ghp '
	@echo '                                                                       '

dcnet:	darrel-resume
	$(PELICAN) $(DCNETINPUTDIR) -o $(DCNETOUTPUTDIR) -s $(DCNETCONFFILE) -t $(THEMEDIR) $(PELICANOPTS)

prod:   darrel-resume
	$(PELICAN) $(DCNETINPUTDIR) -o $(DCNETPRODDIR) -s $(DCNETCONFFILE) -t $(THEMEDIR) $(PELICANOPTS)

ghp:
	$(PELICAN) $(GHPINPUTDIR) -o $(GHPOUTPUTDIR) -s $(GHPCONFFILE) -t $(THEMEDIR) $(PELICANOPTS)
	ghp-import -n -p -b $(GITHUB_PAGES_BRANCH) $(GHPOUTPUTDIR)

darrel-resume:
	cd $(RESUMEDIR) ;\
	pdflatex resume.tex ;\
	pdflatex resume.tex ;\
	pdflatex resume.tex ;\
	mv $(RESUMEPDF) $(DCNETINPUTDIR)/static/

clean:
	[ ! -d $(DCNETOUTPUTDIR) ] || rm -rf $(DCNETOUTPUTDIR)
	[ ! -d $(GHPOUTPUTDIR) ] || rm -rf $(GHPOUTPUTDIR)
	[ ! -d $(BASEDIR)/conf/cache ] || rm -rf $(BASEDIR)/conf/cache
	rm -rf $(BASEDIR)/conf/*.pyc

.PHONY: dcnet prod ghp help clean

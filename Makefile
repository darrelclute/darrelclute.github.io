PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/data
GHPINPUTDIR=$(BASEDIR)/ghp
OUTPUTDIR=$(BASEDIR)/output
GHPOUTPUTDIR=$(BASEDIR)/ghpoutput
CONFNAME?=dcnetconf.py
CONFFILE=$(BASEDIR)/conf/$(CONFNAME)
GHPCONFFILE=$(BASEDIR)/conf/ghpconf.py
RESUMEDIR=$(BASEDIR)/resume
RESUMEPDF=$(RESUMEDIR)/resume.pdf
GITHUB_PAGES_BRANCH=master
PYCURDIR != python -c 'from pathlib import Path; print(Path.cwd())'
PDFLATEX != which pdflatex 2>&1

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make ghp                         (re)generate GitHub Pages          '
	@echo '   make resume                      (re)generate resume PDF from latex '
	@echo '   make clean                       remove the generated files         '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 ghp '
	@echo '                                                                       '

html:
ifeq ($(DEBUG), 1)
	$(info PELICANOPTS is $(PELICANOPTS))
	$(info BASEDIR is $(BASEDIR))
	$(info CONFFILE is $(CONFFILE))
	$(info PYCURDIR is $(PYCURDIR))
	$(info PDFLATEX is $(PDFLATEX))
endif
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -v $(PELICANOPTS)


ghp:
	$(PELICAN) $(GHPINPUTDIR) -o $(GHPOUTPUTDIR) -s $(GHPCONFFILE) -v $(PELICANOPTS)
	ghp-import -l -n -p -b $(GITHUB_PAGES_BRANCH) $(GHPOUTPUTDIR)

resume:
	cd $(RESUMEDIR) ;\
	pdflatex resume.tex ;\
	pdflatex resume.tex ;\
	pdflatex resume.tex ;\
	mv $(RESUMEPDF) $(INPUTDIR)/static/

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	[ ! -d $(GHPOUTPUTDIR) ] || rm -rf $(GHPOUTPUTDIR)
	[ ! -d $(BASEDIR)/conf/cache ] || rm -rf $(BASEDIR)/conf/cache
	rm -rf $(BASEDIR)/conf/*.pyc

.PHONY: dcnet prod ghp help clean

:title: Introduction to Git Basics
:author: Darrel Clute
:description: Introduction to the basics of version control with Git.
:data-transition-duration: 2000
:skip-help: true

----

What will we cover?
===================

* Introduction to version control

* Introduction to Git

* Introduction to GitHub

* Migrating to Git from another system

----

Introduction to version control
===============================

A brief history
---------------

* The beginning - single file control, localized, file based locks

  + 1972 - Source Code Control System (SCCS) developed at Bell Labs

  + 1982 - Revision Control System (RCS) developed at Purdue University

* The interim - multi-file control, Client-Server, merge before commit

  + 1986 - Concurrent Versions System (CVS)

    - Scripts around RCS

    - Non-atomic operation

  + 2000 - Apache Subversion (SVN)

    - Atomic operations

    - Restructuring retains history

* The present - tree based control through changesets, distributed, commit
  before merge

  + 1998 - BitKeeper

    - Used by Linux Kernel until 2005 when BitKeeper decided to restrict
      license

  + 2005 - Git, Mercurial, Bazaar

    - Response to BitKeeper License change

----

Introduction to version control
===============================

Central v Distributed
---------------------

* Complete copy of repository history local

* Each individuals repository is a backup

* Allows for work to be completed offline

* Allows for non-linear workflows

* Permits use of a central repository, but does not enforce

----

Introduction to Git
===================

Configuration Files
-------------------

* System policies in /etc/gitconfig

* User global polices in ~/.gitconfig or ~/.config/git/config

* Repository policies in $repo/.git/config

----

Introduction to Git
===================

Basic Environment Setup
-----------------------

Minimum global configuration to be able to work with Git:

.. code:: bash

   git config --global user.name "Git User"
   git config --global user.email git.user@example.com

Change the user email for a local repository:

.. code:: bash

   git config user.email git.user1@example.net

----

Introduction to Git
===================

Example of a complete user configuration:

.. code::

    [user]
	    name = Git User
	    email = git.user@example.com
    [core]
    	    editor = vim
	    pager = less
    [color]
	    ui = 1
    [push]
	    default = current
    [alias]
	    co = checkout
	    pu = !"git fetch origin -v ; git fetch upstream -v ; git merge upstream/master"
	    cm = commit
	    tags = tag -l
	    branches = branch -avv
	    remotes = remote -v
    [help]
	    autocorrect = 1

----

Introduction to Git
===================

Repository Basics
-----------------

Git operates on a tree

.. code:: bash

   repo-example $ ls
   .git  README  lib

Directory is the repository, containing the current working branch and the
Git directory (.git)

----

Introduction to Git
===================

Basic Workflows - Creating a Repository
---------------------------------------

.. code:: bash

   $ mkdir repo ; cd repo
   $ git init
   $ vi README
   $ mkdir lib
   $ vi lib/example.c
   $ git add .
   $ git commit

----

Introduction to Git
===================

Basic Workflows - Cloning a Repository
--------------------------------------

.. code:: bash

   $ git clone https://github.com/exampleuser/example-repo.git

----

Introduction to Git
===================

Basic Workflows - Branching
---------------------------

.. code:: bash

   $ git branch example
   $ git checkout example

Shorthand, create and change:

.. code:: bash

   $ git checkout -b example

----

Introduction to Git
===================

Basic Workflows - Merging
-------------------------

.. code:: bash

   $ git merge example master

----

Introduction to Git
===================

Basic Workflows - Stashing
--------------------------

Stash your temporary work before performing another Git operation.

.. code:: bash

   $ git stash

Recover your stashed work.

.. code:: bash

   $ git stash pop

----

Introduction to GitHub
======================

What is GitHub?
---------------

* Hosted Git repositories similar to SourceForge

* Collaboration for Projects

* Public at https://github.com/

* Available in an onsite private product as well, GitHub Enterprise

* Provides issue tracking, wiki, project statistics

* Lightweight peer/code review through Pull Requests

* Forking of repositories to increase collaboration without granting write access

----

Introduction to GitHub
======================

GitHub Workflow
---------------

#. Fork repository

#. Clone your fork: ``git clone https://github.com/youruser/repo.git``

#. Add upstream as remote: ``git remote add upstream
   https://github.com/otheruser/repo.git``

#. Make a meaningful branch for your work: ``git checkout -b feature``

#. Make local edits and commits

#. Push changes to your repository: ``git push``

#. Submit pull request

----

Introduction to GitHub
======================

GitHub Workflow - Demo
----------------------

----

Migrating to Git
================

* Use Git to interact with another type of repository through bridges

  + git cvs* ...

  + git svn ...

  + git bzr ...

  + git hg ...

* Import repository from another system

----

Migrating to Git
================

Convert from SVN
----------------

#. Create an authors map

#. Clone the repository: ``git svn clone https://example.com/svn/repository -A
   auhtors.txt``

#. Create the remote repository

#. Add a remote: ``git remote add origin git@github.com:youruser/newrepo.git``

#. Push the changes: ``git push``

----

Migrating to Git
================

Convert from SVN - Demo
-----------------------

----

Further Reading
===============

`Pro Git`_

`Git Internals`_

`Hackers Guide to Git`_

`Git in the Trenches`_

`Git Magic`_

`Git Pocket Guide`_

`Git Workflows`_

`Git Succinctly`_

`Learn Version Control with Git`_

`Version Control by Example`_

`Git for Subversion Users`_

----

Please attribute Darrel Clute with a link to https://www.darrelclute.net.

.. image:: https://licensebuttons.net/l/by-sa/4.0/88x31.png
   :alt: Creative Commons Attribution-ShareAlike 4.0
   :align: center

Except where otherwise noted, this work is licensed under

http://creativecommons.org/licenses/by-sa/4.0/


.. _Pro Git: http://git-scm.com/book/en/v2

.. _Git Internals:
    https://github.com/pluralsight/git-internals-pdf/raw/master/drafts/peepcode-git.pdf

.. _Hackers Guide to Git: https://wildlyinaccurate.com/a-hackers-guide-to-git

.. _Git in the Trenches: http://cbx33.github.io/gitt/download.html

.. _Git Magic: http://www-cs-students.stanford.edu/~blynn/gitmagic/

.. _Git Pocket Guide:
    http://chimera.labs.oreilly.com/books/1230000000561/index.html

.. _Git Workflows: http://documentup.com/skwp/git-workflows-book

.. _Git Succinctly: http://www.syncfusion.com/resources/techportal/ebooks/git

.. _Learn Version Control with Git:
   http://www.git-tower.com/learn/ebook/command-line/introduction

.. _Version Control by Example: http://ericsink.com/vcbe/

.. _Git for Subversion Users: http://git.or.cz/course/svn.html

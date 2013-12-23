Server Reloaded
###############
:date: 2008-09-16
:slug: server-reloaded

If you noticed for a little over a week this site was offline. The
reason being that my colo would not boot into the kernel any longer,
even after much troubleshooting. This colo has been running `Gentoo`_
and `Xen`_ since it was put online. Now I know what the technically
inclined out there are going to say, `Gentoo`_ is not a server OS, and
I'd agree. So why was I running `Gentoo`_ on a server then?

Over the past several years I've used a number of different
distributions of `Linux`_. I started out with `Mandrake (now
Mandriva)`_, and have worked with `Red Hat`_, `Debian`_, `SuSe`_, `Linux
from Scratch`_, `Gentoo`_ and `CentOS`_. I've also used a number of
commercial `UNIX`_ operating systems and `BSD`_ variants. My varied
experiences, especially with binary distributions, have generally left
me wanting or requiring me to build the software I want to utilize
myself to get the functionality I was looking for. I had used the `BSD`_
variants prior to trying `Gentoo`_ and liked the ports system and its
flexibility. What really attracted me to `Gentoo`_ was that it was build
from source like `Linux from Scratch`_ and utilized portage, which is
similar to ports from the `BSD`_ variants, as a package manager. I've
used `Gentoo`_ on my workstations and server since beginning work at
`Liquid Web`_ and have become very comfortable with it.

The primary reason that I put `Gentoo`_ on this server initially was to
test out `Xen`_ to see if it was something that I would want to utilize
moving forward. At the time `Xen`_ was still a fledgling technology and
the best tutorials were for `Gentoo`_ therefore that was the OS I chose
to get things online as well as test. Recently I began running into
issues with the server install and began looking at reloading the OS on
the server. I had been working on replacing the child instance with
`Debian`_ because over the past couple of years they've gotten better
and keeping up with more recent releases of software and their compile
options were nearly the same as those that I was looking for but not in
most other distributions. `Gentoo`_ served its purpose and allowed me to
test out `Xen`_ and become familiar with it. I decided to reload the
server using `Debian`_ with `Xen`_. The install was fairly quick, after
getting the data backed up, and I had the server up and running in
little time.

I reallocated space compared to how it was initially. Instead of running
`Apache`_ as the web server I'm now utilizing `LigHTTPD`_ as the web
server. The memory foot print is lower and it is faster. In the
reallocation I made sure that I designed things a little better, `PHP`_
is now run as a `FastCGI`_ process on an instance separate from the web
server. I also have an instance setup specifically for running `Django`_
as a `FastCGI`_ as well. Each instance is stripped down minimal installs
with just the software necessary and running as few processes as
possible.

Everything is back up and running at the moment and hopefully will be
more stable. Now that I've gotten things squared away with this server
itself and version 1.0 is released I can start working on my `Django`_
application to replace `Drupal`_.

.. _Gentoo: http://www.gentoo.org/
.. _Xen: http://www.xen.org/
.. _Linux: http://www.kernel.org/
.. _Mandrake (now Mandriva): http://www.mandriva.com/
.. _Red Hat: http://www.redhat.com/
.. _Debian: http://www.debian.org/
.. _SuSe: http://www.suse.com/
.. _Linux from Scratch: http://www.linuxfromscratch.org/
.. _CentOS: http://www.centos.org/
.. _UNIX: http://www.unix.org/
.. _BSD: http://www.bsd.org/
.. _Liquid Web: http://www.liquidweb.com/
.. _Apache: http://www.apache.org/
.. _LigHTTPD: http://www.lighttpd.net/
.. _PHP: http://www.php.net/
.. _FastCGI: http://www.fastcgi.com/
.. _Django: http://www.djangoproject.com/
.. _Drupal: http://www.drupal.org/

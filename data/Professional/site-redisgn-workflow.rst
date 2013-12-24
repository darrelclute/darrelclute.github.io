Site Redesign and Workflow
##########################

:date: 2013-12-24 00:00
:slug: site-redesign-workflow

In my previous post I stated that I would be leaving the Blogger_ platform to 
better work into my flow.  As part of that I have additionally redesigned my 
site so that things are hopefully easier on readers.  Here is the workflow that
I have developed that will work best for me, but first some notes on the 
redesign.

Making Changes
==============

I personally was not liking the look of my site.  Additionally I was not seeing
any use case where having Google Ads on my site was of any benefit to me or my
readers.  So since I was going to be changing my workflow and migrating away
from Blogger_, I decided to take some time and rebuild the site layout.

As I had decided that I would use a static site generator, specifically
Pelican_ and more on that below, I started reviewing the available public
domain themes.  I ended up selecting svbhack_ as the base, took some design
queues from `Text and Hubris`_ in the use of the `Font Awesome`_ icons, and
made my own customizations, which you can view in my dcnet-theme-svbhack_
repository.

Over the past four years or so my blog has been hosted at blog.darrelclute.net.
The reason for this was as I was moving to Blogger_ after leaving an employer,
at the time Blogger_ did not have the ability to utilize a naked domain as
Google refers to it.  Now that I am no longer utilizing Blogger_ I decided to
make a change and migrate both my blog and my main site to the same site.
Hopefully anyone subscribed through an RSS reader will receive the appropriate
update to their configurations.  I have setup the former blog to redirect with
a 301 to the appropriate location on the combined site.

I've also made some changes to how feeds are generated.  Instead of separating
out personal posts to a separate site I am going to leave them as a single
site.  Although I don't expect to post many personal posts I am thinking of my
potential readers.  In addition to having a feed for all posts, I also have
separate feeds for each category.  I will also be migrating away from
FeedBurner_.  I am having FeedBurner_ redirect subscribers to the all posts
feed, so if you do not wish to get all of my posts please update your RSS
reader appropriately.

That is about it for the changes to the site, let's delve into how I plan to
become more effective in authoring content, by looking at the planned workflow.

Authoring
=========

After reading `Greg Ferro's book on blogging`_ it became clear to me that I
needed to rethink my workflow.  Part of my problem with authoring over the past
few years can in part be directly contributed to the blogging platform I had
chosen.  The biggest problem with this for me was that there was not a good
method to interact with the platform from the command line.  Now you are
probably thinking to yourself:  

    Whoa, did he just say command line?  

Yes, as I have extensively and nearly exclusively utilized Linux on the desktop
for well over 12 years now, I can accomplish things much faster from the
command line. In fact the majority of my writing is completed in Vim_ utilizing
either LaTeX_ or reStructuredText_.  And I maintain my resume in LaTeX_.
Through reading Greg's examples of using Markdown_, I easily saw how I could
correlate that to utilizing reStructuredText_ which would be a better fit for
me.

My last post I partially wrote out in reStructuredText_ before publishing just
to ensure that I could start building my new workflow.  I knew that I wanted to
have my posts and such stored in Git_ as I have gotten quite used to it being
part of many of my other workflows.  With also being a Python_ user for my
programming I completed a few quick Google searches and found Pelican_.  

Pelican_ is a static site generator written in Python_.  It will take a source
file in reStructuredText_ or Markdown_ and generate a static site that you can
literally host anywhere.  It also utilizes Jinja2_ for the templating language,
which I've been utilizing frequently with Salt_.  So with some background you
are probably wondering what my actual workflow is.

Quite simply I have a directory on any number of computers that I can simply
pull the latest repository contents to and go.  I have a basic structure of how
the content is laid out so that I can keep track of items as well, which I have
outlined here::

    repository|
              |_____drafts
              |_____pages
              |_____<categories>

In this layout I start all writing in the drafts folder, I keep a file there
for quick notes and each draft is separated out by slug as I start writing it.
As I am also utilizing Git_ I also ensure that I commit any changes upon saving
a file.  The pages directory contains all static pages for the site, also in
reStructuredText_.  The <categories> folder is actually more of a variable, I
have a corresponding folder for each category.  As I promote a post from draft
to published, I simply relocate it from the drafts folder to the appropriate
category.

So with the authoring of articles no longer requiring me to utilize a platform
I can better focus on the task at hand.  I no longer need to have my browser
open to be able to be working on articles.  This also has the advantage that I
can work completely offline, which can be extremely beneficial when working
without Internet access.  Now that I have some generated content I just need to
publish.

Publishing
==========

Utilizing a static site generator like Pelican_ opens up where you can host
your site to being nearly infinite.  One of the things that I wanted to
accomplish with the publishing workflow was that I would not have to generate
the site pages locally and push them to the server.  With utilizing Git_ this
is fairly easy because I can have a post-update hook deploy on the server.  But
where to host?  Well being a proponent of PaaS solutions and already leveraging
`Google AppEngine`_ I decided I'd look down that route.

I could have simply deployed it to `Google AppEngine`_ as they have Git_
support now, but there has been something I have been recommending lately that
I thought would be better to deploy to.  I decided that I'd utilize `Red
Hat's`_ `OpenShift Online`_ service as I have been extolling its enterprise
version for Private PaaS deployments.  Going through to build out the initial
deployment was far easier then building out on `Google AppEngine`_.  `OpenShift
Online`_ utilizes Git_ as the base means of deploying the application.  This
means that as soon as I push the repository back up it will build out the site,
or at least the new pages.

You are likely thinking that if I'm auto deploying that my drafts would be
published every time I push the repository.  Thankfully Pelican_ has a
configuration option where I can exclude directories from generation.  This is
quite beneficial for being able to maintain a single repository.  

Since I am using `OpenShift Online`_ it is fair to clarify that the directory
layout above is actually a subset of the actual Git_ repository.  A minor
detail but worth having clarified.

Why Static?
===========

So with a static site, many people think that I'd loose the ability to have
dynamic content on my site, such as comments.  As many of you know services
such as Disqus_ provide a means to host comments for you, it simply gets loaded
through your call of some JavaScript code they provide.  It wouldn't be too
much of a stretch for most other dynamic content you may want on your site to
be provided in this manner.

A static site is easier to maintain as you don't have to worry about your
platform changing on upgrades.  Using a hosted service like Blogger_ or
upgrading your own install base of your favorite platform can unexpectedly
change how your site behaves, or a lack of doing so causes your site to become
defaced.  Additionally a static site will scale far better then a dynamically
generated site.  If you need something dynamic, utilize a service or have a
specialized application that provides that functionality through JavaScript.
It is far easier to scale out a subset of functionality that is dynamic as
opposed to making the entire site dynamic.

My site only has a single author, but that doesn't mean that this setup would
not work for a site with more then one.  Git_ is a version control system,
designed to be distributed.  By utilizing Git_ you can either provide everyone
necessary with write access to the repository, or you can have them submit pull
requests to the editors.  People tend to be a bit put off by version control
systems before or just as they are starting to utilize them.  But don't let
that hold you back from trying it out, it helps with tracking changes and
differences, and correcting mistakes when they arise.

Closing Thoughts
================

Change is a good thing at times.  I decided that as part of changing my
workflow for article creation I would also refresh my site.  I have already
noticed an increase in productivity with the new workflow, and now that the
site is published in its new format things should hopefully be simplified.  In
an industry that is constantly changing it is good for you to induce changes
upon yourself at times instead of having them forced upon you by external
factors.  Take some time and think about the last time that you made a change
for your sake, it may be time to make changes for yourself.


.. _Blogger:  http://www.blogger.com

.. _dcnet-theme-svbhack: https://github.com/darrelclute/dcnet-theme-svbhack

.. _Pelican: http://docs.getpelican.com/en/3.3.0/

.. _svbhack: https://github.com/giulivo/pelican-svbhack

.. _Font Awesome: http://fontawesome.io/

.. _Text and Hubris: http://www.textandhubris.com/

.. _Greg Ferro's book on blogging: https://leanpub.com/Technical-Blogging-Writing-Arse-First

.. _FeedBurner: http://feedburner.google.com

.. _LaTeX: http://www.latex-project.org/

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

.. _Python: http://www.python.org

.. _Git: http://git-scm.com/

.. _Markdown: http://daringfireball.net/projects/markdown/

.. _Jinja2: http://jinja.pocoo.org/

.. _Salt: http://saltstack.com

.. _Google AppEngine: http://appengine.google.com

.. _Red Hat's: http://www.redhat.com/

.. _OpenShift Online: http://openshift.com/

.. _Disqus: http://disqus.com

.. _Vim: http://www.vim.org/

"DevOps Engineer"?
##################

:slug: devops-engineer
:date: 2014-06-20 21:00

Recently talking with someone about their hiring woes and they mentioned that
they were having an extremely hard time finding a "DevOps Engineer".  This
struck a chord with me as I don't typically consider this to be a job title,
and I know from several conversations on Twitter that I am not alone in that
assumption.  In fact this is something that I have given a great deal of
thought to and am finally given it enough thought to codify it here.  Why the
conflicted understandings between the two of us?


===============
What is DevOps?
===============

DevOps is intentionally a very vague and ambiguous term, by design of those
that coined the phrase.  Too often people confuse DevOps with lower level parts
of the overall movement such as Infrastructure as Code or Agile Operations.
Although these parts tend to be vital to an organization succeeding with being
a DevOps organization, it itself is not DevOps.  As you can see with just
trying to clear up some of the easy to distinguish aspects that it still
doesn't necessarily clear up any of the confusion.

The main reason that DevOps visionaries such as Gene Kim and Jez Humble try to
leave the definition of DevOps as ambiguous as possible was to allow
organizations to better adapt it to themselves.  As time has progressed there
has been some clarity on the relation of these tightly knit sub-movements into
a singular movement.  DevOps itself is usually best described as the cultural
components of the overall movement, but not divorced from the other aspects.
Being cultural means that it has influence over how the organization operates
and integrates IT as opposed to it being a separate business unit or cost
center.

The other two components that I mentioned, Infrastructure as Code and Agile
Operations, outline the processes and methods of enabling more efficient IT,
and by extension the types of tools in a general sense.  These two components
can be implemented by an operations organization in a traditional enterprise
and they would still gain benefit, but this is rare to find outside of
organizations moving towards DevOps enablement.


======================
Why not a DevOps Role?
======================

I stated in the opening that effectively I don't see DevOps belonging in a job
title.  As DevOps is encompassing across roles it is no less ambiguous to state
that you are a DevOps Engineer as opposed to an IT Engineer.  With either of
those titles you would have no way of determining if the individual you are
speaking with has their specialty in development, testing, or operations, or
where your job will be focused if you are looking for a job.

I know what you are thinking:  "Right, but isn't that the point of DevOps,
eliminate silos?"  Well, yes and no.  Depending on how an organization embraces
DevOps, and this doesn't necessarily depend on size, the silos may be gone or
present.  In my personal opinion having division of workforce is necessary for
management purposes, and as such makes sense to make those divisions with
functional groups.  This is where culture comes into play.  Without the open
nature of the DevOps culture communication breakdowns will be a detriment
regardless of whether you have silos or not, more so if you do.  What does not
make sense to me, at least until you get to massive scale, is having divisions
beyond the 3 overarching disciplines; Development, QA, Operations.

"OK, so if there are still silos, what have you achieved?"  Well, for an
organization embracing DevOps, just because there are still departments or
divisions inside of IT doesn't mean that there are silos.  Departments exist
for management hierarchy, but should not exist for each department to work
toward different goals than that of the organization.  When each department
works independently of the others, that is how a silo is formed.  When you have
departments, but individuals across those departments function as a single
team, you don't have silos in the traditional sense.

Taking that further, say that an organization has decided that all of IT will
be a single department, without traditional sub-groupings, do all of the
engineers do exactly the same job and have exactly the same title?  Well, of
course you could do this, but it doesn't necessarily make the most sense.  You
will still have subject matter experts even after you start down the path to
enabling DevOps, so why obfuscate out that distinction?  

Even if you feel the need to give everyone a common title, make sure that you
also give them a subtitle that denotes what their primary subject matter is, it
makes it easier to know where to send people when they are having a particular
problem.  Here is one that I am going to leave up to you the reader, if you
give everyone the same primary title, with differing subtitles, how do you
handle those truly unique and hard to find engineers that can rightfully be
called subject matter experts in more than one discipline?  Likewise how have
you addressed this in traditional IT departments?


========
Clarity?
========

The prior two sections definitely help provide clarity around some of the
confusion that I see come up with regard to DevOps.  And it definitely will
help frame deeper conversations that I have with others regarding my
opinion on DevOps as a term in a job title.  But does that help provide clarity
to the situation I opened with?

Back to the individual I was speaking with, what struck me as even more
peculiar came when I probed more about what they were looking for.  They were
looking for an operationally focused position, but not a traditional operations
engineer.  They are looking for an individual that is a developer first, with
operational experience managing infrastructure.  I knew that this sounded
familiar to something that I had heard of before, but couldn't place it at the
time.  I also knew that it sounded like something that I had heard or read
about in relation to DevOps, but not directly.

It was when I read `Matt Simmons article`_ on his take aways from the
`SREConf`_ that he recently attended.  Reading his article I realized that the
individual I was speaking with was looking for a non-traditional operations
engineer, specifically a Site Reliability Engineer.  What sets Site Reliability
Engineering apart from traditional infrastructure engineering is in how the
role is typically filled, in addition to typically only being found at
extremely large web properties.  My last statement is not an indication that
you only need this type of operational mindset when you get to a certain scale,
simply that they are more likely to occur at those types of scale.

SRE from a personnel perspective is typically filled with an individual with a
BS or higher in Computer Science, has extensive experience with development as
well as infrastructure operations.  This is not to say that traditional
infrastructure operations staff cannot fill a role in SRE, it is just far less
common.  The reason for the desire for a full development background is that
they will not only operate the environment, but they will also develop the
necessary tooling, monitoring, and scaling infrastructure to support the
application in ways that a pure infrastructure engineer cannot, typically by
writing large scale distributed applications.

SRE goes beyond typical Infrastructure as Code, where you treat the
infrastructure configuration as code, and typically utilize a configuration
management tool to provide a declarative definition of your needs instead of
imperatively defining it.  From my impression of SRE teams, they will do this
as well, but will also build applications which manage the applications, and
which the applications that are being consumed are dependent on the
applications that the SRE team has developed.  It is likely that SRE teams were
the designer and original developers of the early PaaS implementations that so
many today consume.

==========
Conclusion
==========

There is a great deal of ambiguity and confusion around the still emerging
trends around DevOps, SDN, and other related movements and disciplines.  In
many respects the ambiguity is intentional so that organizations can choose the
best path for themselves to be able to embrace the movement, and work toward
having high performing IT teams.  Other times the ambiguity comes from how
early everything is in the life cycle that not everything is well understood,
such as the case with SDN.

Was I able to help out the individual come to a better understanding of what
they are looking for to fulfill their operational position?  As of the time of
this writing I cannot answer that question, as we haven't delved that far down
into the conversation yet.  I felt it was more important to get this out there
to use as a jumping off point, and hopefully help others as well at the same
time.

Want to explore this in more depth with me?  Feel free to get in touch with me
below in the comments, on `Twitter`_, or `Google+`_.  I think that conversations like
these need to be had across the industry, and not just on the server and
application side as has been the majority of focus to date, networking needs to
be there as well.


.. _Matt Simmons article: 
   http://www.standalone-sysadmin.com/blog/2014/06/the-difference-between-site-reliability-engineering-system-administration-and-devops/

.. _SREConf:
   https://www.usenix.org/conference/srecon14/program

.. _Twitter: https://twitter.com/darrelclute

.. _Google+: https://plus.google.com/+DarrelClute

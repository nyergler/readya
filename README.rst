==========
 Read Ya!
==========

*Read Ya!* is a periodic newletter of Young Adult literature, old and
new.

RY is a static site hosted on GitHub Pages using Pelican_.

Writing
=======

#. Clone the repository::

     $ git clone git@github.com:nyergler/readya.git

#. Create a virtualenv::

     $ cd readya
     $ virtualenv .

#. Activate the virtualenv::

     $ source bin/activate

#. Install the dependencies::

     (readya)$ pip install -r requirements.txt

#. Write the content, placing the file in the ``content/letters``
   directory.
#. Commit your work.
#. Publish to GitHub Pages::

     $ make github

Copyright
=========

RY is copyright 2013-2014, Nathan Yergler. All rights reserved.

.. _Pelican: http://getpelican.com/

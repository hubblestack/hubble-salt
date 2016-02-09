Conventions Used In This Book
=============================

The following typographical conventions are used throughout this book:

*Italic*

 - Indicates new terms, URLs, email addresses, filenames, and file extensions.

``Fixed-width``

 - Used for program listings, as well as within paragraphs to refer to program
   elements such as variable or function names, databases, data types,
   environment variables, statements, and keywords.

**Code Snippets**

.. code-block:: python

    #!/usr/bin/env python2

    import salt.client

    try:
        caller = salt.client.Caller()
        ret = caller.function('test.ping')

**Note**

.. note::

    This signifies a tip, suggestion or general note.

**Warning**

.. warning::

    This indicates a caution or warning.

**See Also**

.. seealso::

    This suggests related topics to be referenced for more detailed
    information.

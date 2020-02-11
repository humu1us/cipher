cipher
======

|pypi| |pyversion|

Encryption and decryption tools. Cipher mix AES encryption with base64 encode generating plain text encrypted files.

Usage
+++++

* variables:

.. code:: python

    >>> import cipher
    >>> cipher.encrypt("encryption_password", "something to encrypt!")
    'WDJoMWJYVXhkWE5mWlc1algxOGNSc2hFT1o2ZGRBOGhoWnByQjYzZnZBYlp3N2ZKZmVDTEw2V1ZEMWlhZ0ZyZDVpSnpVZDll'

.. code:: python

    >>> import cipher
    >>> encrypted = cipher.encrypt("encryption_password", "something to encrypt!")
    >>> cipher.decrypt("encryption_password", encrypted)
    'something to encrypt!'

* files:

.. code:: python

    >>> import cipher
    >>> txt = "file content to encrypt!"
    >>> cipher.write("/tmp/file.encrypted", "encryption_password", txt)

.. code:: python

    >>> import cipher
    >>> cipher.read("/tmp/file.encrypted", "encryption_password")
    'file content to encrypt!'

* A ``Credentials`` class can be used to handle secrets stored in ``JSON`` formats:

.. code:: python

    >>> import json
    >>> secrets = {
    ...     "db_dsn": "mysql://user:pass@host:port/dbname",
    ...     "api_token": "some token"
    ... }
    >>> cipher.write("/tmp/secrets", "encryption_password", json.dumps(secrets))
    >>>
    >>> # so, in your app you can do something like this:
    >>> import cipher
    >>> cred = cipher.Credentials("/tmp/secrets", "encryption_password")
    >>> cred.db_dsn
    'mysql://user:pass@host:port/dbname'
    >>> cred.api_token
    'some token'

Generating keys
+++++++++++++++

There are a lot of ways to create keys but a good easy to use way to create non-easy to remember keys is using ``/dev/urandom``, almost on Unix systems. For example:

.. code::

    dd if=/dev/urandom bs=16 count=1 | base64 > /path/to/key_file

The ``count`` parameter is the number of blocks to read and write, while the ``bs`` parameter is the size of each block.


CLI
+++

There is also available a nice command line. Just install ``cipher`` and start using it! ``$ ciphercmd -v`` will let you know it is ready to be used.

Installation
++++++++++++

PyPi:

::

    $ pip install humu1us-cipher

Development version:

::

    $ git clone git@github.com:humu1us/cipher.git
    $ cd cipher
    $ pip install -e .

Contribution
++++++++++++

Contributions are welcome! Feel free to report bugs or open an issue if you feel a new feature is needed. Pull requests are welcome!


.. |pypi| image:: https://img.shields.io/pypi/v/humu1us-cipher.svg?style=flat-square
   :target: https://pypi.python.org/pypi/humu1us-cipher/
.. |pyversion| image:: https://img.shields.io/pypi/pyversions/humu1us-cipher.svg?style=flat-square
   :target: https://pypi.python.org/pypi/humu1us-cipher/

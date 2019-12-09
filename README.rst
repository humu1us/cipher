cipher
======

Encryption and decryption tools.

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

CLI
+++

There is also available a nice command line. Just install ``cipher`` and start using it! ``$ ciphercmd -v`` will let you know it is ready to be used.

Installation
++++++++++++

PyPi:

::

    $ pip install cipher

Development version:

::

    $ git clone git@github.com:humu1us/cipher.git
    $ cd cipher
    $ pip install -e .

Contribution
++++++++++++

Contributions are welcome! Feel free to report bugs or open an issue if you feel a new feature is needed. Pull requests are welcome!

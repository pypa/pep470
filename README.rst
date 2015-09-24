pep470
======

pep470 is a small tool which enables users to easily upload their files to PyPI
during the PEP470 migration phase.


Usage
-----

To use pep470, simply execute the ``pep470`` CLI utility with a list of one or
more project names like:

.. code-block:: console

    $ pep470 foo bar spam
    Downloading |################################| 3/3
    Downloaded all externally hosted files, upload to PyPI using `twine upload --skip-existing dist/*`

Once that has executed, then simply run ``twine upload --skip-existing dist/*``
to upload all of the files it has found to PyPI.


Discussion
----------

If you run into bugs, you can file them in our `issue tracker`_.

You can also join ``#pypa`` or ``#pypa-dev`` on Freenode to ask questions or
get involved.


Code of Conduct
---------------

Everyone interacting in the pep470 project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`issue tracker`: https://github.com/pypa/pep470/issues
.. _PyPA Code of Conduct: https://www.pypa.io/en/latest/code-of-conduct/

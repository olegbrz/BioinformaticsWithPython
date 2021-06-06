Tests
======

In order to check the correct functioning of the suite, unit tests for all functions were developed with Python unittest.

The task requested a report of the test coverage of the code, but this was not available in the "Community" version of the IDE that was used, JetBrains PyCharm.

To run the tests automatically, being inside the project directory, you can execute:

.. code-block:: bash

	python -m unittest discover

If the tests are passed, the output should be the following:

.. code-block:: bash

	.....................
	---------------------------------------------
	Ran 21 tests in 0.004s

	OK

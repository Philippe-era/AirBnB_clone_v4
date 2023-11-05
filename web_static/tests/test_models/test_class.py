#!/usr/bin/python3
"""library for the class city"""
import inspect
import pep8


class TestClassDocumentation():
    """doc implementation in line"""

    def __init__(self, tests, _class):
        """Constructor"""
        self.tests = tests
        self.name = _class

        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def documentation(self):
        """everything needed for it to work"""
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):

                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)

        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)

    def pep8(self, files):
        """implementation of pep 8"""
        python_8 = pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(files)
        self.tests.assertEqual(result_check.total_errors, 0,
                               'Found code style errors (and warnings)."')

if __name__ == '__main__':
    unittest.main()


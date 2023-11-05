#!/usr/bin/python3
"""This command signifies the command itself"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class of the console"""

    def create(self):
        """the instance created based on it all"""
        return HBNBCommand()

    def test_quit(self):
        """ method of the quit
        """
        connection_code = self.create()
        self.assertTrue(connection_code.onecmd("quit"))

    def test_EOF(self):
        """the EQF WILL BE TESTED
        """
        connection_code = self.create()
        self.assertTrue(connection_code.onecmd("EOF"))

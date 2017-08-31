
import unittest
from runtime.objects.session.session import Session
from runtime.exceptions.app.exception import AppException
from runtime.exceptions.arity.exception import ArityException
from runtime.exceptions.keymismatch.exception import KeyMismatchException
from runtime.components.guard.add_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_wrong_arg_types(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.add_user, 'session': 'xyz'}
        guard = self.component
        with self.assertRaises(TypeError):
            guard.do(instr)

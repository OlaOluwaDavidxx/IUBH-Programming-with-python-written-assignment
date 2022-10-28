from unittest import TestCase
import sys


class TestWorkingEnv(TestCase):
    def test_working_env(self):

        system_version = sys.version_info.major
        self.assertEqual(system_version, 3)

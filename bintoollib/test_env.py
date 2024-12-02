# coding = utf-8

import unittest
from bintoollib import Env

class TestEnv(unittest.TestCase):
    def setUp(self):
        self.env = Env()

    def test_define(self):
        self.env.define('test', 'value')
        self.assertEqual(self.env['test'], 'value')

    def test_define_already_defined(self):
        self.env.define('test', 'value')
        with self.assertRaises(KeyError):
            self.env.define('test', 'value')

    def test_undefine(self):
        self.env.define('test', 'value')
        self.env.undefine('test')
        with self.assertRaises(KeyError):
            self.env.undefine('test')

    def test_undefine_not_defined(self):
        with self.assertRaises(KeyError):
            self.env.undefine('test')

    def test_exec(self):
        self.env.define('test', 'value')
        result = self.env.exec('$test')
        self.assertEqual(result, 'value')

    def test_exec_not_defined(self):
        with self.assertRaises(KeyError):
            self.env.exec('$test')

    def test_exec_exper(self):
        self.env.define('test', 1)
        result = self.env.exec('$test + 1')
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
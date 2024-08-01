from unittest import TestCase
from hashlib import sha1

from whatever import Whatever


class WhateverTests(TestCase):
    def test_get_attr(self):
        """
        All attributes of whatever should be whatever
        """
        foo = Whatever()
        x = foo.bar
    
    def test_get_attr(self):
        """
        If you set an attribute on whatever then that attribute will be what you set it to
        """
        foo = Whatever()
        foo.bar = 'BAR'
        self.assertEqual(foo.bar, 'BAR')
        foo.bar = 'foobar'
        self.assertEqual(foo.bar, 'foobar')

    def test_get_attr_children_classes(self):
        """
        If you extend whatever it's still whatever
        """
        class Foo(Whatever):
            x = 'X'
        foo = Foo()
        self.assertEqual('X', foo.x)
        self.assertTrue(foo.y)

    def test_equality(self):
        """
        Whatever is equal to pretty much whatever
        """
        foo = Whatever()
        bar = Whatever()
        self.assertEqual(bar, foo)
        self.assertEqual(self, foo)
        self.assertEqual(2, foo)
        self.assertEqual(True, foo)
        self.assertEqual('', foo)
        self.assertEqual(2.5, foo)
        self.assertEqual(bool, foo)


    def test_inequality(self):
        """
        Whatever is also probably not equal to pretty much whatever
        """
        foo = Whatever()
        bar = Whatever()
        self.assertNotEqual(bar, foo)
        self.assertNotEqual(self, foo)
        self.assertNotEqual(2, foo)
        self.assertNotEqual(True, foo)
        self.assertNotEqual('', foo)
        self.assertNotEqual(2.5, foo)
        self.assertNotEqual(bool, foo)


    def test_reference_equality(self):
        """
        If Foo is whatever and Bar is whatever Foo is equal to Bar but Foo is not Bar
        """
        foo = Whatever()
        bar = Whatever()
        self.assertTrue(foo == bar)
        self.assertFalse(foo is bar)


    def test_existance(self):
        """
        Whatever does exist
        """
        foo = Whatever()
        self.assertTrue(foo)

    def test_arithmatic(self):
        """
        You can do whatever type of arithmatic you want on whatever, but it will still be whatever
        """
        foo = Whatever()
        self.assertTrue(foo + 1 is foo)
        self.assertTrue(foo - 1 is foo)
        self.assertTrue(foo * 2 is foo)
        self.assertTrue(foo / 2 is foo)
        self.assertTrue(foo % 2 is foo)
        self.assertTrue(foo + foo is foo)
        self.assertTrue(foo - foo is foo)
        self.assertTrue(foo * foo is foo)
        self.assertTrue(foo / foo is foo)
        self.assertTrue(foo % foo is foo)

    def test_cast_to_string(self):
        """
        Whatever as a string is "Whatever"
        """
        foo = Whatever()
        self.assertEqual('Whatever', str(foo))
        self.assertTrue(isinstance(str(foo), str))


    def test_boolean_arithmatic(self):
        """
        You can even do whatever you want on the bytes of whatever, but it will still be whatever
        """
        # TODO
        pass


    def test_is_instance(self):
        """
        Everything is kinda whatever
        """
        #TODO
        self.assertTrue(isinstance('blah', Whatever))
        self.assertTrue(isinstance(5, Whatever))
        self.assertTrue(isinstance(5.5, Whatever))
        self.assertTrue(isinstance(True, Whatever))
        self.assertTrue(isinstance(self, Whatever))


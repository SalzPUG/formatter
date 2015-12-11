#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from formatter import formatter

def test_formatter():
    assert_equals(formatter("{}, {}", "a", "b"),  "a, b")


def test_formatter2():
    assert_equals(formatter("{}, {}", "c", "b"),  "c, b")

def test_formatter3():
    assert_equals(formatter("{}, {}, {}", "c", "b", "z"),  "c, b, z")

@raises(IndexError)
def test_formatter4():
    formatter("{}, {}, {}")

def test_positional():
    assert_equals(formatter("{1}, {0}", "a", "b"), "b, a")

def test_positional_multi():
    assert_equals(formatter("{1}, {0}, {2}, {1}, {0}", "a", "b", "c"), "{1}, {0}, {2}, {1}, {0}".format("a", "b", "c"))

def test_positional_mix():
    assert_equals(formatter("{1}, {}, {2}, {}, {0}", "a", "b", "c"), "b, a, c, b, a")

def test_named_args_1():
    assert_equals(formatter("{a}", a="b"), "b")

def test_named_args_2():
    assert_equals(formatter("{a}, {b}, {a}", a="b", b="a"), "b, a, b")

def test_named_args_3():
    assert_equals(formatter("{a}, {0}", "a", a="b"), "b, a")

def test_escape():
    assert_equals(formatter("{{}}"), "{{}}".format())

def test_int():
    assert_equals(formatter("{}", 1), "1")

def test_int2():
    assert_equals(formatter("{0}", 1), "1")

def test_int3():
    assert_equals(formatter("{bla}", bla=1), "1")

def test_formatting():
    assert_equals(formatter("{:d}", 1), "1")

def test_formatting2():
    assert_equals(formatter("{}, {:d}", "k", 1), "k, 1")

def test_formatting3():
    assert_equals(formatter("{}, {blah:d}", "k", blah=1), "k, 1")

@raises(ValueError)
def test_whatever():
    formatter("{:d}", "blah")




"""Test the molecule text module."""

from __future__ import annotations

from molecule.text import (
    camelize,
    strip_ansi_color,
    strip_ansi_escape,
    title,
    underscore,
)


def test_camelize() -> None:  # noqa: D103
    assert camelize("foo") == "Foo"
    assert camelize("foo_bar") == "FooBar"
    assert camelize("foo_bar_baz") == "FooBarBaz"


def test_strip_ansi_color() -> None:  # noqa: D103
    s = "foo\x1b[0m\x1b[0m\x1b[0m\n\x1b[0m\x1b[0m\x1b[0m\x1b[0m\x1b[0m"

    assert strip_ansi_color(s) == "foo\n"


def test_strip_ansi_escape() -> None:  # noqa: D103
    string = "ls\r\n\x1b[00m\x1b[01;31mfoo\x1b[00m\r\n\x1b[01;31m"

    assert strip_ansi_escape(string) == "ls\r\nfoo\r\n"


def test_title() -> None:  # noqa: D103
    assert title("foo") == "Foo"
    assert title("foo_bar") == "Foo Bar"


def test_underscore() -> None:  # noqa: D103
    assert underscore("Foo") == "foo"
    assert underscore("FooBar") == "foo_bar"
    assert underscore("FooBarBaz") == "foo_bar_baz"

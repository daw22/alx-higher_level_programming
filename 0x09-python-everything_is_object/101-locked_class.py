#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """instance of this class cn only be intialized with
    attribute called 'first_name'"""
    __slots__ = ('first_name',)

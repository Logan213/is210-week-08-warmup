#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Decent Docstring"""


def bool_to_str(bval):
    """Docstring.

    Args:
        bool_to_str(bool): Arg that is evaluated for truthiness or falsiness.

    Returns:
        A string indicating Yes or No depending on truthiness or falsiness.

    Examples:
        >>> bool_to_str(1)
        'Yes'

        >>> bool_to_str('')
        'No'

    """
    mybool = ''
    if bval:
        mybool = 'Yes'
    else:
        mybool = 'No'
    return mybool

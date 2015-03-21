#! usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""

import decimal


def lexicographics(to_analyze):
    """Required string to calculate max, min and avg number of words.

    Args:
        to_analyze(str): Arg string to calculate length

    Returns:
        A tuple with max, min and average of a list of words.

    Example:
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))

    """
    mylist = to_analyze.split('\n')
    stats = []
    for item in mylist:
        val = len(item.split())
        stats.append(val)
    return (max(stats), min(stats), sum(stats)/decimal.Decimal(len(stats)))

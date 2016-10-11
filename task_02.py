#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02 docstring"""


def prepare_email(appointments):
    """Create a list with clients and email.

    Args:
        appointment(list): clients and appointments in tuples.

    Returns:
        list: list with client and email.

    Examples:
        >>>prepare_email([('Jen', '2015'),('Max', 'March 3')])
        ['Dear Jen, \nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max, \NI look forward to meeting with you on March 3.\nBest,\nMe']
    """

    email = 'Dear{}, \nI look forward to meeting with you on {}.\nBest,\nMe'
    new_list = []
    for list_item in appointments:
        name = list_item[0]
        date = list_item[1]
        new_list.append(email.format(name, date))

    return new_list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_01 docstring"""


def get_party_stats(families, table_size=6):
    """This calculate people and table needed for the party.

    Args:
        families(list): list of families members.
        table_size(int, optional): Maximum of seats per table.

    Returns:
        tuple: Total atending members and total of number of tables.

    Examples:
        >>>get_party_stats([['Jan'],['Jen', 'Jess']])
        (3, 2)
    """

    guests = 0
    tables = 0
    for list_item in families:
        guests = guest + len(list_item)
        tables = tables + (-(-(len(list_item))//table_size))

    return (guests, tables)



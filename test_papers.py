#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import py
import re
from papers import decide


def test_basic():

    assert decide("test_returning_citizen.json", "watchlist.json","countries.json") == ["Accept", "Accept"]
 #   assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Secondary"]
  #  assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_quarantine.json", r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Quarantine"]
'''
def test_files():
    with pytest.raises(FileNotFoundError):
        decide("test_returning_citizen.json", "", "countries.json")
'''
# add functions for other tests


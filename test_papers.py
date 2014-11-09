#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = "Tania_Misquitta and Vidhya_Arulnathan"
__email__ = "tania.misquitta@mail.utoronto.ca / vidhya.arulnathan@mail.utotonto.ca"

__copyright__ = "2014 Tania Vidhya"
__license__ = "Tania Vidhya License"

__status__ = "Prototype"

# imports one per line
import pytest
import py
import re
from papers import decide, valid_date_format, valid_passport_format


def test_basic():

    assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_returning_citizen.json", r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Accept", "Accept"]
    assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Secondary"]
    assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_quarantine.json", r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Quarantine"]
    assert decide(r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\test_reject.json", r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\watchlist.json",r"C:\Users\Nathan\PycharmProjects\inf1340_2014_asst2\countries.json") == ["Reject"]


def test_files():
    with pytest.raises(FileNotFoundError):
        decide("test_returning_citizen.json", "", "countries.json")


def test_date_format():
    assert valid_date_format("Nov 4") == 'False'
    assert valid_date_format("2012-10-09") == 'True'


def test_passport():
    assert valid_passport_format("S3Q1-5ABCD-8EFGH-9XYZ1-TH60U") == False
    assert valid_passport_format("hs2ir-YR34H-jdkt9-THY78-absc4") == True





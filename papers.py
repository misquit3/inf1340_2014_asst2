#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Tania_Misquitta and Vidhya_Arulnathan
__assignment__ = "inf1340_2014_asst2"


__status__ = "Prototype"

# imports one per line
import re
import datetime
import json


def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"

    """
    with open(countries_file, "r") as file_reader:
        country_contents = file_reader.read()
        country_contents = json.loads(country_contents)

    with open(watchlist_file, "r") as file_reader:
        watch_contents = file_reader.read()
        watch_contents = json.loads(watch_contents)
    with open(input_file,"r") as file_reader:
        entries_contents = file_reader.read()
        entries_contents = json.loads(entries_contents)

        for cont in country_contents:
            for item in entries_contents:
     #check for quarantine
                if country_contents[cont]['medical_advisory'] != "":

                    if cont == item['from']['country']:

                        return ("Quarantine")

                    elif 'via' in item.keys():
                        if cont == item['via']['country']:
                            return ("Quarantine")
    #check for visitor visa
        for cont in country_contents:
            if country_contents[cont]['visitor_visa_required'] == '1':
                for item in entries_contents:
                    if item['entry_reason'] == "visit":
                        if cont == item['from']['country']:
                            if 'visa' in item.keys():
                                visit_visa_date = datetime.strptime(item['visa']['date'], "%Y-%m-%d")
                                visit_visa_year = visit_visa_date.year
                                if visit_visa_year > 2012:
                                    return ("Accept")
                            else:
                                return ("Reject")


     #check for transit visa
        for cont in country_contents:
            if country_contents[cont]['transit_visa_required'] == '1':
                for item in entries_contents:
                    if item['entry_reason'] == "transit":
                        if cont == item['from']['country']:
                            if 'visa' in item.keys():
                                transit_visa_date = datetime.strptime(item['visa']['date'], "%Y-%m-%d")
                                transit_visa_year = transit_visa_date.year
                                if transit_visa_year > 2012:
                                    return ("Accept")
                            else:
                                return ("Reject")


    #check watchlist
        for item in entries_contents:
            for watch in watch_contents:
                if item['first_name'] == watch['first_name']:
                    return ("Secondary")
                elif item['last_name'] == watch['last_name']:
                    return ("Secondary")
                elif item['passport'] == watch['passport']:
                    return ("Secondary")
    #Returning home
        for item in entries_contents:
            if item['home']['country'] == 'KAN':
                if item['from']['country'] not in ('ELE', 'LUG'):
                    return ("Accept")




    


def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

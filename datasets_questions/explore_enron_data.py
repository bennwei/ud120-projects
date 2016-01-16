#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print "How many data points (people) are in the dataset? ", len(enron_data)
# For each person, how many features are available?
print "For each person, how many features are available? ", len(enron_data["SKILLING JEFFREY K"])
print enron_data["SKILLING JEFFREY K"]
poi_count = 0
for i in enron_data:
    if enron_data[i]["poi"] == 1:
        poi_count += 1
print "How many POIs are there in the E+F dataset? ", poi_count

print "What is the total value of the stock belonging to James Prentice? ", \
    (enron_data['PRENTICE JAMES']['total_stock_value'])

print "How many email messages do we have from Wesley Colwell to persons of interest? ", \
        enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What's the value of stock options exercised by Jeffrey Skilling? ", \
        enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "SKILLING JEFFREY K money: ", enron_data['SKILLING JEFFREY K']['total_payments']

print "Lay, Kenneth money: ", enron_data['LAY KENNETH L']['total_payments']

quantified_salary_count = 0
for i in enron_data:
    if enron_data[i]['salary'] != 'NaN':
        quantified_salary_count += 1
print "How many folks in this dataset have a quantified salary? ", \
        quantified_salary_count

email_address_count = 0
for i in enron_data:
    if enron_data[i]['email_address'] != 'NaN':
        email_address_count += 1
print "What about a known email address? ", email_address_count

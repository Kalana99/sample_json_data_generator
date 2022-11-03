import json
import random


def get_reg_nos(count):

    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]

    reg_nos = []
    no_int = 0

    while len(reg_nos) < count:

        # reg_no = chr(random.randint(65, 90)) * 3 + "%04d" % random.randint(0, 9999)
        reg_no = "AAA" + "%04d" % no_int

        if reg_no not in reg_nos:
            reg_nos.append(reg_no)
            no_int += 1

    return reg_nos


def get_names(count):

    names = []

    for i in range(count):
        names.append("sample_station_" + "%04d" % i)

    return names


def get_contact_nos(count):

    sp = ["070", "071", "072", "074", "075", "076", "077", "078"]

    nos = []
    for _ in range(count):

        no = random.choice(sp) + "%07d" % random.randint(0, 9999999)
        nos.append(no)

    return nos


def get_locations(count):

    cities = []

    with open("cities.txt", 'r') as f:
        lines = f.readlines()

    for city in lines:
        cities.append(city[:-1])

    locations = []
    while len(locations) < count:

        sel_loc = random.choice(cities)
        locations.append(sel_loc)

    return locations


def get_emails(count):

    emails = []
    while len(emails) < count:

        email = "examplestationemail" + "%04d" % random.randint(0, 9999) + "@gmail.com"

        if email not in emails:
            emails.append(email)

    return emails


def create_stations():

    global count, reg_nos, names, nos, locations, companies, emails

    stations = []

    for i in range(count):

        station = {}

        station["registrationNo"] = reg_nos[i]
        station["name"] = names[i]
        station["contactNo"] = nos[i]
        station["location"] = locations[i]
        station["company"] = random.choice(companies)
        station["email"] = emails[i]

        stations.append(station)

    return stations


def write_json(data, out_file_name, indentation):

    out_file = open(out_file_name, "w")
    json.dump(data, out_file, indent=indentation)
    out_file.close()


count = 1000

reg_nos = get_reg_nos(count)
names = get_names(count)
nos = get_contact_nos(count)
locations = get_locations(count)
companies = ["Ceypetco", "Lanka IOC"]
emails = get_emails(count)

stations = create_stations()

out_file_name = "stations.json"
indentation = 4
write_json(stations, out_file_name, indentation)

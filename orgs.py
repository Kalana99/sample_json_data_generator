import json
import random


def get_reg_nos(count):

    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]

    reg_nos = []
    no_int = 0

    while len(reg_nos) < count:

        # reg_no = chr(random.randint(65, 90)) * 3 + "%04d" % random.randint(0, 9999)
        reg_no = "ZZZ" + "%04d" % no_int

        if reg_no not in reg_nos:
            reg_nos.append(reg_no)
            no_int += 1

    return reg_nos


def get_names(count):

    names = []

    for i in range(count):
        names.append("sample_org_" + "%04d" % i)

    return names


def get_contact_nos(count):

    sp = ["070", "071", "072", "074", "075", "076", "077", "078"]

    nos = []
    for _ in range(count):

        no = random.choice(sp) + "%07d" % random.randint(0, 9999999)
        nos.append(no)

    return nos


def get_addresses(count):

    addresses = []
    no_int = 0

    while len(addresses) < count:

        add_no = "%04d" % random.randint(1000, 9999)
        add_st = "sample_street_" + str(no_int)
        add_city = "sample_city_" + str(no_int)
        address = ", ".join([add_no, add_st, add_city])

        addresses.append(address)
        no_int += 1

    return addresses


def get_emails(count):

    emails = []
    while len(emails) < count:

        email = "exampleorgemail" + "%04d" % random.randint(0, 9999) + "@gmail.com"

        if email not in emails:
            emails.append(email)

    return emails


def create_orgs():

    global count, reg_nos, names, nos, addresses, emails

    orgs = []

    for i in range(count):

        org = {}

        org["registrationNo"] = reg_nos[i]
        org["name"] = names[i]
        org["contactNo"] = nos[i]
        org["address"] = addresses[i]
        org["email"] = emails[i]
        org["priority"] = random.randint(1, 5)

        orgs.append(org)

    return orgs


def write_json(data, out_file_name, indentation):

    out_file = open(out_file_name, "w")
    json.dump(data, out_file, indent=indentation)
    out_file.close()


count = 1000

reg_nos = get_reg_nos(count)
names = get_names(count)
nos = get_contact_nos(count)
addresses = get_addresses(count)
emails = get_emails(count)

orgs = create_orgs()

out_file_name = "orgs.json"
indentation = 4
write_json(orgs, out_file_name, indentation)

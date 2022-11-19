import json
import random


vehicle_types = [
        "A-Bicycle",
        "B-Tricycle/Car",
        "C-Lorry",
        "D-Bus",
        "G-Agricultural",
        "J-Special Purpose"
    ]

type_fuel_type = {"petrol": [0], "diesel": [3, 5], "both": [1, 2, 4]}


def get_reg_nos(count):

    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]

    global personal

    province_code = ["CP", "EP", "NC", "NE", "NW", "SB", "SP", "UP", "WP"]

    reg_nos = []
    no_int = 0

    while len(reg_nos) < count:

        # reg_no = chr(random.randint(65, 90)) * 3 + "%04d" % random.randint(0, 9999)
        mid_str = "-AAA-" if personal else "-BBB-"
        reg_no = random.choice(province_code) + mid_str + "%04d" % no_int

        if reg_no not in reg_nos:
            reg_nos.append(reg_no)
            no_int += 1

    return reg_nos


def get_eng_nos(count):

    global personal

    eng_nos = []
    no_int = 0

    while len(eng_nos) < count:

        mid_str = "-AAA-" if personal else "-BBB-"
        eng_no = "%02d" % (no_int % 100) + mid_str + "%05d" % no_int

        if eng_no not in eng_nos:
            eng_nos.append(eng_no)
            no_int += 1

    return eng_nos


def get_owner_nics(count):

    nics = []
    no_int = 0

    while len(nics) < count:

        if no_int % 2 == 0:
            nic = "%04d" % random.randint(2000, 2023) + "%03d" % random.randint(1, 366) + "%05d" % random.randint(0, 99999)
        else:
            nic = "%02d" % random.randint(0, 99) + "%03d" % random.randint(1, 366) + "%04d" % random.randint(0, 9999) + "v"

        nics.append(nic)
        no_int += 1

    return nics


def get_types(count):

    global vehicle_types

    types = []
    for _ in range(count):
        types.append(random.choice(vehicle_types))

    return types


def get_fuel_types(types):

    global vehicle_types, type_fuel_type

    fuel_types = []

    for type in types:

        if vehicle_types.index(type) in type_fuel_type["petrol"]:
            fuel_types.append("Petrol")
        elif vehicle_types.index(type) in type_fuel_type["diesel"]:
            fuel_types.append("Diesel")
        else:
            fuel_types.append(random.choice(["Petrol", "Diesel"]))

    return fuel_types


def create_vehicles():

    global count, reg_nos, eng_nos, nics, types, fuel_types, vehicle_types

    vehicles = []

    for i in range(count):

        vehicle = {}

        vehicle["registrationNo"] = reg_nos[i]
        vehicle["engineNo"] = eng_nos[i]
        vehicle["ownerNIC"] = nics[i]
        vehicle["type"] = types[i]
        vehicle["fuelType"] = fuel_types[i]

        if types[i] in vehicle_types[4:]:
            vehicle["priority"] = 1
        else:
            vehicle["priority"] = random.randint(1, 5)

        vehicles.append(vehicle)

    return vehicles


def write_json(data, out_file_name, indentation):

    out_file = open(out_file_name, "w")
    json.dump(data, out_file, indent=indentation)
    out_file.close()


count = 1000
# personal = True
personal = False

reg_nos = get_reg_nos(count)
eng_nos = get_eng_nos(count)
nics = get_owner_nics(count)
types = get_types(count)
fuel_types = get_fuel_types(types)

vehicles = create_vehicles()

out_file_name = "personal_vehicles.json" if personal else "org_vehicles.json"
indentation = 4
write_json(vehicles, out_file_name, indentation)

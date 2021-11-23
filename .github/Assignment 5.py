# Programmers: Victoria Shelton
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

# Defining constant variables

taxi_list = []
TAXI_ID = 0
TRIP_DATE_TIME = 1
TRIP_END_TIME = 2
DURATION = 3
DISTANCE = 4
COST = 5
PAYMENT_TYPE = 6
PICKUP_LAT = 7
PICKUP_LON = 8
DROP_LAT = 9
DROP_LON = 10


def load_file_data(filename):
    global file
    lines = 0
    try:
        file = open(filename, "r")
        try:
            for line in file:
                lines += 1
                line_entries = line.split(",")
                line_entries[TAXI_ID] = line_entries[TAXI_ID].strip()
                line_entries[TRIP_DATE_TIME] = line_entries[TRIP_DATE_TIME]
                line_entries[TRIP_END_TIME] = line_entries[TRIP_END_TIME]
                line_entries[DURATION] = line_entries[DURATION]
                line_entries[DISTANCE] = line_entries[DISTANCE]
                line_entries[COST] = line_entries[COST]
                line_entries[PAYMENT_TYPE] = line_entries[PAYMENT_TYPE].strip()
                line_entries[PICKUP_LAT] = line_entries[PICKUP_LAT]
                line_entries[PICKUP_LON] = line_entries[PICKUP_LON]
                line_entries[DROP_LAT] = line_entries[DROP_LAT]
                line_entries[DROP_LON] = line_entries[DROP_LON]
                taxi_list.append(line_entries)
        except ValueError:
            print("Error in line" + str(lines) + ", line skipped.")
    except FileNotFoundError:
        print("This file does not exist.")
    file.close()
    return taxi_list


def average_cost(t_list):
    average_cash = 0
    for line in t_list:
        if t_list[PAYMENT_TYPE] == "cash":
            average_cash = t_list[COST] + average_cash
    return average_cash


def main():
    print(average_cost(load_file_data("2016_09.csv")))

main()

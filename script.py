from __future__ import print_function
import csv
from textwrap import indent
from tokenize import Double


class Apartment:
    def __init__(self, url, address, building, commute, crime, pets, beds, doorman, elevator):
        self.url = url
        self.address = address
        self.building = building
        self.commute = int(commute)
        self.crime = float(crime)
        self.pets = int(pets)
        self.beds = int(beds)
        self.doorman = int(doorman)
        self.elevator = int(elevator)
        self.score = 100
        self.calc_score()

    def calc_score(self):
        CRIME_MULTIPLIER = 2.5  # 50%
        COMMUTE_MULTIPLIER = 0.5  # 20%
        NO_PETS = 3  # 3%
        STUDIO = 5  # 5%
        NO_DOORMAN = 15  # 15%
        NO_ELEVATOR = 7  # 7%

        SHORT_COMMUTE = 20
        LOW_CRIME_RATE = 10

        if self.commute > SHORT_COMMUTE:
            commute = (self.commute - SHORT_COMMUTE)*COMMUTE_MULTIPLIER
            self.score -= min(commute, 20)
        if self.crime > LOW_CRIME_RATE:
            self.score -= (self.crime - LOW_CRIME_RATE)*CRIME_MULTIPLIER
        if self.pets == 0:
            self.score -= NO_PETS
        if self.beds == 0:
            self.score -= STUDIO
        if self.doorman == 0:
            self.score -= NO_DOORMAN
        if self.elevator == 0:
            self.score -= NO_ELEVATOR

        self.score = round(self.score)

    def get_score(self):
        return self.score


apartment_List: Apartment = []

with open('Apartments.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        # print(row)
        apartment_List.append(
            Apartment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

apartment_List.sort(key=lambda apt: apt.score, reverse=True)

with open('results.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Score", "URL", "Address", "Building", "Commute",
                    "CrimeRate", "Pets", "Beds", "Doorman", "Elevator"])
    for index, apartment in enumerate(apartment_List):
        writer.writerow([apartment.score, apartment.url, apartment.address, apartment.building, apartment.commute, apartment.crime,
                        "Yes" if apartment.pets else "No", "Studio" if apartment.beds == 0 else f"{apartment.beds}Br", "Yes" if apartment.doorman else "No", "Yes" if apartment.elevator else "No"])

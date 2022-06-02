from __future__ import print_function
import csv
from textwrap import indent


class Apartment:
    def __init__(self, url, address, building, commute, crime, pets, beds, doorman, elevator):
        self.url = url
        self.address = address
        self.building = building
        self.commute = int(commute)
        self.crime = int(crime)
        self.pets = int(pets)
        self.beds = int(beds)
        self.doorman = int(doorman)
        self.elevator = int(elevator)
        self.score = 100
        self.calc_score()

    def calc_score(self):
        CRIME_MULTIPLIER = 1.5  # 30%
        COMMUTE_MULTIPLIER = 0.66  # 20%
        SHORT_COMMUTE = 20
        NO_PETS = 5  # 5%
        STUDIO = 10  # 10%
        NO_DOORMAN = 20  # 20%
        NO_ELEVATOR = 15  # 15%
        LOW_CRIME_RATE = 10

        if self.commute > SHORT_COMMUTE:
            self.score -= (self.commute - SHORT_COMMUTE)*COMMUTE_MULTIPLIER
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


apartment_List: Apartment = []

with open('Apartments.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        apartment_List.append(
            Apartment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

print("")
for apartment in apartment_List:
    print(apartment.score)

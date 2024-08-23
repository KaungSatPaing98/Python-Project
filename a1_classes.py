"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from placecollection import PlaceCollection

""" Travel Tracker Assignment 1

Created by Kaung Sat Paing, 21 April 2023
URL - https://github.com/JCUS-CP1404/cp1404--travel-tracker---assignment-1-KaungSatPaing98

"""

import random
from place import Place
from placecollection import PlaceCollection

""" Travel Tracker Assignment 1

Created by Kaung Sat Paing, 21 April 2023
URL - https://github.com/JCUS-CP1404/cp1404--travel-tracker---assignment-1-KaungSatPaing98

"""

FILENAME = "places.csv"
MENU = """Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit"""


def main():
    """Allow users to track places they want to travel and already travel."""
    print("Travel Tracker 1.0 - by Kaung Sat Paing")

    place_collection = PlaceCollection()
    place_collection.load_places(FILENAME)
    visited_places = list_visited_places(place_collection.places)
    unvisited_places = list_unvisited_places(place_collection.places)
    print("{} places loaded from {}".format(len(place_collection.places), FILENAME))
    print(MENU)

    choice = input(">>> ").lower()
    while choice != 'q':

        if choice == 'l':
            place_collection.sort()
            visited_places = list_visited_places(place_collection.places)
            unvisited_places = list_unvisited_places(place_collection.places)
            list_places(place_collection.places, visited_places, unvisited_places)
        elif choice == 'r':
            random_places(place_collection.places)
        elif choice == 'a':
            add_new_place(place_collection, unvisited_places)
        elif choice == 'm':
            mark_places(place_collection.places, visited_places, unvisited_places)
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").lower()

    place_collection.save_places(FILENAME)
    print(f"{len(place_collection.places)} places saved to {FILENAME}")
    print("Have a nice day :)")


def list_visited_places(places):
    """ List places for visited places"""
    visited_places = []
    for visited_place in places:
        if visited_place.is_visited:
            visited_places.append(visited_place)
    return visited_places


def list_unvisited_places(places):
    """ List places for unvisited places"""
    unvisited_places = []
    for unvisited_place in places:
        if not unvisited_place.is_visited:
            unvisited_places.append(unvisited_place)
    return unvisited_places


def list_places(places, visited_places, unvisited_places):
    """ Display formatted list of places details."""
    # sort_places(unvisited_places, visited_places)

    count = 1
    for place in unvisited_places:  # looping for unvisited places
        if not place.is_visited:
            print("{}{}. {:8} in {:11} {:>2}".format("*", count, place.name, place.country, place.priority))
            count += 1

    for place in visited_places:  # looping for visited places
        if place.is_visited:
            print(" {}. {:8} in {:11} {:>2}".format(count, place.name, place.country, place.priority))
            count += 1

    if len(places) == len(visited_places):  # when the unvisited places is not have / displaying the No places to visit
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print("{} places. You still want to visit {} places.".format(len(places),
                                                                     (len(places) - len(visited_places))))


def random_places(places):
    """ Random places for unvisited places """
    unvisited_places = [place for place in places if place.is_visited == False]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print("Not sure where to visit next?")
        print(f"How about... {place.name} in {place.country}?")
    else:
        print("No places left to visit!")


def mark_places(places, visited_places, unvisited_places):
    if len(places) == len(visited_places):  # check the all places are visited
        print("No unvisited places")
    else:
        list_places(places, visited_places, unvisited_places)
        print("Enter the number of a place to mark as visited")

        valid_place_num = False
        while not valid_place_num:  # error checking for mark places number input
            try:
                choice = int(input(">>> "))
                if choice > 0 and places[choice - 1]:
                    if choice <= len(unvisited_places):  # check for number input
                        marked_place = unvisited_places[choice - 1]
                        print("{} in {} visited".format(marked_place.name, marked_place.country))
                        marked_place.is_visited = True
                        visited_places.append(marked_place)
                        del unvisited_places[choice - 1]
                    else:
                        marked_place = visited_places[choice - len(unvisited_places) - 1]
                        print(f"You have already visited {marked_place.name}")
                    valid_place_num = True
                    return choice - 1
                else:
                    print("Number must be > 0")
            except IndexError:
                print("Invalid place number")
            except ValueError:
                print("Invalid input; enter a valid number")


def add_new_place(place_collection, unvisited_places):
    """ Add new places to CSV file"""
    while True:
        name = input("Name: ")
        if name:
            break
        else:
            print("Input cannot be blank")
    while True:
        country = input("Country: ")
        if country:
            break
        else:
            print("Input cannot be blank")
    while True:
        try:
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Priority must be an integer")
    new_places = Place(name, country, priority, False)
    print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
    place_collection.add_place(new_places)
    unvisited_places.append(new_places)
    place_collection.save_places(FILENAME)


main()

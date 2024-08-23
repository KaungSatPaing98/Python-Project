"""..."""


# Create your PlaceCollection class in this file


import csv
from operator import attrgetter
from place import Place


class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                priority = int(priority)
                visited = visited.lower() == "v"
                place = Place(name, country, priority, visited)
                self.places.append(place)

    def save_places(self, file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            for place in self.places:
                if place.is_visited:
                    is_visited = "v"
                else:
                    is_visited = "n"
                writer.writerow([place.name, place.country, place.priority, is_visited])

    def add_place(self, place):
        self.places.append(place)

    def get_num_unvisited_places(self):
        count = sum(1 for place in self.places if not place.is_visited)
        return count

    def sort(self, mode):
        self.places.sort(key=lambda x: x.priority)


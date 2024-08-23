"""CP1404 Travel Tracker Assignment-2

Created by Kaung Sat Paing Started date - 26.05.2023

https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-KaungSatPaing98"""


# Create your Place class in this file


class Place:
    """creating Place class and adding attributes"""
    def __init__(self, name="", country="", priority=0, is_visited=True):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited
        self.status = self.is_visited

    def __str__(self):
        """displaying the name, country, priority, and visited status."""
        visited_status = "Visited" if self.is_visited else "Not Visited"
        return f"{self.name} in {self.country} Priority: {self.priority}  ({visited_status})"

    def mark_visited(self):
        """The mark_visited method marks the place as visited by setting the visited attribute to True."""
        self.is_visited = True

    def mark_unvisited(self):
        """The mark_unvisited method marks the place as unvisited by setting the visited attribute to False."""
        self.is_visited = False

    def is_important(self):
        return self.priority <= 2

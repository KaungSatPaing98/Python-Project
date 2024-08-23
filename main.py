"""
Name:Kaung Sat Paing
Date:26 May 2023
Brief Project Description:Travel Tracker 2 with GUI interface
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-KaungSatPaing98
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection
from kivy.properties import StringProperty

FILENAME = 'places.csv'
SORTING_MODES = ['Name', 'Country', 'Priority', 'Visited']
SOFT_GREEN = (0, 0.5, 0.5, 1)
GRAY = (0.5, 0.5, 0.5, 1)
WHITE = (1, 1, 1, 1)


class TravelTrackerApp(App):
    """Creating travel tracker app"""
    program_state = StringProperty()
    status_label = StringProperty()

    def __init__(self, **kwargs):
        """Initialize the attributes."""
        super().__init__(**kwargs)
        self.places = []
        PlaceCollection.load_places(self, FILENAME)
        self.sorting_modes = SORTING_MODES
        self.current_mode = self.sorting_modes[0]

    def build(self):
        """ Create a widget of places to travel """
        self.title = "TravelTacker"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creating places button """
        for place in self.places:
            if place.status == 'n':
                place_button = Button(text=str(place))
                place_button.background_color = GRAY
                place_button.color = WHITE
            else:
                place_button = Button(text=f"{place.name} in {place.country}, priority {place.priority}")
                place_button.background_color = SOFT_GREEN
                place_button.color = WHITE

            place_button.bind(on_release=self.press_entry)
            place_button.place = place
            self.root.ids.place_display.add_widget(place_button)
        self.display_visited_unvisited_num()

    def press_entry(self, instance):
        """ Handle pressing place button """
        current_place = instance.place
        if current_place.status == 'n':
            current_place.is_visited = 'n'
            current_place.status = 'v'
            instance.text = f"{current_place.name}(visited)"
            self.program_state = f"You need to visit {current_place.name}"
            instance.background_color = SOFT_GREEN
        else:
            current_place.is_visited = 'v'
            current_place.status = 'n'
            instance.text = str(current_place)
            self.program_state = f"You have visited {current_place.name}"
            instance.background_color = GRAY

        if self.current_mode == 'Visited':
            self.sort_places("Visited")
        self.display_visited_unvisited_num()

    def sort_places(self, mode):
        """ Sort the places button according to chosen mode"""
        self.current_mode = mode
        if mode == 'v':
            mode = 'status'
        mode = str(mode).lower()
        PlaceCollection.sort(self, mode)
        self.clear_all()
        self.create_widgets()

    def clear_all(self):
        """ Clear all the place buttons"""
        self.root.ids.place_display.clear_widgets()

    def on_top(self):
        """Update changes to the file when the program is closed"""
        self.current_mode = self.sorting_modes[0]
        PlaceCollection.save_places(self, FILENAME)

    def add_new_places(self, name, country, priority):
        """add new places"""
        if self.valid_inputs(name, country, priority):
            new_place = Place(name, country, int(priority), 'n')
            PlaceCollection.add_place(self, new_place)
            place_button = Button(text=f"{new_place.name}(unvisited)")
            place_button.bind(on_release=self.press_entry)
            place_button.place = new_place
            self.root.ids.place_display.add_widget(place_button)
            self.sort_places(mode=self.current_mode)
            self.display_visited_unvisited_num()
            self.clear_data()

    def valid_inputs(self, name, country, priority):
        """ Check if the inputs for places are valid"""

        if name == '' or country == '' or priority == '':
            self.program_state = f"All fields must be completed"
            return False
        else:
            try:
                place_priority = int(priority)
                if place_priority < 0:
                    self.program_state = f"Priority must be > 0"
                    return False
            except ValueError:
                self.program_state = f"Please enter a valid number"
                return False
            return True

    def display_visited_unvisited_num(self):
        """Display of places and unvisited places"""
        self.status_label = f"Places to visit: {PlaceCollection.get_num_unvisited_places(self)}"

    def clear_data(self):
        """Clear all the inputs textbox and program state at the button"""
        self.root.ids.input_name.text = ''
        self.root.ids.input_country.text = ''
        self.root.ids.input_priority.text = ''
        self.program_state = ''


if __name__ == '__main__':
    TravelTrackerApp().run()

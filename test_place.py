"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited

    # TODO: Add more tests, as appropriate, for each method
    # Test mark_visited method
    print("Test mark_visited:")
    new_place.mark_visited()
    assert new_place.is_visited

    # Test mark_unvisited method
    print("Test mark_unvisited:")
    new_place.mark_unvisited()
    assert not new_place.is_visited

    # Test is_important method
    print("Test is_important:")
    important_place = Place("Important Place", "Country", 2, False)
    unimportant_place = Place("Unimportant Place", "Country", 3, False)
    assert important_place.is_important()
    assert not unimportant_place.is_important()


run_tests()

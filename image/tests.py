from django.test import TestCase

# Create your tests here.
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    def test_update_location(self):
        new_location = 'kericho'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='kericho')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
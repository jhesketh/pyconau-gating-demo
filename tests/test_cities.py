import testtools

import cities


class TestCities(testtools.TestCase):
    def test_largest(self):
        largest = 'Sydney'
        self.assertEqual(
            largest, cities.largest_city(cities.get_population_data()).name)

import unittest
import pytest
import requests


class Test(unittest.TestCase):
    test_data_zip_codes = [
    ("us", "90210", "Beverly Hill"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")]

    @pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
    @staticmethod
    def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
        response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
        response_body = response.json()
        assert response_body["places"][0]["place name"] == expected_place_name



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
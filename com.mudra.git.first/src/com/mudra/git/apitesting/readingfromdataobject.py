import pytest
import requests
'''
To make pytest runner work on eclipse

https://stackoverflow.com/questions/41399825/how-to-run-pytest-on-eclipse
        Window -> Preferences -> PyDev -> PyUnit
        Change the test runner to "py.test runner" and clear the parameters (or add the ones you prefer. Make sure they are valid flags for pytest.)

example run
#@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
#def test_eval(test_input, expected):
 #   assert eval(test_input) == expected
'''
test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")]

@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name


'''
 NOTES:
 https://docs.pytest.org/en/stable/parametrize.html#parametrize
 https://docs.pytest.org/en/stable/unittest.html
'''
    
    
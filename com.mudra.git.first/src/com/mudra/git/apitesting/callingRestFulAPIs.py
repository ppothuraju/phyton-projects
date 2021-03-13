'''
https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/
'''
import unittest
import requests

class TestcallingRestFulAPI(unittest.TestCase):
    purl = "http://api.zippopotam.us/IN/522001"
    
    '''
    NOTES: 
    In Python you should add self argument as the first argument to all defined methods in classes.
     def method(self,arg):
     Occasionally (but not often), you really don't care about the object that your method is bound to, and in that circumstance, you can decorate the method with the builtin staticmethod() function to say so:
    @staticmethod
    def method(arg):
        print(arg)
    '''
    #assertion that checks that the HTTP status code equals 200:
    def test_get_locations_for_us_522001_check_status_code_equals_200(self):
        response = requests.get(purl)
        assert response.status_code == 200
        
    #check if the value of the response content type header correctly identifies that the response body is in JSON format    
    @staticmethod
    def test_get_locations_for_us_522001_check_content_type_equals_json():
        response = requests.get(purl)
        assert response.headers["Content-Type"] == "application/json"
     
    #first check that the response body element country is equal to United States   
    def test_get_locations_for_us_522001_check_country_equals_india(self):
        response = requests.get(purl)
        response_body = response.json()
        assert response_body["country"] == "India"
     
    #assert on the value of the place name for the first place in the list of places,    
    def test_get_locations_for_us_522001_check_city_equals_kothapet(self):
        response = requests.get(purl)
        response_body = response.json()
        assert response_body["places"][0]["place name"] == "G T R Kothapet"
    
    #check that all places returned belong to only state Andhra Pradesh,    
    def test_get_locations_for_us_522001_check_state_equals_andhra_pradesh_for_all_results(self):
        response = requests.get(purl)
        response_body = response.json()
        states_in_response = []
        i=0
        for i in range(len(response_body["places"])):
            states_in_response.append(response_body["places"][i]["state"])
        #print(state_in_response)  
        unique_states = set(states_in_response)
        if len(unique_states)>1:
            print("Invalid number of states")
        else:
            assert unique_states.pop() == "Andhra Pradesh"
        
    #check that the list of places returned by the API contains exactly one entry:
    @staticmethod
    def test_get_locations_for_us_522001_check_multiple_places_are_returned():
        response = requests.get(purl)
        response_body = response.json()
        assert len(response_body["places"]) == 1 #returns multiple places and test fail
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
import urllib.request
import json

def check_car_in_database(make):
    """Checks whether the car (model and make) is in the database"""
    
    URL = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
    try:
        result = urllib.request.urlopen(URL).read()
        result = json.loads(result)
        models = []
        for model in result['Results']:
            models.append(model['Model_Name'])
        models = set(models)    
        return models
    except:
        print("Could not load: ", URL)
        return None


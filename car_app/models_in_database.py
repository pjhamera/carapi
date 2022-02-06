import urllib.request
import json

def models_from__database(make):
    """Return a list of models for a given make from the database
    included in the URL"""
    
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


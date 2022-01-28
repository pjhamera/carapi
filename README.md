# Car API

This API is used to add, retrieve and delete cars (make & model). <br />
Added cars can be rated (1-5). A list with all the cars with their average rating and a list with the most rated cars can be retrieved. <br />
Before a car is added to the database, the existence of the provided make and model is checked against the following external database: <br />
https://vpic.nhtsa.dot.gov/api/ (Get Models for Make). <br />

## Docker
The app has been dockerized. It is enough to run the docker-compose file (python manage.py migrate and runserver commands are included in the file).
I suggest using Postman to play around/test the API.

## Libraries/Toolkits
The app employs the Django Rest Framework, which is a very convenient and mighty toolkit used for building Rest APIs.

## Database 
I switched from the default SQLite database to the more powerful and compatible with Python Postgresql database, which is also offered by Heroku and 
in the case of Docker images is compatible with more architectures (including ARM and ARM64) <br />

## Heroku
The app has been deployed to Heroku: https://carapiapp.herokuapp.com (stopped working, have to look into it)<br />

## Browsable DRF API
I disabled the default browsable DRF API. <br />

## Endpoints

### POST /cars/ <br />
{ <br />
  "make" : "Volkswagen", <br />
  "model" : "Golf", <br />
} <br />

### DELETE /cars/{  id }/ <br />

### POST /rate/ <br />

{ <br />
  "car_id" : 1, <br />
  "rating" : 5, <br />
} <br />

### GET /cars/ <br />

Response: <br />
[  <br />
{ <br />
  "id" : 1, <br />
  "make" : "Volkswagen", <br />
  "model" : "Golf", <br />
  "avg_rating" : 5.0, <br />
}, <br />
{ <br />
  "id" : 2, <br />
  "make" : "Volkswagen", <br />
  "model" : "Passat", <br />
  "avg_rating" : 4.7, <br />
} <br />
] <br />

### GET /popular/ <br />
Response: <br />
[ <br />
{ <br />
  "id" : 1, <br />
  "make" : "Volkswagen", <br />
  "model" : "Golf", <br />
  "rates_number" : 100, <br />
}, <br />
{ <br />
  "id" : 2, <br />
  "make" : "Volkswagen", <br />
  "model" : "Passat", <br />
  "rates_number" : 31, <br />
} <br />


## Tests
Tests of the endpoints can be found in car_app -> tests.py.


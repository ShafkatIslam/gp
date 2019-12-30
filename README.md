# **REST key-val store**

Steps to Setup and Run The Project

✔️ This project has been developed using Python 3.6.5 on Windows  
✔️ It is mandatory that Python >= 3.6.5 must be installed in your system.Now, follow the below steps:

The project will run both your local machine and also a public domain.
I deployed it to the Heroku Server.

URL : https://gpsoftwareengineer.herokuapp.com

    For Get all the values of the store:
    
    URL : https://gpsoftwareengineer.herokuapp.com/api/GET/values/
   
   Then it will reponse for all the value under a key for each in JSON format. i.e, response: {key1: value1, key2: value2, key3: value3...}
   
    For Get one or more specific values from the store and also reset the TTL of those keys:
    
    URL : https://gpsoftwareengineer.herokuapp.com/api/GET/values/1
   
   Then it will reponse for the value under a key in JSON format. Here 1 is the index number and it a key that I used. You can use any number instead of 1 if you have value under that key in your database.
   i.e, {key1: value1, key2: value2}
   
    For Save a value in the store:
    
    URL : https://gpsoftwareengineer.herokuapp.com/api/POST/values/
    
   Then it will reponse to save new input to you following the format of JSON, i.e, KEY-VALUE pair like
   {key1: value1, key2: value2..}
   
    Update a value in the store and also reset the TTL.
    
    URL : https://gpsoftwareengineer.herokuapp.com/api/PATCH/values/1
    
   Then it will reponse for updating the value under a key in JSON format. Here 1 is the index number and it a key that I used. You can use any number instead of 1 if you have value under that key in your database.
   i.e, {key1: value1, key2: value2}
   
   TTL is set in the **view.py** file under the api folder.
   
   You can run the project on your local machine. Then you need to set up some required library.
    
    Setup Virtual Environment and Install Required Packages
    Start Django Server
    Send Request Using API
    
   Here is the installation Procedure:
    
    Install Required Package:
    
    pip install pipenv
    pipenv shell
    pipenv install django
    
    It is mandatory to migrate the database with command for the first time.
    
    python manage.py makemigrations
    python manage.py migrate
    
   URL for Local Machine: 
   
   http://127.0.0.1:8000/
   
   For Get all the values of the store:
    
    URL : http://127.0.0.1:8000/api/GET/values/
   
   Then it will reponse for all the value under a key for each in JSON format. i.e, response: {key1: value1, key2: value2, key3: value3...}
   
    For Get one or more specific values from the store and also reset the TTL of those keys:
    
    URL : http://127.0.0.1:8000/api/GET/values/1
   
   Then it will reponse for the value under a key in JSON format. Here 1 is the index number and it a key that I used. You can use any number instead of 1 if you have value under that key in your database.
   i.e, {key1: value1, key2: value2}
   
    For Save a value in the store:
    
    URL : http://127.0.0.1:8000/api/POST/values/
    
   Then it will reponse to save new input to you following the format of JSON, i.e, KEY-VALUE pair like
   {key1: value1, key2: value2..}
   
    Update a value in the store and also reset the TTL.
    
    URL : http://127.0.0.1:8000/api/PATCH/values/1
    
   Then it will reponse for updating the value under a key in JSON format. Here 1 is the index number and it a key that I used. You can use any number instead of 1 if you have value under that key in your database.
   i.e, {key1: value1, key2: value2}
    

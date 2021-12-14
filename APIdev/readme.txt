1- Add a virtual enviroment with the modules needed
   Path> py -3 -m venv <name>
   pip install fastapi[all]
2- Add my first function to call an http get method to show a message in localhost
   See Http methods (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
3- Start a live server with a reload option  $ uvicorn main: app --reload
4- Install postman to automatically create a GUI to test and deploy our APIs
5- Add a post request that takes input user data, saves it as a dictionary and display it in the form of a post
6- Use Pydantic to create an schema, The post data can be easily accessed inheriting from the BaseModel class
7- Create the Post Fields, required and Optionals 
   
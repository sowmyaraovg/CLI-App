"# CLI-App" 
This is a command line application in Python to read and write to Json schema.
Json is an easy to read, flexible text based format that can be used to store and communicate information and is mainly based on key:value pairs. I used Python, as Python makes it simple to work with JSON files.I am reading json files ad converting into a Python value (object).The data is returned as a Python dictionary (JSON object data structure).

Maps": [
      {
        "Continent:"xyz"
        "MapContent": [
          {
            "CountryName": "abcdefghij,
            "Capital": "klmn",
            "StateA" [
              {
                "Name": "name1",
                "Population": "989881"
              },
              {
                "Name": "name2",
                "Population": "576656"
              }
            ],
            "StateB": [
              {
                "Name": "name3",
                "Population": "3645487",
                
              },
             ]
         }
       ]
    }
]
I have used similar structure for my project.
I have loaded Json file into a variable and  access the data as python dict or list. 
Here in this example, we mostly deal with lists which have key value pairs.So, I considered using Maps as a list with Countries as key value pair.Again Countries is a list of states considered as key value pairs . Each State is a list of key value pairs of their names and population.

References:
https://docs.python.org/3.5/tutorial/index.html
https://codingnetworker.com/2015/10/python-dictionaries-json-crash-course/
Using Python to access Web Data-Coursera 
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html
Python programming tutorials -Socratica in youtube

Future Enhancements:
Adding Class structures and to improve the code by avoiding redundancy and repetitions in the code.
Use Flask to convert the CLI to Web app.


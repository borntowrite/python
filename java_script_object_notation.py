
# Java Script Object Notation = JSON

import json
print(dir(json))

json_file = open("c:/work/python/movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()
print(movie)
print(json.dumps(movie))
print(json.dumps(movie, ensure_ascii=False))
print(type(movie))
print(movie["title"])
print(movie["credits"]["director"])

value = """{
    "title": "Tron: Legacy",
    "composer" : "Daft Punk",
    "release_year" : 2010,
    "budget" : 1700000000,
    "actors" : null,
    "won_oscar" : false
    }"""

tron = json.loads(value)
print(tron)
print(json.dumps(movie))

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "a"
movie2["composer"] = "b"
movie2["actors"] = ["tom", "colin", "samantha", "max"]
movie2["is_awesome"] = True
movie2["budget"] = "12222222"
movie2["cinematographer"] = "Janusz\u01444ski"

file2 = open("c:/work/python/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii = False)
file2.close()












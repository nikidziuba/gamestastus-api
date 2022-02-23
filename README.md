# Gamestatus Unofficial Python API

This Project uses page's django api and makes it easier to use with python functions.
You can find the API page [here](https://gamestatus.info/back/api/gameinfo/game/) 


# Requirements
- Python 3 (Basic python 2 compatibility is implemented but untested)
- json, requests, datetime and platform packages all of which should be installed automatically with Python

# Usage
You can use any of these 4 functions:
- get_by_title()
- search_titles()
- search()
- get_game_info()
       to search for games and get basic info about them.


# Additional info
- I have referred to slugs in the code. This is the name that is used by official API and refers to name of the game in the link. So for example in https://gamestatus.info/far-cry-6 the "far-cry-6" is the slug for Far Cry 6. It can be used e.g. for getting game's page
- I am in no way connected to or affiliated with gamestatus.info page
# License
This package is under MIT License 

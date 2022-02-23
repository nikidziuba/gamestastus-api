import json
import requests
import datetime
from platform import python_version

if python_version().startswith('2'):
    from __future__ import print_function

def get_by_title(title: str):
    '''
    Returns first search result by given title.
    ### Requires:
    ##### title: String that you want to search for
    ### Returns:
    ##### List with title and 'slug' in this format
    ##### ["Title of Game", "title-of-game"]
    '''

    url = 'https://gamestatus.info/back/api/gameinfo/game/search_title/?format=json'

    r = requests.post(
        url,
        data = '{"title":"' + str(title) + '"}',
        headers = {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
        })
    
    res = json.loads(r.text)
    return [res[0]['title'], res[0]['slug']]
    


def search_titles(title: str):
    '''
    Returns multiple search results by given title.
    ### Requires:
    ##### title: String that you want to search for
    ### Returns:
    ##### List with result titles
    ##### ["Title of Game 1", "Title of Game 2"]
   
    '''
    url = 'https://gamestatus.info/back/api/gameinfo/game/search_title/?format=json'

    r = requests.post(
        url,
        data = '{"title":"' + str(title) + '"}',
        headers = {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
        })
    
    res = json.loads(r.text)
    ret_val = []
    for i in res:
        ret_val.append(i['title'])
    return ret_val

def search(title: str):
    '''
    Returns multiple search results by given title.
    ### Requires:
    ##### title: String that you want to search for
    ### Returns:
    ##### List of lists with result titles and slugs:
    ##### [ ["Title of Game 1", "title-of-game-1"], ["Title of Game 2", "title-of-game-2"] ]
   
    '''
    url = 'https://gamestatus.info/back/api/gameinfo/game/search_title/?format=json'

    r = requests.post(
        url,
        data = '{"title":"' + str(title) + '"}',
        headers = {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
        })
    
    res = json.loads(r.text)
    ret_val = []
    for i in res:
        ret_val.append(i['title'])
    return ret_val



def get_game_info(game_slug: str):
    '''
    Returns basic info about a game
    ### Requires:
    ##### game_slug: Slug of the game, use get_by_title(), read docs
    ### Returns:
    ##### Dictionary with basic info from game's page:
    ##### {title: xxx, protections: xxx, release-date: dd-mm-yyyy, released: bool, cracked: bool, crack-date: dd-mm-yyy('' if not cracked), crack_time: days(days from release if not cracked, '' if not released), image: link-to-image, small-image: link-to-image}
    
    '''
    url = 'https://gamestatus.info/back/api/gameinfo/game/' + game_slug + '/?format=json'

    r = requests.get(url)
    res = json.loads(r.text)

    ret_val = {}

    ret_val['title'] = res['title']
    ret_val['protections'] = json.loads(res['protections'])
    
    
    ret_val['release-date'] = datetime.datetime.strptime(res['release_date'], '%Y-%m-%d').strftime("%d-%m-%Y")
    
    
    time = (datetime.date.today() - datetime.datetime.strptime(ret_val['release-date'], '%d-%m-%Y').date()).days
    if time >= 0:
        ret_val['released'] = True
    else:
        ret_val['released'] = False

    if not res['crack_date']:
        ret_val['cracked'] = False
        ret_val['crack-date'] = ''
        
        if time >= 0:
            ret_val['crack_time'] = time
        else:
            ret_val['crack_time'] = ''

    else:
        #Here starts the datetime fuckery. Basically it converts y-m-d to d-m-y (and in the 'crack_time' line uses delta function of date objects then converts it to number of days).
        ret_val['cracked'] = True
        ret_val['crack-date'] = datetime.datetime.strptime(res['crack_date'], '%Y-%m-%d').strftime("%d-%m-%Y") 
        ret_val['crack_time'] = (datetime.date.today() - datetime.datetime.strptime(ret_val['release-date'], '%d-%m-%Y').date()).days
    ret_val['image'] = res['full_image']
    ret_val['small-image'] = res['short_image']

    return ret_val



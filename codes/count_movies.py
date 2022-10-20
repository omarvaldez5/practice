# ============================================================================ #
# START
# ============================================================================ #

"""
Counting movies

Write an HTTP GET method to retrieve information from a movie database concerning
how many movies have a particular string in their title. Given a search term,
query https://jsonmock.hackerrank.com/api/movies/search/?Title=[substr].
The query response will be a JSON object with the following five fields:

* page: The current page.
* per_page: The maximum number of results per page.
* total: The total number of movies having the substring substr in their title.
* total_pages: The total number of pages which must be queried to get all the results.
* data: An array of JSON objects containing movie information where the Title field
denotes the title of the movie

Function Description

Complete the function getNumberOfMovies in the editor below.

getNumberOfMovies has the following parameter(s):
    str substr: the string to search for in the movie database

Returns:
    int: the value of the total field in the returned JSON object
    
Sample Input
STDIN       FUNCTION
maze    --> subtr = 'maze'

Sample Output:
97
"""

import requests

def getNumberOfMovies(substr):
    # Endpoint: https://jsonmock.hackerrank.com/api/movies/search/?Title=substr
    
    # Get response
    url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page="
    response = requests.get(url).json()
    
    # Storage
    pagina = 1
    max_pages_limit = False
    titles = []
    
    # Grab data until limit
    while not max_pages_limit:
        next_url = url + str(pagina)
        info = requests.get(next_url).json()
        
        max_data = info["total_pages"]
        
        if pagina == max_data + 1:
            max_pages_limit = True
        else:
            for movie in info["data"]:
                titles.append(movie["Title"])
            pagina += 1
    
    return len(titles)


print(getNumberOfMovies("maze"))

# ============================================================================ #
# END
# ============================================================================ #

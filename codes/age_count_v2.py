# ============================================================================ #
# START
# ============================================================================ #

"""
Python Age Counting

Question :
In the Python file, write a program to perform a GET request on the route
https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the
value is a string which contains items in the format: key=STRING, age=INTEGER. Your goal
is to count how many items exist that have an age equal to or greater than 50, and print
this final value.

Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2
"""

# Load library
import requests

# Get response
url = "https://coderbyte.com/api/challenges/json/age-counting"
response = requests.get(url)

# Obtain key data & split by comma
df = response.json().get("data").split(",")

# Use specific text to remove information
remove_text = ' age='

# Get age list with for loop & condition
age_list = [
    int(x.replace(remove_text, ''))
    for x in df
    if x.startswith(remove_text) and int(x.replace(remove_text, '')) >= 50
]

# Return output
print("\n")
print("*" * 30)
print(len(age_list))
print("*" * 30)
print("\n")

# ============================================================================ #
# END
# ============================================================================ #


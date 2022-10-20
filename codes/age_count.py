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

# Load data
r = requests.get("https://coderbyte.com/api/challenges/json/age-counting").json()
df = r["data"]

# List split
split_data = df.split(",")

# Obtain ages
age_list = []

for x in range(1, len(split_data), 2):
    age = split_data[x][5:]
    age_list.append(int(age))

# Goal: Count how many items equal or greater than 50
def objective(x):
    return x >= 50

# Iterate over list and return output
print("\n")
print("*" * 30)
print(sum(objective(x) for x in age_list))
print("*" * 30)
print("\n")

# # Another way
# count = 0
# for x in age_list:
#     if x >= 50:
#         count +=1

# print(count)

# ============================================================================ #
# END
# ============================================================================ #

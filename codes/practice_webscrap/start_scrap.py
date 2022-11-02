# ============================================================================ #
# START
# ============================================================================ #

# Library
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Loreum ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p> Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")
print(simple_soup.find("h1"))

h1_tag = simple_soup.find("h1")
print(h1_tag.string)

def find_title():
    h1_tag = simple_soup.find("h1")
    print(h1_tag.string)

find_title()

print("*" * 30)

def find_list_items():
    list_items = simple_soup.find_all("li")
    print(list_items)

find_list_items()


# list items strings
def find_list_items():
    list_items = simple_soup.find_all("li")
    list_contents = [e.string for e in list_items]
    print(list_contents)

print("*" * 30)
find_list_items()


def find_subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"})
    print(paragraph)

print("*" * 30)
find_subtitle()

# Just text subtitle
def find_subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"}).string
    print(paragraph)

print("*" * 30)
find_subtitle()




# ============================================================================ #
# With XPATH

soup_with_xpath = BeautifulSoup(SIMPLE_HTML, "lxml")
def find_xpath_title():
     h1_tag = soup_with_xpath.find("h1").string
     print(h1_tag)

print("*" * 30)
print("With xpath")
find_xpath_title()

def find_xpath_subtitle():
    paragraph = soup_with_xpath.find("//p[@class='subtitle']")
    print(paragraph)

print("*" * 30)
print("With xpath")
find_xpath_subtitle()






# ============================================================================ #
# END
# ============================================================================ #
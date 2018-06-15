import requests, json
from bs4 import BeautifulSoup

result = requests.get("http://en.arguman.org/google-returning-a-page-about-abortion-to-a-search-for-murder-is-valid?view=list")
if result.status_code != 200:
    print("error with connection")
    exit(0)
c = result.content
soup = BeautifulSoup(c, "html.parser")
array = soup.find_all('p')
statements = []
for i in range(len(array)-1):
    if("time-ago" in str(array[i+1])):
        statements.append(str(array[i])[3:-4])
        if "<" in statements[-1] or len(statements[-1]) < 20:
            statements.pop()
        else:
            statements[-1].replace("\"", "")
            statements[-1].replace("'", "")
statements = list(set(statements))
print (json.dumps(statements))
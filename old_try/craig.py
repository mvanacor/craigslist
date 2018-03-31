import requests
r = requests.get('htps://norfolk.craigslist.org')
print(r.status_code)

f = open('test.txt', 'w')
f.write('test output', 'UTF-8')
f.close()

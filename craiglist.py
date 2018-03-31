import requests
from bs4 import BeautifulSoup

print('Starting...')

# Read the list of searches
searchesFile = open('searches.txt', 'r')
searches = searchFiles.readlines()
searchFile.close()

for search in searches:

    # Nintendo search on Norfolk craigslist
    r = requests.get('https://norfolk.craigslist.org/search/sss?query=' + search +'&sort=rel')

    # If the url did not return OK, then assume we failed
    if requests.codes.ok != r.status_code:
        input = input('Error: ' + str(r.status_code))
        exit()

    print('Got the goods...')

    # make some soup
    soup = BeautifulSoup(r.text, 'lxml')

    print('Made some soup...')

    # print the soup to a file
    #f = open('soup.txt', 'w')
    #f.write(soup.prettify())
    #f.close()

    print('Splitting the soup...')

    # Get the list items
    results = soup.find_all("li", class_="result-row".split())
    titles = soup.find_all('a', class_='result-title hdrlnk'.split())
    prices = soup.find_all('', class_='result-price'.split())
    hoods = soup.find_all('span', class_='result-hood')
    datetimes = soup.find_all('time', class_='result-date')

    print ('Number of results: ' + str(len(results)))

    # Get the list of items we've already seen
    processedResultsFile = open('processedresults.txt', r)
    processedResults = processedResults.readlines()
    processedResultsFile.close()

    processedResultsFile = open('processedresults.txt', 'a+')

    # Look through each result we got from Craigslist
    for result in results:

        # Only process results we haven't seen yet
        if result not in processedResults:
            
           

    # print results
    #f = open('listitems.txt', 'w')
    #for result in results:
    #    f.write(str(result['class']) + ' ' + str(result['data-pid']) + '\n')
    #f.close()

    # print titles/links
    #f = open('titles.txt', 'w')
    #for title in titles:
    #    f.write(title.get_text() + ' ' + title['href'] + '\n')
    #f.close()

    #print prices
    #f = open('prices.txt', 'w')
    #for price in prices:
    #    f.write('Price: ' + price.get_text() + '\n')
    #f.close()

    #print hoods
    #f = open('hoods.txt', 'w')
    #for hood in hoods:
    #    f.write('Hood: ' + hood.get_text() + '\n')
    #f.close()

    # print date/time
    #f = open('datetimes.txt', 'w')
    #for datetime in datetimes:
    #    f.write('Datetime: ' + str(datetime['datetime']) + '\n')
    #f.close()

    input = input('Exiting...')

import platform

import requests
from bs4 import BeautifulSoup

import smtplib
from email.mime.text import MIMEText

print('Starting...')

# Read the list of searches
searchFile = open('searches.txt', 'r')
searches = searchFile.readlines()
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
    f = open('soup.txt', 'w')
    if platform.system() is 'Windows':
        print('Platform is Windows')
        f.write(soup.prettify('UTF-8'))
    else:
        print('Platform is Linux')
        f.write(soup.prettify())
    f.close()

    print('Splitting the soup...')

    # Get the list items
    results = soup.find_all("li", class_="result-row".split())
    titles = soup.find_all('a', class_='result-title hdrlnk'.split())
    prices = soup.find_all('', class_='result-price'.split())
    hoods = soup.find_all('span', class_='result-hood')
    datetimes = soup.find_all('time', class_='result-date')

    print ('Number of results: ' + str(len(results)))

    # Get the list of items we've already seen
    processedResultsFile = open('processedresults.txt', 'r')
    processedResults = processedResultsFile.readlines()
    processedResultsFile.close()

    # Open with append
    processedResultsFile = open('processedresults.txt', 'a+')

    # Open file to simulate message
    messages = open('messages.txt', 'w')

    # Iterate through the results
    index = 0
    for result in results:
        if result not in processedResults:
            # Build the message
#            msg = MIMEText('')
#            msg['Subject'] = titles[index].get_text()
#            msg['From'] = 'mattvanaco@gmail.com'
#            msg['To'] = 'mattvanaco@gmail.com'
#            print (titles[index]['href'])
#            print (titles[index].get_text())
            messages.write('Subject: ' + titles[index].get_text() + '\n')
            messages.write('Body: ' + titles[index]['href'] + ' ' + prices[index].get_text() + '\n\n')

            # Add to list of processed
            processedResultsFile.write(str(result['data-pid']) + '\n')

        index = index + 1


# WE DON'T WANT ANYTHING AFTER THIS COMMENT
    # Get new results
    newResults = []
    for result in results:
        if result not in processedResults:
            newResults.append(result)

    # Process new results
    for newResult in newResults:

        # Build email to send
        msg = MIMEText('')

        # Add to list of processed
        processedResultsFile.write(str(newResult['data-pid']) + '\n')

# WE DON'T WANT ANYTHING AFTER THIS COMMENT
    # Look through each result we got from Craigslist
    for result in results:

        # Only process results we haven't seen yet
        if result not in processedResults:
            # print results
            f = open('listitems.txt', 'w')
            for result in results:
                f.write(str(result['data-pid']) + '\n')
            f.close()

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

import requests 
from bs4 import BeautifulSoup


#print('sujay')

for i in range(11,0,-1):

    
    URL = "https://thehub.io/funding?categories=VENTURES&countryCodes=DK&page="+str(i)
    print (URL)


    

    r = requests.get(URL) 

    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    #print(soup.prettify())

    for table in soup.findAll('div', attrs = {'class':'mb-30 col-md-6'}) :
    #print(table.prettify())
    
        link=table.find('a') ['href']
        link='https://thehub.io'+str(link)
        #print(link)
        r_sub = requests.get(link)
        soup_sub = BeautifulSoup(r_sub.content, 'html5lib')
        #print(soup_sub.prettify())
        
        #investor-header
        #investor-header__name
        name=soup_sub.find('h2',attrs={'class':'investor-header__name'}).text
        #print(name)
        
        if (soup_sub.find('a',attrs={'class':'text-blue-900'})):
            website=soup_sub.find('a',attrs={'class':'text-blue-900'}) ['href']
        #print(website)
        
            print (name + ',' + website)
        else:
            print(name+ ', ')

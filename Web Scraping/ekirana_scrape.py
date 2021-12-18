import requests 
from bs4 import BeautifulSoup


URL = "https://www.ekirana.nl/"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
#print(soup.prettify())


table = soup.find('div', attrs = {'class':'nav container clearer'})
#print(table.prettify())

for row in table.findAll('ul'): 
    #print(row.prettify())
    for column in row.findAll('li'):
        
        for link in column.findAll('a')[1:]:
            link_sub=link['href']
            #print(link_sub)
            r_sub = requests.get(link_sub)
            soup_sub = BeautifulSoup(r_sub.content, 'html5lib')
            #print(soup_sub.prettify())
            
            if(soup_sub.find('div',attrs={'class':'category-products'})):
                table_sub=soup_sub.find('div',attrs={'class':'category-products'})
                #print(table_sub.prettify())
                for row_sub in table_sub.findAll('ul'):
                    for column_sub in row_sub.findAll('li'):
                        #print(column_sub.prettify())
                        if (column_sub.find('a', attrs={'class':'product-image'})):
                            prod_name=column_sub.find('a', attrs={'class':'product-image'})
                            name=prod_name['title']
                            name=name.replace(',','-')
                            
                            img=column_sub.find('img')
                            
                            img=img['data-po-cmp-scale-original-src']
                            #print(img)
                            
                            price=column_sub.find('div', attrs={'class':'price-box'}).find('span',attrs={'class':'price'})
                            #print(price.text)
                            
                            print ( str(name) + "," + str(price.text) +","+str(img))
                            
                            
                        else:
                            pass
                        
            else:
                pass

            #for row_sub in table_sub.findAll('ul'):
            #    for column_sub in row_sub.findAll('li'):
             #       print(column_sub.prettify())
                
            
        #project_href = [i['href'] for i in soup.find_all('a', href=True)]
         #   print(project_href)
        
        #print(column.prettify())
         


#print(r.content) 

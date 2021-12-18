import requests 
from bs4 import BeautifulSoup


URL = "https://lahorecashandcarry.com/"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
#print(soup.prettify())


table = soup.find('div', attrs = {'class':'menu-center'})
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
            
            if(soup_sub.find('div',attrs={'class':'archive-products'})):
                table_sub=soup_sub.find('div',attrs={'class':'archive-products'})
                #print(table_sub.prettify())
                for row_sub in table_sub.findAll('ul'):
                    for column_sub in row_sub.findAll('li'):
                        #print(column_sub.prettify())
                        if (column_sub.find('div', attrs={'class':'inner'})):
                            prod_name=column_sub.find('div', attrs={'class':'inner'})
                            
                            img=prod_name.find('img')
                            
                            img=img['src']
                            #print(img)
                            product=column_sub.find('a', attrs={'class':'product-loop-title'})
                            name=product.find('h2').text
                            name=name.replace(',','-')
                            #print(name)
                            
                            #
                            #
                            price=column_sub.find('span', attrs={'class':'price'})
                            #print(price.text)
                            #
                            print ( str(name) + "," + str(price.text) +","+str(img))
                            #print ( name.text + "," + str(price.text) +","+str(img.text))
                            
                            
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

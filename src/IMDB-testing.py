
# importing the module
import imdb
from tabulate import tabulate

# creating instance of IMDb
# ia = imdb.IMDb()
ia = imdb.Cinemagoer()
query_active = True
desired_results = 5

# main loop
while query_active == True:
    
    name = input("\nEnter a name to search: ")
    
    if(name == "q"):
        break
    
    #desired_results = input("Enter the desired search result: ")
    
    # searching the name
    search = ia.search_movie(name,desired_results)
    print("\n%.2f Results for [%s]:\n" % (len(search),name))
    search['cover url'] = ""
    print(tabulate(search,headers='keys',maxcolwidths=7))
    #printing the resultss
    for i in range(len(search)):
        #print(type(search))
        print(search[i]['title'])
        #print(tabulate(search[i]),headers='keys')
        
        #print("Title %5")
        #print("%-*s" % search[i]['title'] )
        headers = ['title','year']
    #print(tabulate(search,headers="keys",tablefmt='fancy_grid'))
    #print(tabulate(search,headers=['title','year'],tablefmt='rst',))
 


    

import imdb
from tabulate import tabulate

# creating instance of IMDb
ia = imdb.Cinemagoer()
query_active = True
desired_results = 5

# main loop
while query_active == True:
    
    name = input("\nEnter a name to search: ")
    
    # exit program loop if 'q' is input
    if(name == "q"):
        break
    
    # collect search results
    search = ia.search_movie(name,desired_results)
    
    # print search results - tabulated 
    print("\n%.2f Results for [%s]:\n" % (len(search),name))
    print(tabulate(search,headers='keys',maxcolwidths=7))

 


    

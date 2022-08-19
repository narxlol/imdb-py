import imdb
import consolemenu
from tabulate import tabulate
from consolemenu import *
from consolemenu.items import *

def search_movie():
    ia = imdb.Cinemagoer()
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter a movie to search: ")
    pu.println("\nYou entered:", result.input_string, "\n")
    name = result.input_string
    movies = ia.search_movie(name,5)
    result_list =[]
    for i in range(0,len(movies)):
       movie_title = movies[i]['title']
       movie_id = movies[i].movieID
       result = [movie_title,movie_id]
       result_list.append(result)
       #print(result)
       
    #    result_list[i].append(movie_title)
    #    result_list[i].append(movie_id)
    headers = ['Movie','ID']
    print(tabulate(result_list,headers)+"\n")
    pu.enter_to_continue()

def search_actor():
    ia = imdb.Cinemagoer()
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an actor/actress to search: ")
    pu.println("\nYou entered:", result.input_string, "\n")
    name = result.input_string
    search = ia.search_person(name,5)
    for i in search:
        print(i)
    print("")
    pu.enter_to_continue()

# main loop
def main():
    
    # creating instance of IMDb
    ia = imdb.Cinemagoer()
    query_active = True
    desired_results = 5
    
    
    # Create the root menu
    menu = ConsoleMenu("IMDB App Menu", "Select option:")
    search_movie_item = FunctionItem("Search a movie", search_movie)
    search_movie_person_item = FunctionItem("Search a person", search_actor)
    
    # add menu items 
    menu.append_item(search_movie_item)
    menu.append_item(search_movie_person_item)
    
    # show the menu
    menu.start()
    menu.join()
    
    #name = input("\nEnter a movie to search: ")
        
    # # exit program loop if 'q' is input
    # if(name == "q"):
    #     break
    # collect search results
    # search = ia.search_movie(name,5)
        
    # # print search results - tabulated 
    # print("\n%.2f Results for [%s]:\n" % (len(search),name))
    # print(tabulate(search,headers='keys',maxcolwidths=7))

 

if __name__ == "__main__":
    main()
    

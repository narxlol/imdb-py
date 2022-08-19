import imdb
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate

def help():
    pu = PromptUtils(Screen())
    print("\n This is the help menu!")
    pu.enter_to_continue
    
def search_movie():
   
    ia = imdb.Cinemagoer()
    
    # PromptUtils.input() returns an InputResult
    pu = PromptUtils(Screen())
    result_list =[]
    
    result = pu.input("\nEnter a movie to search: ")
    pu.println("\nResults for", result.input_string, ":\n")
    name = result.input_string
    movies = ia.search_movie(name,10)
    
    for i in range(0,len(movies)):
       printIndex = i + 1
       movie_title = "%-3d %s" % (printIndex,movies[i]['title'])
       movie_id = movies[i].movieID
       result = [movie_title,movie_id]
       result_list.append(result)

    headers = ['Movie','ID']
    print(tabulate(result_list,headers)+"\n")
    movie_index = pu.input("\nSelect movie number: ")
    print("You selected  " + str(result_list[int(str(movie_index.input_string))-1]))
    pu.enter_to_continue()

def search_actor():
    ia = imdb.Cinemagoer()
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter person to search: ")
    pu.println("\nResults for", result.input_string, ":\n")

    name = result.input_string
    persons = ia.search_person(name,5)
    result_list =[]
    for i in range(0,len(persons)):
       person_name = persons[i]['name']
       person_id = persons[i].personID
       result = [person_name,person_id]
       result_list.append(result)

    headers = ['Person','ID']
    print(tabulate(result_list,headers)+"\n")
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
    help_item = FunctionItem("Search a movie", help)
    search_movie_person_item = FunctionItem("Search a person", search_actor)
    
    # add menu items 
    menu.append_item(search_movie_item)
    menu.append_item(search_movie_person_item)
    menu.append_item(help_item)
    
    # show the menu
    menu.start()
    menu.join()
    
if __name__ == "__main__":
    main()
    

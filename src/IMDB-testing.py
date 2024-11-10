import string
import imdb
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate
from pprint import pprint
import textwrap

global movie_selection
global person_selection
global selection_item
global desired_results


def help():

    print("\nThis is the help menu!")
    input("Press [Enter] to continue ")


def set_movie(movie_id):
    global movie_selection
    movie_selection = movie_id
    print("changed movie selection to " + str(movie_selection) + "!\n")


def get_movie_selection():
    return_movie = movie_selection[0].split()[2:]
    return str(" ".join(return_movie))


def set_person(person_id):
    global person_selection
    person_selection = person_id
    print("changed movie selection to " + str(person_selection) + "!\n")


def get_person_selection():
    return_person = person_selection[0].split()[2:]
    return str(" ".join(return_person))


def set_results(num_of_results):
    global desired_results
    desired_results = num_of_results


def set_results_num():
    global menu

    global submenu_2
    pu = PromptUtils(Screen())
    number_of_results = pu.input(
        "Enter the number of desired search results: ")
    set_results(number_of_results.input_string)
    submenu_2.epilogue_text = "\n Changed desired results to " + str(
        desired_results)
    pu.enter_to_continue
    return desired_results


def get_results_num():
    return desired_results

def get_cast(movie):
    cast = movie.get("cast")
    cast_list = []
    for member in cast:
        name = member.get('name')
        role = member.currentRole
        cast_list.append([name, role])
    
    headers = ['Actor', 'Role']
    print("\nCast:")
    print(tabulate(cast_list, headers, tablefmt="grid"))
    return cast_list
    

def search_movie():
    global ia
    global desired_results
    ia = imdb.Cinemagoer()
    num_of_results = 5

    # PromptUtils.input() returns an InputResult
    pu = PromptUtils(Screen())
    result_list = []

    result = pu.input("\nEnter a movie to search: ")
    pu.println("\nResults for", result.input_string, ":\n")
    name = result.input_string
    movies = ia.search_movie(name, desired_results)

    for i in range(0, len(movies)):
        printIndex = i + 1
        movie_title = "%-3d- %s" % (printIndex, movies[i]['title'])
        movie_id = movies[i].movieID
        result = [movie_title, movie_id]
        result_list.append(result)

    headers = ['Movie', 'ID']
    print(tabulate(result_list, headers) + "\n")
    movie_index = pu.input("\nSelect movie number: ")
    # print("\nYou selected  " +
    #       str(result_list[int(str(movie_index.input_string)) - 1]) + "\n")
    set_movie(result_list[int(str(movie_index.input_string)) - 1])
    menu.epilogue_text = "Movie Selected: " + get_movie_selection()
    menu.epilogue_text += " (" + str(movie_selection[1]) + ")"
    print(movie_selection[1])
    movie = ia.get_movie(movie_selection[1])
    print("\nAvailable movie information fields:")
    info_keys = sorted(movie.keys())
    wrapped_keys = [textwrap.fill(k, width=40) for k in info_keys]
    print(tabulate([wrapped_keys[i:i+4] for i in range(0, len(wrapped_keys), 4)], 
                   tablefmt="grid"))
    
    query = ""
    while query != "q":
        query = pu.input("\nEnter field to query (q to quit): ").input_string
 
        if query == "q":
            break
        
        if query not in movie.keys():
            print(f"\nError: '{query}' is not a valid field")
            continue
            
        results = movie.get(query)
        print(f"\nResults for '{query}':")
        
        if isinstance(results, (list, tuple)):
            if all(isinstance(x, (str, int, float)) for x in results):
                print(tabulate([[x] for x in results], tablefmt="grid"))
            else:
                pprint(results, width=80, indent=2)
        else:
            print(textwrap.fill(str(results), width=80))
            
        print("\n")
    
    print(get_cast(movie))
    pu.enter_to_continue()



def get_person_list(person_list):
    result_list = []
    for person in person_list:
        person_name = person[0]
        person_id = person[1]
        
    result = [person_name, person_id]
    # for i in range(0, len(person_list)):
    #     printIndex = i + 1
    #     person_name = "%-3d- %s" % (printIndex, person_list[i]['name'])
    #     person_id = person[i].personID
    #     result = [person_name, person_id]
    #     result_list.append(result)
    #     headers = ['Person', 'ID']
    #     print(tabulate(result_list, headers) + "\n")
    

def search_actor():
    ia = imdb.Cinemagoer()
    num_of_results = 5

    # PromptUtils.input() returns an InputResult
    pu = PromptUtils(Screen())
    result_list = []

    result = pu.input("\nEnter an person to search: ")
    pu.println("\nResults for", result.input_string, ":\n")
    name = result.input_string
    person = ia.search_person(name, desired_results)

    for i in range(0, len(person)):
        printIndex = i + 1
        person_name = "%-3d- %s" % (printIndex, person[i]['name'])
        person_id = person[i].personID
        result = [person_name, person_id]
        result_list.append(result)

    headers = ['Person', 'ID']
    print(tabulate(result_list, headers) + "\n")
    person_index = pu.input("\nSelect person number: ")
    print("\nYou selected  " +
          str(result_list[int(str(person_index.input_string)) - 1]) + "\n")
    set_person(result_list[int(str(person_index.input_string)) - 1])
    menu.epilogue_text = "Person Selected: " + get_person_selection()
    pu.enter_to_continue()


# main loop
def main():
    # declaring globals
    global menu
    global movie_selection
    global person_selection
    global submenu_2
    global desired_results
    global ia

    # set initial selection states
    movie_selection = ""
    actor_selection = ""
    desired_results = 5

    # creating instance of IMDb
    ia = imdb.Cinemagoer()

    # Create the root menu
    menu = ConsoleMenu("IMDB App Menu", "Select an option:")
    search_movie_item = FunctionItem("Search a movie", search_movie)
    help_item = FunctionItem("Help menu", help)
    search_movie_person_item = FunctionItem("Search a person", search_actor)

    # Create a second submenu, but this time use a standard ConsoleMenu instance
    submenu_2 = ConsoleMenu("Settings Menue", "Select a setting to change.")
    item2 = FunctionItem("Set results width", set_results_num)
    submenu_2.append_item(item2)
    submenu_item_2 = SubmenuItem("Settings", submenu=submenu_2)
    submenu_item_2.set_menu(menu)

    # add menu items
    menu.append_item(search_movie_item)
    menu.append_item(search_movie_person_item)
    menu.append_item(help_item)
    menu.append_item(submenu_item_2)

    # show the menu
    menu.start()
    menu.join()
    
    pu = PromptUtils(Screen())
    


if __name__ == "__main__":
    main()

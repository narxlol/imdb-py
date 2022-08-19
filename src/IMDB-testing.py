from asyncio.windows_events import NULL
import imdb
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate

global movie_selection
global actor_selection
global selection_item
def help():

    print("\nThis is the help menu!")
    input("Press [Enter] to continue ")


def set_movie(movie_id):
    global movie_selection
    movie_selection = movie_id
    print("changed movie selection to " + str(movie_selection) + "!\n")

def get_movie_selection():
    return str(movie_selection)

def search_movie():

    ia = imdb.Cinemagoer()
    num_of_results = 5

    # PromptUtils.input() returns an InputResult
    pu = PromptUtils(Screen())
    result_list = []

    result = pu.input("\nEnter a movie to search: ")
    pu.println("\nResults for", result.input_string, ":\n")
    name = result.input_string
    movies = ia.search_movie(name, num_of_results)

    for i in range(0, len(movies)):
        printIndex = i + 1
        movie_title = "%-3d %s" % (printIndex, movies[i]['title'])
        movie_id = movies[i].movieID
        result = [movie_title, movie_id]
        result_list.append(result)

    headers = ['Movie', 'ID']
    print(tabulate(result_list, headers) + "\n")
    movie_index = pu.input("\nSelect movie number: ")
    print("\nYou selected  " +
          str(result_list[int(str(movie_index.input_string)) - 1]) + "\n")
    set_movie(result_list[int(str(movie_index.input_string))-1])
    selection_item = MenuItem(str(result_list[int(str(movie_index.input_string))-1]))
    menu.epilogue_text = "Movie Selected: " + get_movie_selection()
    print("movie selection: " + str(movie_selection))
    pu.enter_to_continue()


def search_actor():
    ia = imdb.Cinemagoer()
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter person to search: ")
    pu.println("\nResults for", result.input_string, ":\n")

    name = result.input_string
    persons = ia.search_person(name, 5)
    result_list = []
    for i in range(0, len(persons)):
        person_name = persons[i]['name']
        person_id = persons[i].personID
        result = [person_name, person_id]
        result_list.append(result)

    headers = ['Person', 'ID']
    print(tabulate(result_list, headers) + "\n")
    pu.enter_to_continue()


# main loop
def main():
    global menu
    global movie_selection
    global actor_selection
    global selection_item
    selection_item = MenuItem("(Nothing selected)")
    movie_selection = "N/A"
    # creating instance of IMDb
    ia = imdb.Cinemagoer()
    query_active = True
    desired_results = 5

    # Create the root menu
    menu = ConsoleMenu("IMDB App Menu", "Select option:")
    search_movie_item = FunctionItem("Search a movie", search_movie)
    help_item = FunctionItem("Help menu", help)
    search_movie_person_item = FunctionItem("Search a person", search_actor)

    # add menu items
    menu.append_item(search_movie_item)
    menu.append_item(search_movie_person_item)
    #menu.(selection_item)
    menu.append_item(help_item)

    # show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()

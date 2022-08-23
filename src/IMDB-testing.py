import string
import imdb
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate

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


def search_movie():
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
    print("\nYou selected  " +
          str(result_list[int(str(movie_index.input_string)) - 1]) + "\n")
    set_movie(result_list[int(str(movie_index.input_string)) - 1])
    menu.epilogue_text = "Movie Selected: " + get_movie_selection()
    menu.epilogue_text += " (" + str(movie_selection[1]) + ")"
    pu.enter_to_continue()


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

    # set initial selection states
    movie_selection = ""
    actor_selection = ""
    desired_results = 5

    # creating instance of IMDb
    ia = imdb.Cinemagoer()

    # Create the root menu
    menu = ConsoleMenu("IMDB App Menu", "Select option:")
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


if __name__ == "__main__":
    main()

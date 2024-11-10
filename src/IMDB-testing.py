from movie_manager import MovieManager
from person_manager import PersonManager
from menu_manager import MenuManager

def main():
    movie_manager = MovieManager()
    person_manager = PersonManager()
    menu_manager = MenuManager(movie_manager, person_manager)
    menu_manager.start()

if __name__ == "__main__":
    main()

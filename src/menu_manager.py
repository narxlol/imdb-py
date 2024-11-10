from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem
from consolemenu.screen import Screen
from consolemenu.prompt_utils import PromptUtils

class MenuManager:
    def __init__(self, movie_manager, person_manager):
        self.movie_manager = movie_manager
        self.person_manager = person_manager
        self.desired_results = 5
        self.menu = None
        self.settings_menu = None
        
    def setup_menus(self):
        # Create main menu
        self.menu = ConsoleMenu("IMDB App Menu", "Select an option:")
        
        # Create menu items
        search_movie_item = FunctionItem("Search a movie", self.search_movie_handler)
        search_person_item = FunctionItem("Search a person", self.search_person_handler)
        help_item = FunctionItem("Help menu", self.show_help)
        
        # Create settings submenu
        self.settings_menu = ConsoleMenu("Settings Menu", "Select a setting to change.")
        results_item = FunctionItem("Set results width", self.set_results_num)
        self.settings_menu.append_item(results_item)
        settings_submenu = SubmenuItem("Settings", submenu=self.settings_menu)
        settings_submenu.set_menu(self.menu)
        
        # Add items to main menu
        self.menu.append_item(search_movie_item)
        self.menu.append_item(search_person_item)
        self.menu.append_item(help_item)
        self.menu.append_item(settings_submenu)
        
    def search_movie_handler(self):
        selected = self.movie_manager.search_movie(self.desired_results)
        movie = self.movie_manager.get_movie_details(selected[1])
        self.movie_manager.show_movie_info(movie)
        self.movie_manager.get_cast(movie)
        self.menu.epilogue_text = f"Movie Selected: {self.movie_manager.get_selection_title()} ({selected[1]})"
        PromptUtils(Screen()).enter_to_continue()
        
    def search_person_handler(self):
        selected = self.person_manager.search_person(self.desired_results)
        self.menu.epilogue_text = f"Person Selected: {self.person_manager.get_selection_name()}"
        PromptUtils(Screen()).enter_to_continue()
        
    def set_results_num(self):
        pu = PromptUtils(Screen())
        number = pu.input("Enter the number of desired search results: ")
        self.desired_results = int(number.input_string)
        self.settings_menu.epilogue_text = f"\nChanged desired results to {self.desired_results}"
        pu.enter_to_continue()
        
    def show_help(self):
        print("\nThis is the help menu!")
        input("Press [Enter] to continue ")
        
    def start(self):
        self.setup_menus()
        self.menu.start()
        self.menu.join()

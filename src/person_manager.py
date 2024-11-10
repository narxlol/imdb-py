import imdb
from tabulate import tabulate
from consolemenu.screen import Screen
from consolemenu.prompt_utils import PromptUtils

class PersonManager:
    def __init__(self):
        self.ia = imdb.Cinemagoer()
        self.person_selection = None
        
    def search_person(self, desired_results=5):
        pu = PromptUtils(Screen())
        result_list = []

        result = pu.input("\nEnter a person to search: ")
        pu.println("\nResults for", result.input_string, ":\n")
        persons = self.ia.search_person(result.input_string, desired_results)

        for i, person in enumerate(persons, 1):
            person_name = f"{i:3d}- {person['name']}"
            person_id = person.personID
            result_list.append([person_name, person_id])

        headers = ['Person', 'ID']
        print(tabulate(result_list, headers) + "\n")
        
        person_index = pu.input("\nSelect person number: ")
        selected = result_list[int(person_index.input_string) - 1]
        self.person_selection = selected
        
        print("\nYou selected", selected[0], "\n")
        return selected
        
    def get_selection_name(self):
        if self.person_selection:
            name = self.person_selection[0].split()[2:]
            return " ".join(name)
        return None

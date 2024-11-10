import imdb
from tabulate import tabulate
from pprint import pprint
import textwrap
from consolemenu.screen import Screen
from consolemenu.prompt_utils import PromptUtils

class MovieManager:
    def __init__(self):
        self.ia = imdb.Cinemagoer()
        self.current_movie = None
        self.movie_selection = None
        
    def search_movie(self, desired_results=5):
        pu = PromptUtils(Screen())
        result_list = []

        result = pu.input("\nEnter a movie to search: ")
        pu.println("\nResults for", result.input_string, ":\n")
        movies = self.ia.search_movie(result.input_string, desired_results)

        for i, movie in enumerate(movies, 1):
            movie_title = f"{i:3d}- {movie['title']}"
            movie_id = movie.movieID
            result_list.append([movie_title, movie_id])

        headers = ['Movie', 'ID']
        print(tabulate(result_list, headers) + "\n")
        
        movie_index = pu.input("\nSelect movie number: ")
        selected = result_list[int(movie_index.input_string) - 1]
        self.movie_selection = selected
        
        return selected
        
    def get_movie_details(self, movie_id):
        movie = self.ia.get_movie(movie_id)
        self.current_movie = movie
        return movie
        
    def show_movie_info(self, movie):
        print("\nAvailable movie information fields:")
        info_keys = sorted(movie.keys())
        wrapped_keys = [textwrap.fill(k, width=40) for k in info_keys]
        print(tabulate([wrapped_keys[i:i+4] for i in range(0, len(wrapped_keys), 4)], 
                      tablefmt="grid"))
        
        pu = PromptUtils(Screen())
        while True:
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
            
    def get_cast(self, movie):
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
        
    def get_selection_title(self):
        if self.movie_selection:
            title = self.movie_selection[0].split()[2:]
            return " ".join(title)
        return None

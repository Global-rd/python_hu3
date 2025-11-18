import requests

class RickMortyExtractor:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"


    def get_data(self, endpoint, params):
        
        data = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            print(url)
            response = requests.get(url, params=params)
            if response.status_code == 200:
                curr_page_response = response.json()
                data.extend(curr_page_response["results"])
                url = curr_page_response["info"]["next"]
            else:
                print(f"Error: {response.status_code}: {response.text}")
        return data

    def get_characters(self, name=None,
                             status=None, 
                             species=None,
                             type=None,
                             gender=None):
        
        params = {"name": name,
                  "status": status,
                  "species": species,
                  "type": type,
                  "gender": gender
                  }
        
        return self.get_data("character", params)
        
    def get_locations(self, name=None, type=None, dimension=None):

        params = {"name": name,
                  "type": type,
                  "dimension": dimension
                  }
        
        return self.get_data("location", params)
        
    def get_episodes(self, name=None, episode=None):

        params = {"name": name,
                  "episode": episode
                  }
        
        return self.get_data("episode", params)
        
api = RickMortyExtractor()

#characters = api.get_characters()
episodes = api.get_episodes()
print(len(episodes))



import http.client
import json
import os.path
from api_key import API_KEY

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
}


class WorldLeagues:
    def __init__(self):
        self.leagues = []
        self.data_dir = os.path.join(os.path.dirname(__file__), "data")
        self.leagues_file = os.path.join(self.data_dir, "leagues.json")
        self.leagues_simplified = os.path.join(self.data_dir, "leagues_simplified.json")
        self.seasons_simplified = os.path.join(self.data_dir, "seasons_simplified.json")

    def _parse(self, league_id=None, league_name=None):
        """
        Check if the league is already in the cache
        If not in cache, check the JSON file
        :param league_id: e.g. 39
        :param league_name: e.g. Bundesliga
        :return: dict
        """
        if self.leagues:
            print("Using cached leagues data")
            for lg in self.leagues:
                if (league_id and lg.id == league_id) or (league_name and lg.name == league_name):
                    return lg

        if os.path.isfile(self.leagues_file):
            print(f"Using leagues data from file: {self.leagues_file}")
            with open(self.leagues_file, "r") as leagues_json_f:
                leagues_data = json.load(leagues_json_f)
            self._simplify(leagues_data)

            for league_data in leagues_data["response"]:
                if (league_id and league_data["league"]["id"] == league_id) or (league_name and league_data["league"]["name"] == league_name):
                    return league_data
            return {}
        else:
            print(f"Fetching leagues data from URL {headers['x-rapidapi-host']}...")
            return self._request()

    def _simplify(self, leagues_data):
        """
        Leave only important information
        :param leagues_data:
        :return:
        """
        simplified_leagues = []
        print(f"Fetched {len(leagues_data)} leagues")

        # Create a list of simplified leagues
        for lg in leagues_data["response"]:
            simplified_leagues.append({
                "id": lg["league"]["id"],
                "name": lg["league"]["name"],
                "country": lg["country"]["name"],
                "seasons": [season["year"] for season in lg["seasons"]],
            })

        with open(self.leagues_simplified, "w") as leagues_json_f:
            json.dump(self.leagues, leagues_json_f, indent=4)

        # Create a list of simplified seasons
        seasons = []
        for lg in leagues_data["response"]:
            for season in lg["seasons"]:
                seasons.append({
                    "league_id": lg["league"]["id"],
                    "league_name": lg["league"]["name"],
                    "country": lg["country"]["name"],
                    "year": season["year"],
                    "start": season["start"],
                    "end": season["end"]
                })
        with open(self.seasons_simplified, "w") as seasons_json_f:
            json.dump(seasons, seasons_json_f, indent=4)

    def _request(self):
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        endpoint = "/leagues"
        conn.request("GET", endpoint, headers=headers)
        result = conn.getresponse()
        result_data = result.read()
        leagues_data = json.loads(result_data)

        # Check for API errors
        if "errors" in leagues_data:
            raise Exception(f"API Error: {leagues_data['errors']}")

        # Cache the data
        with open(self.leagues_file, "w") as leagues_json_f:
            json.dump(leagues_data, leagues_json_f, indent=4)

        # Simplify the data for easier use in data analysis
        self._simplify(leagues_data)

        return leagues_data

    def by_id(self, league_id):
        return self._parse(league_id=league_id)

    def by_name(self, league_name):
        return self._parse(league_name=league_name)

    def all(self):
        leagues_data = self._parse()
        return leagues_data["response"]


class League:
    def __init__(self, data):
        self.id = data["league"]["id"]
        self.name = data["league"]["name"]
        self.country = data["country"]["name"]
        self.seasons = [season["year"] for season in data["seasons"]]
        self.players = []


# Usage example
world = WorldLeagues()
league_by_id = world.by_id(4)

if league_by_id:
    print(f"League found by ID: {league_by_id}")

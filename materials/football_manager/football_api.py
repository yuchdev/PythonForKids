# Open Football API client
import http.client
import json
import os.path
import sys
import argparse

try:
    import xlwings as xw
except Exception:
    print("Unable to import xlwings")

API_KEY = "41b899db8a2f3aaef64f44f30d7ac6b2"

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
}


class Leagues:
    """
    Class for fetching, caching and parsing leagues data
    """

    def __init__(self):
        self.leagues = []
        self.endpoint = "/leagues"
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    def fetch(self):
        """
        Fetch leagues result data from API
        """
        self.conn.request("GET", self.endpoint, headers=headers)
        result = self.conn.getresponse()
        result_data = result.read()

        leagues = json.loads(result_data)
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        with open(os.path.join(data_dir, "leagues_cache.json"), "w") as leagues_json_f:
            json.dump(leagues, leagues_json_f, indent=4)

    def parse(self):
        """
        Parse out important information from league result data and save to file
        [results][][league][id]
        [results][][league][name]
        [results][][country][name]
        [results][][seasons][][year]
        """
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.isfile(os.path.join(data_dir, "leagues_cache.json")):
            print("Fetching leagues data...")
            self.fetch()
        with open(os.path.join(data_dir, "leagues_cache.json"), "r") as leagues_json_f:
            leagues = json.load(leagues_json_f)
        print(f"Fetched {len(self.leagues)} leagues")
        for league in leagues["response"]:
            self.leagues.append({
                "id": league["league"]["id"],
                "name": league["league"]["name"],
                "country": league["country"]["name"],
                "seasons": [season["year"] for season in league["seasons"]],
            })

        with open(os.path.join(data_dir, "leagues.json"), "w") as leagues_json_f:
            json.dump(self.leagues, leagues_json_f, indent=4)

    def to_excel(self):
        """
        Write leagues data to Excel file
        """
        wb = xw.Book()
        ws = wb.sheets["Sheet1"]
        ws.range("A1").value = "ID"
        ws.range("B1").value = "Name"
        ws.range("C1").value = "Country"
        ws.range("D1").value = "Seasons"
        for i, league in enumerate(self.leagues):
            print(f"Writing league {league['name']}: {i + 1} of {len(self.leagues)}")
            ws.range(f"A{i + 2}").value = league["id"]
            ws.range(f"B{i + 2}").value = league["name"]
            ws.range(f"C{i + 2}").value = league["country"]
            ws.range(f"D{i + 2}").value = ", ".join([str(season) for season in league["seasons"]])
        wb.save("Leagues.xlsx")


class Players:
    """
    Class for fetching, caching and parsing players data
    """

    def __init__(self, league_id, season):
        self.players = None
        self.league_id = league_id
        self.endpoint = f"/players?league={league_id}&season={season}"
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        self.pages = None

    def exit_on_error(self, response, players):
        """
        exit app if response["errors"] list is not empty
        """
        if len(response["errors"]):
            print("Errors:")
            data_dir = os.path.join(os.path.dirname(__file__), "data")
            with open(os.path.join(data_dir, f"players_cache_{self.league_id}.json"), "w") as players_json_f:
                json.dump(players, players_json_f, indent=4)
            for error in response["errors"]:
                print(error)
                print("Exiting app...")
            sys.exit(1)

    def fetch(self):
        """
        Fetch players result data from API
        """
        if os.path.isfile(f"data/players_cache_{self.league_id}.json"):
            print("Players cache file exists, skipping fetch...")
            return
        self.conn.request("GET", self.endpoint, headers=headers)
        result = self.conn.getresponse()
        result_data = result.read()

        players = json.loads(result_data)
        self.exit_on_error(players, players)
        self.pages = players["paging"]["total"]
        for page_id in range(2, self.pages + 1):
            print(f"Fetching page {page_id} of {self.pages}")
            paging_endpoint = self.endpoint + f"&page={page_id}"
            self.conn.request("GET", paging_endpoint, headers=headers)
            result = self.conn.getresponse()
            result_data = result.read()
            result_json = json.loads(result_data)
            self.exit_on_error(result_json, players)
            players["response"].extend(result_json["response"])

        data_dir = os.path.join(os.path.dirname(__file__), "data")
        with open(os.path.join(data_dir, f"players_cache_{self.league_id}.json"), "w") as players_json_f:
            json.dump(players, players_json_f, indent=4)

    def parse(self):
        """
        Parse out important information from player result data and save to file
        [response][][player][id]
        [response][][player][firstname]
        [response][][player][lastname]
        [response][][player][age]
        [response][][statistics][team][name]
        [response][][statistics][league][name]
        [response][][statistics][games][position]
        [response][][statistics][goals][total]
        [response][][statistics][goals][conceded]
        [response][][statistics][penalty][scored]
        """
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.isfile(os.path.join(data_dir, f"players_cache_{self.league_id}.json")):
            self.fetch()
        with open(os.path.join(data_dir, f"players_cache_{self.league_id}.json"), "r") as players_json_f:
            players = json.load(players_json_f)
        self.players = []
        if not isinstance(players["response"], list):
            return
        for player in players["response"]:
            self.players.append({
                "id": player["player"]["id"],
                "firstname": player["player"]["firstname"],
                "lastname": player["player"]["lastname"],
                "age": player["player"]["age"],
                "team": player["statistics"][0]["team"]["name"],
                "league": player["statistics"][0]["league"]["name"],
                "position": player["statistics"][0]["games"]["position"],
                "goals": player["statistics"][0]["goals"]["total"],
                "conceded": player["statistics"][0]["goals"]["conceded"],
                "penalty": player["statistics"][0]["penalty"]["scored"],
            })

        with open(os.path.join(data_dir, f"players_{self.league_id}.json"), "w") as players_json_f:
            json.dump(self.players, players_json_f, indent=4, ensure_ascii=True)


def main():
    """
    Main function
    :return: system exit code
    """
    parser = argparse.ArgumentParser(description='Command-list_str interface')
    parser.add_argument('--players-all-leagues',
                        help='Fetch all players from all leagues',
                        action='store_true',
                        required=False)
    parser.add_argument('--all-leagues',
                        help='Fetch all leagues',
                        action='store_true',
                        required=False)
    parser.add_argument('--league-id',
                        help='ID of the league to fetch players from',
                        default="",
                        required=False)

    args = parser.parse_args()

    if args.all_leagues:
        leagues = Leagues()
        leagues.parse()

    if args.players_all_leagues:
        leagues = Leagues()
        leagues.parse()
        for league in leagues.leagues:
            players = Players(league["id"], 2020)
            players.parse()

    if args.league_id:
        players = Players(args.league_id, 2020)
        players.parse()

    return 0


if __name__ == '__main__':
    sys.exit(main())

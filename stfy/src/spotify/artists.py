import requests
from src.spotify.base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Artists:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_artist(self, id: str):
        response = requests.get(
            self.base_url + "/artists/" + id,
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_several_artists(self, ids: str):
        response = requests.get(
            self.base_url + "/artists",
            headers=self.headers,
            params={
                "ids": ids,
            }
        )
        # print(self.headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_artist_albums(self, id: str, limit: int, country_code="US"):
        response = requests.get(
            self.base_url + "/artists/" + id + "/albums",
            headers=self.headers,
            params={
                "limit": limit,
                "market": country_code
            }
        )
        # print(self.headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_artist_top_tracks(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/artists/" + id + "/top-tracks",
            headers=self.headers,
            params={
                "market": country_code
            }
        )
        # print(self.headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_airtist_related_artists(self, id):
        response = requests.get(
            self.base_url + "/artists/" + id + "/related-artists",
            headers=self.headers
        )
        # print(self.headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Remove/comment out these test calls
# Artists().get_artist("1ukmGETCwXTbgrTrkRDnmn")
# Artists().get_several_artists("1ukmGETCwXTbgrTrkRDnmn,40wyqBgeUtnE26B5P4ajSJ")
# Artists().get_artist_albums("1ukmGETCwXTbgrTrkRDnmn", 4)
# Artists().get_artist_top_tracks("1ukmGETCwXTbgrTrkRDnmn")
# Artists().get_airtist_related_artists("1ukmGETCwXTbgrTrkRDnmn")

import requests
from PubgPlayer import PubgPlayer
from PubgMatch import PubgMatch
from PubgMatchTelemetry import PubgMatchTelemetry
import apiKey


class PubgApi():
        def __init__(self):
		self.header = apiKey.getApiHeader()

	def getPlayerFromString(self, playerName):
                response = requests.get("https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]=" + str(playerName), headers=self.header)
                if response.ok:
                        return PubgPlayer(response.json()["data"][0])
                else:
                        return False

	def getPlayerFromId(self, playerId):
                response = requests.get("https://api.playbattlegrounds.com/shards/pc-na/players/" + str(playerId), headers=self.header)
                if response.ok:
                        return PubgPlayer(response.json()['data'])
                else:
                        return False
        
	def getMatch(self, matchId, player):
                response = requests.get("https://api.playbattlegrounds.com/shards/pc-na/matches/" + str(matchId), headers=self.header)
                if response.ok:
                        return PubgMatch(response.json(), player)
                else:
                        return False

        def getMatchTelemetry(self, telemetryUrl):
                return PubgMatchTelemetry(requests.get(str(telemetryUrl), headers=self.header).json())

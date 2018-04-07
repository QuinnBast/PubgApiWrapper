import requests
from PubgPlayer import PubgPlayer
from PubgMatch import PubgMatch
from PubgMatchTelemetry import PubgMatchTelemetry
import apiKey


class PubgApi():
        def __init__(self):
		self.header = apiKey.getApiHeader()

	def getPlayerFromString(self, playerName):
		return PubgPlayer(requests.get("https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]=" + str(playerName), headers=self.header).json()["data"][0])

	def getPlayerFromId(self, playerId):
                return PubgPlayer(requests.get("https://api.playbattlegrounds.com/shards/pc-na/players/" + str(playerId), headers=self.header).json()["data"][0])
        
	def getMatch(self, matchId, player):
                return PubgMatch(requests.get("https://api.playbattlegrounds.com/shards/pc-na/matches/" + str(matchId), headers=self.header).json(), player)

        def getMatchTelemetry(self, telemetryUrl):
                return PubgMatchTelemetry(requests.get(str(telemetryUrl), headers=self.header).json())

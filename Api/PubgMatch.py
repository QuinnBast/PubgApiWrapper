from PubgPlayerMatchData import PubgPlayerMatchData
import PubgApi

class PubgMatch():
        def __init__(self, jsonData, player):
                self.data = jsonData["data"]
                self.included = jsonData['included']
                self.player = player
                
        def getGameMode(self):
                return str(self.data['attributes']['gameMode'])
        
        def getMapName(self):
                return str(self.data['attributes']['mapName'])
        
        def getMatchPlayerDict(self):
                players = []
                for obj in self.included:
                        if str(obj['type']) != "participant":
                                continue;
                        
                        #We now have each player in the match.
                        player = [{'id': obj['attributes']['stats']['playerId'], 'name': obj['attributes']['stats']['name']}]
                        if (player is not False):
                                players += player
                return players

#ToDO
        #def getTeamMembers(pubgPlayer):
                #players = []
                #for obj in self.included:
                        #if str(obj['type']) != "roster":
                                #continue;
#                        
                        ##We now have each roster in the match.
                        #for player in obj['relationsihps']['participants']
                                #if(player['data'][0][
                                #player = PubgApi().getPlayerFromId(player['data'][0]['id'])
                                #players += [player]
                #return players

        def getPlayerData(self):
                for obj in self.included:
                        if (str(obj['type']) != "participant"):
                                continue;
                        
                        #We have all participants.
                        if str(obj['attributes']['stats']['playerId']) == self.player.getPlayerId():
                                return PubgPlayerMatchData(obj['attributes']['stats'])

        def getTelemetry(self):
                for obj in self.included:
                        if (str(obj['type']) != "asset"):
                                continue;
                        
                        if obj['attributes']['name'] == "telemetry":
                                return PubgApi.PubgApi().getMatchTelemetry(str(obj['attributes']['URL']))

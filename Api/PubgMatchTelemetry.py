import sys
sys.path.append('Models/')
import PubgBlueZoneModel

class PubgMatchTelemetry():
        def __init__(self, jsonData):
                self.data = jsonData

        #The map location ranges from 0 to 816,000
        #0,0,0 is the bottom left.
        
        def getMatchStart(self):
                for i in range(0, len(self.data)):
                        if self.data[i]['_T'] == "LogMatchStart":
                                break;

        def getBlueZone(self):
                blueZone = []
                #Check if this game was already logged
                model = PubgBlueZoneModel.PubgBlueZoneModel().alias()
                model = model.select().where(model.gameId == self.data[0]['MatchId'])
                if len(list(model)) > 0:
                        return
                
                for i in range(0, len(self.data)):
                        if self.data[i]['_T'] == "LogGameStatePeriodic":
                                if len(blueZone) is 0 or blueZone[len(blueZone)-1] != str(self.data[i]['gameState']['poisonGasWarningRadius']):
                                        
                                        model = PubgBlueZoneModel.PubgBlueZoneModel(x=str(self.data[i]['gameState']['poisonGasWarningPosition']['x']),y=str(self.data[i]['gameState']['poisonGasWarningPosition']['y']),z=str(self.data[i]['gameState']['poisonGasWarningPosition']['z']),radius=str(self.data[i]['gameState']['poisonGasWarningRadius']),mapName=str(self.data[i]['common']['mapName']), gameId=self.data[i]['common']['matchId'])
                                        if model.x != 0 or model.y != 0:
                                                model.save(force_insert = True)
                                                blueZone += [str(self.data[i]['gameState']['poisonGasWarningRadius'])]

        def getWinningDropLocation(self):
                #Get the winning player
                for i in range(0, len(self.data)):
                        if self.data[i]['_T'] == "LogMatchEnd":
                                for c in self.data[i]['characters']:
                                        if str(c['ranking']) == "1":
                                                winningPlayer = str(c['name'])
                                                break;

                #Get the drop location
                for i in range(0, len(self.data)):
                        if self.data[i]['_T'] == "LogItemUnequip" and self.data[i]['item']['itemId'] == "Item_Back_B_01_StartParachutePack_C" and str(self.data[i]['character']['name']) == winningPlayer:
                                print("x: " + str(self.data[i]['character']['location']['x']) + " y: " + str(self.data[i]['character']['location']['y']) + " z: " + str(self.data[i]['character']['location']['z']))                               

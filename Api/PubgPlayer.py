class PubgPlayer():
        def __init__(self, jsonData):
                self.matches = []
                self.data = jsonData
                for match in self.data['relationships']['matches']['data']:
                        self.matches += [str(match['id'])]
        
        def getPlayerName(self):
                return str(self.data['attributes']['name'])

        def getPlayerId(self):
                return str(self.data['id'].split('.')[1])

        def getPlayerMatches(self):
                return self.matches

        def getMatch(self, matchIndex):
                from PubgApi import PubgApi
                return PubgApi().getMatch(str(self.matches[matchIndex]), self)

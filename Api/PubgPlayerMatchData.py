class PubgPlayerMatchData():
        def __init__(self, jsonData):
                self.data = jsonData

        def getPlayerName(self):
                return str(self.data['name'])

        def getDBNO(self):
                return str(self.data['DBNO'])

        def getAssists(self):
                return str(self.data['assists'])

        def getBoostsUsed(self):
                return str(self.data['boosts'])

        def getDamageDealt(self):
                return str(self.data['damageDealt'])

        def getDeathType(self):
                return str(self.data['deathType'])

        def getHeadshotKills(self):
                return str(self.data['headshotKills'])

        def getHeals(self):
                return str(self.data['heals'])

        def getKillRank(self):
                return str(self.data['killPlace'])

        def getKillPoints(self):
                return str(self.data['killPoints'])

        def getKillPointsDelta(self):
                return str(self.data['killPointsDelta'])

        def getKillstreaks(self):
                return str(self.data['killstreaks'])

        def getKills(self):
                return str(self.data['kills'])

        def getLongestKill(self):
                return str(self.data['longestKill'])

        def getMostDamage(self):
                return str(self.data['mostDamage'])

        def getPlayerId(self):
                return str(self.data['playerId'])

        def getRevives(self):
                return str(self.data['revives'])

        def getVehicleDistance(self):
                return str(self.data['rideDistance'])

        def getRoadKills(self):
                return str(self.data['roadKills'])

        def getTeamKills(self):
                return str(self.data['teamKills'])

        def getTimeSurvived(self):
                return str(self.data['timeSurvived'])

        def getVehiclesDestroyed(self):
                return str(self.data['vehicleDestroys'])

        def getWalkDistance(self):
                return str(self.data['walkDistance'])

        def getWeaponsAcquired(self):
                return str(self.data['weaponsAcquired'])

        def getWinRank(self):
                return str(self.data['winPlace'])

        def getWinRating(self):
                return str(self.data['winPoints'])

        def getWinRatingDelta(self):
                return str(self.data['winPointsDelta'])
        

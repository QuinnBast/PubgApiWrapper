import sys
sys.path.append('Api/')
from PubgApi import PubgApi

player = PubgApi().getPlayerFromString("R10t--")
print("Player Name: " + player.getPlayerName())
print("Player Id: " + player.getPlayerId())

players = player.getMatch(0).getMatchPlayerDict()
for p in players:
    print("id: " + str(p['id']) + " name: " + str(p['name']))
print("Players: " + str(len(players)))

playerData = player.getMatch(0).getPlayerData()
print("Kills: " + playerData.getKills())
print("Damage: " + playerData.getDamageDealt())
print("Boosts: " + playerData.getBoostsUsed())
print("Kill Ranking: " + playerData.getKillRank())
print("Win Ranking: " + playerData.getWinRank())

telemetry = player.getMatch(0).getTelemetry()
telemetry.getMatchStart()
telemetry.getBlueZone()
telemetry.getWinningDropLocation()

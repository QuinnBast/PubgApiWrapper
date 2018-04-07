import sys
sys.path.append('Api/')
from PubgApi import PubgApi

player = PubgApi().getPlayerFromString("R10t--")
print(player.getPlayerName())
print(player.getPlayerId())
playerData = player.getMatch(0).getPlayerData()
print(playerData.getKills())
print(playerData.getDamageDealt())
print(playerData.getBoostsUsed())
print(playerData.getKillRank())
print(playerData.getWinRank())

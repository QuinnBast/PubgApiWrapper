import peewee
import re
from peewee import *
import datetime

conn = MySQLDatabase('CrawlerDatabase', user='root', passwd='C:hDrh"Ey2X@){]@`:C3w6!E5bjTE2]-')

class BaseModel(peewee.Model):
	class Meta:
		database = conn

class PubgStatsModel(BaseModel):
	statpk = peewee.IntegerField(unique = True, primary_key = True)
	date = peewee.DateTimeField()
	playerName = peewee.CharField()
	gameMode = peewee.CharField()
	rating = peewee.IntegerField()
	kDRatio = peewee.IntegerField()
	avgDamage = peewee.IntegerField()
	winRate = peewee.DecimalField()
	topTen = peewee.DecimalField()
	longestKill = peewee.DecimalField()
	headshots = peewee.DecimalField()
	averageRank = peewee.DecimalField()
	averageSurvivalTime = peewee.DecimalField()
	mostKills = peewee.IntegerField()
	gamesPlayed = peewee.IntegerField()
	server = peewee.CharField()

	def __init__(self):
                self.date = datetime.datetime.now()
                conn.connect()
                conn.create_tables([PubgStats])

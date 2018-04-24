import peewee
import re
from peewee import *
import datetime
import conn

conn = conn.dbConnection()

class BaseModel(peewee.Model):
	class Meta:
		database = conn

class PubgBlueZoneModel(BaseModel):
	x = peewee.FloatField()
	y = peewee.FloatField()
	z = peewee.FloatField()
	radius = peewee.FloatField()
	mapName = peewee.CharField()
	gameId = peewee.CharField()

	def __init__(self, **kwargs):
            BaseModel.__init__(self, **kwargs)
            conn.create_tables([PubgBlueZoneModel])

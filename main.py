import urllib 
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import lxml
import urllib, json
import pandas as pd, numpy as np
from urllib.parse   import quote
import pymongo
from pymongo import MongoClient
import requests


def grab_test(user,key):
	url = 'https://distribution-xml.booking.com/json/bookings.getHotels?city_ids=-2637882'
	response = requests.get(url, auth = ( user , key )) 
	return response
	print (response.json())

def grab_hotel_list():

	response = grab_test()
	output = [[] for k in range(0,8)]
	for count, item in reversed(list(enumerate(r3.json()))):
		output[0].append(r3.json()[count]['name'])
		output[1].append(r3.json()[count]['address'])
		output[2].append(r3.json()[count]['city'])
		output[3].append(r3.json()[count]['city_id'])
		output[4].append(r3.json()[count]['hotel_id'])
		output[5].append(r3.json()[count]['location']['latitude'])
		output[6].append(r3.json()[count]['location']['longitude'])
		output[7].append(r3.json()[count]['zip'])
	df_ = pd.DataFrame(output).T
	df_.columns = [['name','address','city','city_id','hotel_id','latitude','longitude','zip']]
	print (df_.head())
	return df_



def connect_mongo():
	client = MongoClient('localhost', 27017)
	print (client.database_names())
	db = client.booking
	print (db.collect_1.find_one())


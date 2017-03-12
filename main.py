from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import urllib, json, lxml
import pandas as pd, numpy as np
from urllib.parse   import quote
import pymongo
from pymongo import MongoClient



user = 'hacker234'
key = '8hqNW6HtfU'


def grab_hotel_list_json(user,key):
	url = 'https://distribution-xml.booking.com/json/bookings.getHotels?city_ids=-2637882'
	response = requests.get(url, auth = ( user , key )) 
	print (response.json())
	return response.json()



def grab_hotel_pic_json(user,key):
	url = 'https://distribution-xml.booking.com/json/bookings.getHotelDescriptionPhotos?city_ids=-2637882'
	response = requests.get(url, auth = ( user , key )) 
	print (response.json())
	return response.json()
	

def get_hotel_list():

	response = grab_hotel_list_json(user,key)
	output = [[] for k in range(0,8)]
	for count, item in reversed(list(enumerate(response))):
		output[0].append(response[count]['name'])
		output[1].append(response[count]['address'])
		output[2].append(response[count]['city'])
		output[3].append(response[count]['city_id'])
		output[4].append(response[count]['hotel_id'])
		output[5].append(response[count]['location']['latitude'])
		output[6].append(response[count]['location']['longitude'])
		output[7].append(response[count]['zip'])
	df_ = pd.DataFrame(output).T
	df_.columns = [['name','address','city','city_id','hotel_id','latitude','longitude','zip']]
	print (df_.head())
	return df_

def get_hotel_photo():
	
	response = grab_hotel_pic_json(user,key)
	output_photo = [[] for k in range(0,3)]
	for count, item in reversed(list(enumerate(response))):
		output_photo[0].append(response[count]['hotel_id'])
		output_photo[1].append(response[count]['url_max300'])
		output_photo[2].append(response[count]['url_original'])
	df_photo = pd.DataFrame(output_photo).T
	df_photo.columns = [['hotel_id','url_max300','url_original']]
	df_photo_ = df_photo.groupby('hotel_id').first().reset_index()
	print (df_photo_.head())
	return df_photo_
      

def hotel_data():
	hotel_list_data  = get_hotel_list()
	print (hotel_list_data.head(3))
	hotel_photo = get_hotel_photo()
	print (hotel_photo.head(3))
	df_final = pd.merge(hotel_list_data,hotel_photo,  how='left',on = 'hotel_id').sort('url_max300')
	print (df_final)
	print ('merge OK')
	df_final_json = json.loads(df_final.to_json(orient='records'))
	print (df_final_json)
	return df_final , df_final_json



def input_data_mongo():
	df, df_json = hotel_data()
	clinet, db = connect_meteor_mongo()
	try:
		db.hotels.insert(df_json)
		print ('insert OK ')
	except:
		print ('failer')




# ======================================

def connect_mongo():
	client = MongoClient('localhost', 27017)
	print (client.database_names())
	db = client.booking
	print (db.collect_1.find_one())


def connect_meteor_mongo():
	client = MongoClient('localhost', 3001)
	print (client.database_names())
	db = client.meteor
	print (db.hotels.find_one())
	return client, db 



input_data_mongo()





import requests,json

#############################################
#simplified library to read/write on Xively
# https://xively.com/dev/docs/api/data/
#############################################
class XivelyRequests:
	def __init__(self,apikey,feed):
		self.baseurl = 'https://api.xively.com/v2/feeds'
		self.headers = {'X-ApiKey':apikey}
		self.feed = feed

	#create datastream for every device
	def __createDataStream(self,id_sensor,value):
		data = {
					'id':id_sensor,
					'datapoints':[],
					'current_value':value
				}
		return data

	def __createData(self,sensors):
		streams = [self.__createDataStream(x,y) for (x,y) in sensors.items()]
		#append to data
		data = {
			'version':'1.0.0',
			'datastreams': streams
		}
		#
		return json.dumps(data)

	#get feed
	def get(self):
		res = requests.get('%s/%s.json' % (self.baseurl,self.feed),headers=self.headers)
		if res:
			return res.json()
		else:
			return False

	#push datastreams to feed
	def push(self,sensors):
		data = self.__createData(sensors)
		res = requests.put('%s/%s.json' % (self.baseurl,self.feed), data=data, headers=self.headers)


#tests
if __name__ == "__main__":
	import random
	#create connector
	x = XivelyRequests('PiDZeUIcrII4P6AZy1ccpUzrEsJoCrrHC5nYEyHp90575890','1938656644')
	#get data
	print x.get()
	#set data
	x.push({'sensor':random.randint(1,100),'sensor2':random.randint(1,100)})
	#get data
	print x.get()


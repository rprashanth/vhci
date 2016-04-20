import sys
sys.path.insert(0, '../')
from ttcc import core, utils
import devices

newcommand = True
oldResult = {}
output = {}

def test_totem():
	core.register('totem', devices.totem)
	global newcommand, oldResult, output
	expected_output_1 = {
		"arguments": {
		 	"name": " devices"
		 },
		 "device": "totem",
		 "intent": "--play"
	}
	expected_output_2 = {
  		"arguments": {},
  		"device": "totem",
  		"intent": "--pause"
	}

	expected_output_3 = {
  		"arguments": "",
  		"device": "totem",
  		"intent": None
	}
	expected_output_4 = {
		  "arguments": {},
		  "device": "totem",
		  "intent": "--quit"
		}
	expected_output_5 = {
		"arguments":{},
		"device":"totem",
		"intent":"--next"
		}
	actual_output, device, output = core.parse('totem play devices', newcommand, oldResult, output)
	assert expected_output_1 == actual_output
	print('success 1 totem')
	actual_output, device, output = core.parse('totem pause', newcommand, oldResult, output)
	assert expected_output_2 == actual_output
	print('success 2 totem')
	actual_output, device, output = core.parse('totem',newcommand, oldResult, output)
	assert expected_output_3 == actual_output
	print('success 3 totem')
	actual_output, device, output = core.parse('totem quit',newcommand, oldResult, output)
	assert expected_output_4 == actual_output
	print('success 4 totem')
	actual_output, device, output = core.parse('totem next',newcommand, oldResult, output)
	assert expected_output_5 == actual_output
	print('success 5 totem')

def  test_tweets():
	core.register('tweet', devices.tweet)
	global newcommand, oldResult, output
	expected_output_1 = {
		"arguments": {
			"name": " google"
		},
		"device": "tweet",
		"intent": "search/tweets"
	}
	expected_output_2 = {
       	"arguments": {
    		"name": " india"
  		},
  		"device": "tweet",
  		"intent": "trends/place"
	}
	expected_output_3 = {
       	"arguments": {
    		"name": " rcbtweets"
  		},
  		"device": "tweet",
  		"intent": "statuses/user_timeline"
	}
	expected_output_4 = {
  		"arguments": "",
  		"device": "tweet",
  		"intent": None
	}
	actual_output, device, output = core.parse('tweets on google', newcommand, oldResult, output)
	assert expected_output_1 == actual_output
	print('success 6 tweets')
	actual_output, device, output = core.parse('tweets in india', newcommand, oldResult, output)
	assert expected_output_2 == actual_output
	print('success 7 tweets')
	actual_output, device, output = core.parse('tweets by rcbtweets', newcommand, oldResult, output)
	assert expected_output_3 == actual_output
	print('success 8 tweets')
	actual_output, device, output = core.parse('tweets', newcommand, oldResult, output)
	assert expected_output_4 == actual_output
	print('success 9 tweets')

def test_weather():
	core.register('weather',devices.weather)
	global newcommand, oldResult, output
	expected_output_1 = {
  		"arguments": {},
  		"device": "weather",
  		"intent": 'will'
	}
	expected_output_2 = {
		"arguments": {
			'name' : ' london'
		},
  		"device": "weather",
  		"intent": 'set city'
	}
	expected_output_3 = {
		"arguments": {},
  		"device": "weather",
  		"intent": 'maxTemperature'
	}
	expected_output_4 = {
		"arguments": {},
  		"device": "weather",
  		"intent": 'weather'
	}
	actual_output, device, output = core.parse('forecast will it rain tomorrow', newcommand, oldResult, output)
	assert expected_output_1 == actual_output
	print('success 10 weather')
	actual_output, device, output = core.parse('forecast set city london', newcommand, oldResult, output)
	print(actual_output)
	assert expected_output_2 == actual_output
	print('success 11 weather')
	actual_output, device, output = core.parse('forecast max temperature', newcommand, oldResult, output)
	assert expected_output_3 == actual_output
	print('success 12 weather')
	actual_output, device, output = core.parse('forecast what will be the weather tomorrow', newcommand, oldResult, output)
	assert expected_output_4 == actual_output
	print('success 13 weather')


test_totem()
test_tweets()
test_weather()
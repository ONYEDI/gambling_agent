import requests
import json
import pandas as pd


url = "https://api-football-v1.p.rapidapi.com/v3/odds/live"

headers = {
	"X-RapidAPI-Key": "1f097c55c1msh197c97107c7352fp11865cjsn52073dc08857",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)


data = response.json()
data_json = data['response']
data_csv = pd.DataFrame(data_json)
data_csv.to_csv('odd.csv')

    
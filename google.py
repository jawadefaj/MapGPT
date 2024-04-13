import requests
from openai import OpenAI

url = "https://maps.googleapis.com/maps/api/directions/json"
client = OpenAI(
        api_key= '' #wont let me push an API key 
)

params = {
    "origin": "San Francisco",
    "destination": "Los Angeles",
    "key": "AIzaSyDwV3dWFF0-3nXha9uQwBHnpSebxB72VB8" #wont let me push an API key 

}




def callgpt(map_response):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                #change message 
                "content": "You will be provided with a JSON, and your task is to create a summary of the trip based on the information from the json file, at least one paragraph long."
            },
            {
                "role": "user",
                "content": f"{map_response}"
            }
        ],
        temperature=0.3,
        max_tokens=64,
        top_p=1
    )
    
    return response

response = requests.get(url, params=params) #api call to google maps 

if response.status_code == 200:
    #convert to json
    data = response.json()

    #this is to delete the polyline and overview_polyline from the json file
    routes = data.get("routes", [])
    for route in routes:
        legs = route.get("legs", [])
        for leg in legs:
            steps = leg.get("steps", [])
            for step in steps:
                step.pop('polyline', None)
                step.pop('overview_polyline', None)
    print(data) #print out JSON data 

    map_response = data
    
    #call chatgpt on the data 
    summary = callgpt(map_response)
    print(summary)
else:
    print("Error:", response.status_code)

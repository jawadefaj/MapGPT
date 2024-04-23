import requests
from openai import OpenAI
import json
# import osm2gmns as og

# og.downloadOSMData(112143, "san_jose.osm")

# Define the API endpoint and parameters
url = "https://api.openrouteservice.org/v2/directions/driving-car/json"


body = {"coordinates" :  [[-121.905, 37.349], [-121.905, 37.350]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf62487626350f230942808541a0b850e37e55',
    'Content-Type': 'application/json; charset=utf-8'
}

call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car/json', json=body, headers=headers)

print(call.json())
#save the json to a file
with open('data.json', 'w') as f:
    json.dump(call.json(), f)

client = OpenAI(
        api_key= '' #wont let me push an API key 
)

def callgpt(map_response):
    promptE = " you are an expert in maps and you will carefully help plan routes. Your task is to make a summary of a route from a JSON file given to you. In the summary, you have to include the following things: origin and destination, total distance, total duration, and a description of the route chosen. You must give a description of the route in a way that is easy to understand for the user. If there is anything that makes the route complex, you have to mention it (for example, winding roads, fast exit ramps, multiple lane changes.). The summary should be a detailed paragraph."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                #change message 
                "content": promptE
            },
            {
                "role": "user",
                "content": f"{map_response}"
            }
        ],
        temperature=0.3,
        top_p=1
    )
    
    
    return response

# Make the API request

# Check if the request was successful


map_response = call

#call chatgpt on the data 
summary = callgpt(map_response.json())
message = summary.choices[0].message.content
print(message)


    # Access the route information
   


import requests
from openai import OpenAI
import json

# url = "https://maps.googleapis.com/maps/api/directions/json"
url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
client = OpenAI(
        api_key= '' #wont let me push an API key 
)

payload = {
    "origin": {
        # "address": "Reed & Graham, Inc. - Geosynthetics, 550 Sunol St, San Jose, CA 95126"
        "address": "Gulshan 1, Dhaka 1212, Bangladesh"

    },
    "destination": {
        # "address": "Tennis courts - Almarida, San Jose, CA 95128"
        "address": "Mirpur-2, Dhaka, Bangladesh"
    },
    "travelMode": "DRIVE"
}

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': 'AIzaSyCpSybPL8g3yZtagfU_4d5fEXdHpc0Romg',  # Replace 'YOUR_API_KEY' with your actual API key
    'X-Goog-FieldMask': '*'
}


params = {
    ##glendale to LA 
    #Houston to 
    "origin": "Reed & Graham, Inc. - Geosynthetics, 550 Sunol St, San Jose, CA 95126",
    "destination": "Tennis courts - Almarida, San Jose, CA 95128",
    "key": "AIzaSyDwV3dWFF0-3nXha9uQwBHnpSebxB72VB8" #wont let me push an API key 

}




def callgpt(map_response):
    

    promptE = "You are an expert in maps and you will carefully help plan routes. Your task is to make a summary of a route from a JSON file. Include the origin and destination, total distance, total duration, and a description of the route chosen. Make the summary easy to understand for the user. If there are any coordinates, make sure to convert them to locations the user can understand.  Write a detailed paragraph describing the route."
    prompt2 = "Make the summary more detailed. I want to know every turn and lane change. Include any landmarks or traffic conditions that might be important. Make sure to convert all coordinates to real locations. Return a detailed paragraph."
    response1 = client.chat.completions.create(
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
    # print("res1")
    # print(response1.choices[0].message.content)
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                #change message 
                "content": prompt2
            },
            {
                "role": "user",
                "content": response1.choices[0].message.content
            }
        ],
        temperature=0.3,
        top_p=1
    )
    
    
    return response2

# response = requests.get(url, params=params) #api call to google maps 

def remove_polyline(obj):
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == 'polyline' or key == 'encodedPolyline':
                del obj[key]
            else:
                remove_polyline(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            remove_polyline(item)
    return obj

def googleAPI_and_filter(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Remove 'polyline' and 'overview_polyline' keys from each step
        r = remove_polyline(data)

        return r

        # Write modified JSON data to file
        # with open('exmple.json', 'w') as f:
        #     json.dump(r, f)

        # print(data) # Print out modified JSON data
    #write JSON to file
    # with open('newdata.json', 'w') as f:
    #     json.dump(data, f)

    # map_response = data
    
    # #call chatgpt on the data 
    # summary = callgpt(map_response)
    # message = summary.choices[0].message.content
    # # file1 = open("summary.txt","w")
    # # file1.write(str(message))
    # # file1.close()
    # print(message)
# googleAPI_and_filter(url, payload, headers)
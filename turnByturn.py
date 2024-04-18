import requests
from openai import OpenAI

def get_turn_by_turn_directions(source, destination, api_key):
    url = f"https://maps.googleapis.com/maps/api/directions/json?destination=destination&origin=source&key= api_key"
    
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "OK":
        # Extracting the steps from the response
        steps = data["routes"][0]["legs"][0]["steps"]
        turn_by_turn_directions = []
        for step in steps:
            turn_by_turn_directions.append(step["html_instructions"])
        return data
    else:
        print("Error:", data["status"])
        return None
    
def callgpt(map_response):
    client = OpenAI(
        api_key= '' #wont let me push an API key 
)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                #change message 
                "content": "You will be provided with a JSON, and your task is to create a summary of the trip based on the information from the json file with the Include origin and destination,Total distance,Travel time,Route Overview,Iconic store or field or sign while describing the route, Complex road layouts,Speed bumps , Multiple ramps, loops, exits with numerous exits, flyover, roundabout,Multiple lane changes to take an exit,Merging onto oncoming traffic,Being at a stop sign to turn onto the freeway,Narrow streets,Unfamiliar roads,Different speed zones through the route,Travel tie,Route Overview,Iconic store or field or sign while describing the route. and complexities:Speed bumps , Multiple ramps, loops, exits with numerous exits, flyover, roundabout,Multiple lane changes to take an exit,Merging onto oncoming traffic,Being at a stop sign to turn onto the freeway,Narrow streets,Unfamiliar roads,Different speed zones through the route"
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

def main():
    source = input("Enter the source address: ")
    destination = input("Enter the destination address: ")
    api_key = ""

    directions = get_turn_by_turn_directions(source, destination, api_key)
    
    if directions:
        print("Turn-by-turn directions:")
        for direction in directions:
            print(direction)
        summary = callgpt(directions)
        print(summary)

    else:
        print("Failed to retrieve directions.")

if __name__ == "__main__":
    main()

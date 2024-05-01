#this is the steps for pipeline:
# open CSV file and extract needed data
# make arrays of all extracted data
#then one giant for loop for all data, call google maps API, get the response, call GPT-3 API. If using COT, set flag to true, and call COT API
#then from the Human Summary and AI Summary, put the results into BERT and get the similarity score, 
#then put the results into BLEU and get the similarity score, and then 
#write the response to a CSV file, with the routeID, Start,  Destination, End Destination, Human Summary of Route, AI Summary of Route (if using COT, then COT Summary of Route), Similarity Score from BERT, Similarity Score from BLEU


import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from evaluate import load

from openai import OpenAI
from pathlib import Path
from bleu1 import bleu_score


from datagoogle import googleAPI_and_filter , callgpt
import pandas as pd
# Read the CSV file



def cosine_sim(ref, pred):
    vectorizer = CountVectorizer()

    # Fit and transform the text data
    vectorized_text = vectorizer.fit_transform([ref, pred])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
    # print(cosine_sim)
    # print("Cosine Similarity:", cosine_sim[0][0])
    return cosine_sim[0][0]




bertscore = load("bertscore")

df = pd.read_csv('routefilter.csv')

# Display the first few rows of the dataframe

#origin is the 3rd column, destination is the 4th column
origin = df.iloc[0, 2]
destination = df.iloc[0, 3]

originarr = []
destinationarr = []
humanarr = []
routeIDarr = []
isCOT = False

url = 'https://routes.googleapis.com/directions/v2:computeRoutes'


fieldnames = ['routeID', 'Start', 'Destination', 'Human_Summary', 'AI_SummaryCOT', 'BERT_Precision', 'BERT_Recall', 'BERT_F1', 'Cosine_Similarity', 'BLEU_Score']


with open('COToutput.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': 'AIzaSyCpSybPL8g3yZtagfU_4d5fEXdHpc0Romg',  # Replace 'YOUR_API_KEY' with your actual API key
    'X-Goog-FieldMask': '*'
}


#loop through all the origins and destinations
for i in range(len(df)):
    
    origin = df.iloc[i, 2]
    destination = df.iloc[i, 3]
    human_summary = df.iloc[i, 5]
    # print(f"Origin: {origin}")
    if pd.isna(origin) or pd.isna(destination):
        continue

    # print(f"Destination: {destination}")
    # print(f"Human Summary: {human_summary}")
    originarr.append(origin)
    destinationarr.append(destination)
    humanarr.append(human_summary)
    routeIDarr.append(origin + " to " + destination)
    # Make the API request


    payload = {
        "origin": {
            # "address": "Reed & Graham, Inc. - Geosynthetics, 550 Sunol St, San Jose, CA 95126"
            "address": originarr[i]

        },
        "destination": {
            # "address": "Tennis courts - Almarida, San Jose, CA 95128"
            "address": destinationarr[i]
        },
        "travelMode": "DRIVE"
    }
    googJson = googleAPI_and_filter(url=url, payload=payload, headers=headers)

    res = callgpt(googJson)   
    AIsummary = res.choices[0].message.content

# print(AIsummary)

    references = humanarr[i]
    predictions = AIsummary


    BERTresults = bertscore.compute(predictions=[AIsummary], references=[references], lang="en")

    BleuResults = bleu_score(predictions, references)
    cosine_similary = cosine_sim(references, predictions)

#write the response to a CSV file, with the routeID, Start,  Destination, End Destination, Human Summary of Route, AI Summary of Route (if using COT, then COT Summary of Route), Similarity Score from BERT, Similarity Score from BLEU, with the first row being the headers
    with open('COToutput.csv', mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'routeID': routeIDarr[i], 'Start': originarr[i], 
                         'Destination': destinationarr[i], 
                        'Human_Summary': humanarr[i], 
                        'AI_SummaryCOT': AIsummary, 
                        'BERT_Precision': BERTresults['precision'][0], 
                        'BERT_Recall': BERTresults['recall'][0],
                        'BERT_F1': BERTresults['f1'][0],
                        'Cosine_Similarity': cosine_similary,
                        'BLEU_Score': BleuResults})



    







    

    





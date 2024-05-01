# from nltk.translate.bleu_score import corpus_bleu

# # Define your desired weights (example: higher weight for bi-grams)
# weights = (0.25, 0.25, 0, 0) # Weights for uni-gram, bi-gram, tri-gram, and 4-gram

# prediction = "This route takes you from 550 Sunol St to San Jose, covering a distance of 5.4 miles and taking approximately 9 minutes. The route includes a mix of city streets and highways, starting with a short drive north on Sunol St before merging onto I-280 N. From there, you will take exit 5B onto CA-17 S towards Santa Cruz before taking the exit towards E Hamilton Ave. Finally, you will turn right onto Almarida Dr and reach your destination at the traffic circle. This route offers a quick and efficient way to reach your destination in San Jose. Starting at 550 Sunol St, you will head north towards W Julian St. After a short drive, you will merge onto I-280 N towards San Francisco. Stay on I-280 N for about 3.5 miles before taking exit 5B towards CA-17 S towards Santa Cruz. Keep right at the fork to continue on CA-17 S. Along this stretch, you will pass by the Winchester Mystery House and the Santana Row shopping center. After about 1.5 miles, take the exit towards E Hamilton Ave. Keep left at the fork and follow signs for E Hamilton Ave E. You will then turn right onto E Hamilton Ave and continue for about half a mile before turning right onto Almarida Dr. This will lead you to a traffic circle where you will reach your destination in San Jose, CA 95128. Along the route, you may encounter moderate traffic conditions, especially on I-280 N and CA-17 S during peak hours. Keep an eye out for any construction or accidents that may cause delays. The Winchester Mystery House is a notable landmark along the route, known for its unique architecture and rumored hauntings. Santana Row is also a popular spot for shopping, dining, and entertainment."
# splitted = prediction.split()
# print(splitted)
# # Reference and predicted texts (same as before)
# reference = [["the", "picture", "is", "clicked", "by", "me"],
# 			["this", "picture", "was", "clicked", "by", "me"]]
# predictions = ["the", "picture", "the", "picture", "by", "me"]

# # Calculate BLEU score with weights
# score = corpus_bleu(reference, predictions, weights=weights)
from nltk.translate.bleu_score import sentence_bleu

def bleu_score(reference, prediction):
    
    references = reference.split()
    prediction = prediction.split()
    score = sentence_bleu(references, prediction)
    return score





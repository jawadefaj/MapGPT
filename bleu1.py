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


# two references for one document
from nltk.translate.bleu_score import corpus_bleu

prediction = "This route takes you from 550 Sunol St to San Jose, covering a distance of 5.4 miles and taking approximately 9 minutes. The route includes a mix of city streets and highways, starting with a short drive north on Sunol St before merging onto I-280 N. From there, you will take exit 5B onto CA-17 S towards Santa Cruz before taking the exit towards E Hamilton Ave. Finally, you will turn right onto Almarida Dr and reach your destination at the traffic circle. This route offers a quick and efficient way to reach your destination in San Jose. Starting at 550 Sunol St, you will head north towards W Julian St. After a short drive, you will merge onto I-280 N towards San Francisco. Stay on I-280 N for about 3.5 miles before taking exit 5B towards CA-17 S towards Santa Cruz. Keep right at the fork to continue on CA-17 S. Along this stretch, you will pass by the Winchester Mystery House and the Santana Row shopping center. After about 1.5 miles, take the exit towards E Hamilton Ave. Keep left at the fork and follow signs for E Hamilton Ave E. You will then turn right onto E Hamilton Ave and continue for about half a mile before turning right onto Almarida Dr. This will lead you to a traffic circle where you will reach your destination in San Jose, CA 95128. Along the route, you may encounter moderate traffic conditions, especially on I-280 N and CA-17 S during peak hours. Keep an eye out for any construction or accidents that may cause delays. The Winchester Mystery House is a notable landmark along the route, known for its unique architecture and rumored hauntings. Santana Row is also a popular spot for shopping, dining, and entertainment."
splitted_prediction = prediction.split()
print(splitted_prediction)

reference1 = "The route starts from Reed and Graham Inc. and ends at the Tennis Courts in Almarida San Jose. The total travel time will be around 11 minutes, and the total distance will be 4.4 miles. You will first have to turn left on Savaker Ave, take a left on Lincoln, and then follow Parkmoore Ave until you merge onto I-280 N towards CA-17. From there, you must do two lane changes to take exit 5B towards Santa Cruz. Once you are on the 17, you will use the right lane to take the exit toward East Hamilton Ave. Once you are on Hamilton Ave, take a right at the signal and go straight on Almarida Dr until you reach the destination. There will be a roundabout on that road, so take care when driving."
splitted_referrence1 = reference1.split()
print(splitted_referrence1)

reference2 = "The route is a total of 5.4 miles, where you drive 4 miles on the highway interstate I 280. First, you take the Sunol st for about half a mile. Take a right turn after the Del Monte park field and get on to Auzerais st. Cross the Los Gatos Creek. Cross the Royal Ave and take a right at the Barack Obama Bl. take the freeway entrance right after taking the right turn towards I 280. Stay alert during this transition as you have to cross a bike lane while crossing the ramp. Marge with the I 280 by moving to the left lane as there is an exit-only lane for taking the race street to southwest Expwy. Keep second from the left lane to avoid merging and exit-taking traffic when you are crossing the exit 5A. You will see a sign for exit 5B-C. Take exit 5B and keep left so that you can take the next exit toward Santa Cruz. Be careful here as there are merging traffic from the Parkmoore Ave road. Keep on driving and merge with the Highway 17 traffic. Keep on you right to take exit only road towards Hamilton Ave. This will become a 4 lane road with three lanes going to the left and one lane going to the right. Keep right to take the east Hamilton ave. take right on the first traffic light you see. This will lead you to almarida dr. Cross Kohls store on your right watch out for the speed bumps in this areas. When you reach the first small roundabout, keep on driving towards Almarida drive. This will finally take you to Tennis courte almarida."
splitted_referrence2 = reference2.split()
print(splitted_referrence2)

reference3 = "We started from 525 Sunol Road which is a narrow road for driving only two cars. When we see the first road cross section with four directions, we take a right turn and drive to 809 Auzerals Ave. We face a slight left curve while reaching 799 Auzerals Ave. There is a train line that goes across 741 Auzerals Ave. After that, we take a very sharp right turn to go to the I-280. I-280 has two big turns along the way. From I-280, we go to the San Jose Freeway. Then we get to 501 Parkmoor Ave. There is a sharp left turn from Parkmoor Ave to Highway 17. From there, we take an exit from Campbell, CA. Then we take a left turn to Hamilton Ave in order to merge into Almarida Drive. We see a cross section, we take the straight road and go through the 761 Almarida Drive to reach the tennis court."
splitted_referrence3 = reference3.split()

references = [[reference1,reference2,reference3]]

candidates = [prediction]
score = corpus_bleu(references, candidates)
print(score)

from profanity_check import predict, predict_prob
import joblib

sentences = ["fuck you", 
             "hello how are you", 
             "she's looking bad because she got no teeth", 
             "government also make bad decision because they are often brainless",
             "people are annoying sometimes", 
             "bitch nigga miss me with it",
             "bitch plz whatever"]

res = predict(['predict() takes an array and returns a 1 for each string if it is offensive, else 0.'])
print(res)
# [0]

res = predict(['fuck you'])
print(res)
# [1]

res = predict_prob(['predict_prob() takes an array and returns the probability each string is offensive'])
# [0.08686173]
print(res)

res = predict_prob(['go to hell, you scum'])
# [0.7618861]
print(res)

res = predict_prob(sentences)
print(res)

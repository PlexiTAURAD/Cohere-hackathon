# All import statements 
import cohere
import config
import examples_t
from examples_t import classify1
from cohere.classify import Example
import json
import numpy as np
co = cohere.Client('qKmjw3VxjZl30lbOw8oxWV8InZoRdkM7Ltq0wGTE')

details = [] 
#Initially an empty list, this will contain all important details of the interaction and will be displayed at the end with the help of a text_map
###
# Here we get the response classification
response = co.classify(
    model = "large",
    inputs = ["I just bought this laptop but its charger is not working"],
    examples= classify1
)
list = []


#Now we get the highest confidence label and store it in a list
#print(response.classifications) to check how the input compares
#print(response.classifications[0].prediction) to get the prediction label
tru_response = response.classifications[0].prediction 
list.append(tru_response) #Empty list now has 1 recorded value 
print(list)

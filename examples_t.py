import cohere
from cohere.classify import Example

classify1 = [
    Example("Hello, my laptop isnt connecting to the internet","0"),
    Example("My laptop keeps crashing","0"),
    Example("Why isnt my phone turning on?","0"),
    Example("How do I download apps","0"),
    Example("How do I upgrade my windows software?","0"),
    Example("What is the best laptop you are selling?","1"),
    Example("What are the device specifications for this phone?","1"),
    Example("Does this laptop have an HD display?","1"),
    Example("What is the camera quality in this phone?","1"),
    Example("Is this laptop good for gaming?","1"),
    Example("Hello I had ordered a laptop, when will I receive it?","2"),
    Example("I would like to cancel my order","2"),
    Example("My order still hasnt been delivered yet","2"),
    Example("I was supposed to recieve my order today, why did i not get it yet?","2"),
    Example("Can you change the address for the order? I will be outside","2"),
    Example("I want to return my product","3"),
    Example("Are there any exhange offers available for this product?","3"),
    Example("This product sucks and I want to return it","3"),
    Example("This product arrived broken, I dont want this","3"),
    Example("This product is misleading, I dont want it","3"),
    Example("Why was I charged extra?","4"),
    Example("Are loan options availabe for this device?","4"),
    Example("I would like to update my billing information","4"),
    Example("Can you send bills to a new address instead?","4"),
    Example("My account was debited despite the billing period being over","4"),
    Example("My device is broken, where can I fix it","5"),
    Example("How much will it cost to fix my phone","5"),
    Example("Where can I check my warranty?","5"),
    Example("I would like to extend my warranty","5"),
    Example("How much will a repair cost if I dont have warranty?","5"),
    Example("The laptop speakers are terrible","6"),
    Example("Great device! I loved it","6"),
    Example("Your products are awful","6"),
    Example("This is the best phone I ever had","6"),
    Example("Please just close down your company","6")
]

classify_warr = [
    Example("No I dont have warranty",0),
    Example("I used to but not anymore",0),
    Example("It expired last month",0),
    Example("I will in a month",0),
    Example("Yes I do",1),
    Example("Just got it last month",1),
    Example("I do",1)
]

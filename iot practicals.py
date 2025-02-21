import datetime
qna={
    "current date and time":datetime.datetime.now(),
    "what is your name":"my name is ashish",
    "what you do?":"i am a student",
    "who teaches you iot":"rahul sir",
    }
while True:
    question=input("ask your questions:        ")
    if(question=="quit"):
        break
    else:
        print(qna[question])




import random
print("hello reader")
reader=input("enter your name :  ")
print("welcome"  +reader)
name=["ram ","lakshman","bharat"]
place=["mumbai","delhi","kolkata"]
rn=random.choice(name)
rq=random.choice(place)
story=" "+rn+" is a good boy.he lives in "+rq+" his brother comes from "+rq+" and kill him"
print(story)

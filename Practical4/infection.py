#Initialize total students to 91
#Initialize current infected count and growth rate
#Set day counter to 0

#While current infected < total students:
   # Print current day and infected number
    #Calculate new infections (rounded)
    #Update total infected count
    #Increase day by 1

#After loop ends, print total days needed
whole=91
infected=5
rate=0.3
days=0
growth=0
while infected < whole:
    days+=1
    growth=round(infected*rate)
    infected+=growth
print(days)


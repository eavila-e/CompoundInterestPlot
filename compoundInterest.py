#FV = P*(1+R/N)^(N*T)
#FV is the future value of the loan or investment
#P is the initial principal amount
#R is the annual interest rate
#N represents the number of times interest is compounded per year
#T represents time in years
###
#For example, a $100 investment today with a 5.0% interest rate compounding annually for three years equals 
# $115.76 ($100*(1+.05/1)^(1*3). 
# Note that compound interest produces a higher end result than simple interest. Using the same example, 
# a simple interest calculation would only result in a value of $115.00 ($100*(1+.05*3)
#

import matplotlib.pyplot as plt
import numpy as np

# Compound interest variables
finalValue = []
initialAmount = [100,1000,5000]
annualRate = [0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]
finalValueArray = []
paymentPerYear = [1,2,3]
# Time in years
years = np.arange(0,20,0.5)
print(years)
colors = ['#DAF7A6','#FFC300','#FF5733','#C70039','#900C3F','#581845','r','g']
figure1, axis1 = plt.subplots(3,1)
figure2, axis2 = plt.subplots(3,1)
figure3, axis3 = plt.subplots(3,1)

for ia in initialAmount:

    for ppy in paymentPerYear:
        #ppy = 2
        for rate in annualRate:
                    
            for t in years:
                #FV = P*(1+R/N)^(N*T)
                power = pow((1+(rate/ppy)),(ppy*t))
                finalV = ia*power
                finalValue.append(finalV)
            
            finalValueArray.append(finalValue)
            finalValue = []

axisCount = 0
colorCount = 0
for i in range(len(finalValueArray)):
    
    if axisCount==3:
        axisCount=0

    if (i)%48 != 0 and i > 47 or i==48:
        print('plot : ',i)
        axis3[axisCount].plot(years,finalValueArray[i],color=colors[colorCount])
        colorCount+=1
    elif (i)%24 != 0 and i > 23 or i ==24:
        print('plot : ',i)
        axis2[axisCount].plot(years,finalValueArray[i],color=colors[colorCount])
        colorCount+=1
    elif (i)%8 != 0 or i==0 or i==8 or i ==16:
        print('plot : ',i)
        axis1[axisCount].plot(years,finalValueArray[i],color=colors[colorCount])
        colorCount+=1

    if (i+1)%8==0:
        axisCount+=1
        colorCount=0
    
plt.show()
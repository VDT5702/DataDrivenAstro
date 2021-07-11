from matplotlib import pyplot as plt
import random
import numpy as np

n=int(input("Enter the number of observations: "))

outcome_1=[]
outcome_2=[]

for i in range(0,n):
    outcome_1.append(random.randint(1,6))
    outcome_2.append(random.randint(1,6))
    
die_1=np.array(outcome_1)
die_2=np.array(outcome_2)

die_out=die_1+die_2

plt.hist(die_out)

plt.show()

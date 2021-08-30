# Hayati TAŞTAN
# 30.08.2021
# ===================
#SUBJECT: Classifying temperatures 
# PROBLEM: https://github.com/geo-python-2019/Exercise-3/blob/206bf7dc1b223a8dd85e139b6eb8c5011e01b8b5/Exercise-3-problem-2.ipynb
# SOLUTION: 

temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]
Cold =[]
Slippery = []
Comfortable =[]
Warm=[]

for i in temperatures: 
    if (i < -2):
        Cold.append(i)
    elif (i <= -2 or i < 2):
        Slippery.append(i)
    elif (i <= 2 or i < 15):
        Comfortable.append(i)
    else:
        Warm.append(i)
        
print("In April 2013, it was slippery " + str(len(Slippery)) + " times.")
print("In April 2013, it was warm " + str(len(Warm)) + " times.")
print("In April 2013, it was cold " + str(len(Cold)) + " times.")
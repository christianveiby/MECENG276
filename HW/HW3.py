import numpy as np

# Problem 4

# Get num of zeros and ones
survey = open("./survey.txt")
n = 0
y = 0
for i in survey.read().split("\n"):
    if i.__contains__("0"):
        n+=1
    else:
        y+=1

mean = (y*1+n*0)/(y+n)
std_dev = np.sqrt(((n*(0-mean)**2) + (y*(1-mean)**2))/(y+n))

print("Sample mean: ", mean)
print("Std. dev.: ", std_dev.round(4))

# We can use the CLT to make the gaussian assumption. Because the sample size is large enough.

# Find the Confidence Interval of the mean with 95% confidence

P = (std_dev/np.sqrt(n+y)) *np.abs(1.960)
confidence_interval = [(mean-P).round(4), (mean+P).round(4)]

print("Mean with c: 95%: ", confidence_interval)

N = ((std_dev/(P/2)) *np.abs(1.960))**2

print("Num of surveys to half ci: ", N)
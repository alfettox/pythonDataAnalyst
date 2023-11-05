import numpy as np

arr = [4,6,7,5,6,8,3,9]

mean = np.mean(arr)
standard_deviation = np.std(arr)

print("Mean: ", mean)
print("Standard deviation (variability, data distribution, risk): {:.4f}".format(standard_deviation))

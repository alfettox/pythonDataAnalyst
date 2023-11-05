import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 4, 4.5, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot")
plt.show()

#Create a scatter with seaborn
sns.scatterplot(x=x, y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter seaborn plot')

plt.show()
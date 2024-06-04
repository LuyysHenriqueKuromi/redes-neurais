import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression

#np.random.seed(42)
ages = np.random.randint(low=15, high=70, size=40)

print(ages)

labels = []
for age in ages:
    if age < 30:
        labels.append(0)
    else:
        labels.append(1)

#randow swap
for i in range(0, 3):
    r = np.random.randint(0, len(labels) -1)
    if labels[r] == 0:
        labels[r] = 1
    else:
        labels[r] = 0

model = LinearRegression()
model.fit(ages.reshape(-1, 1), labels)

#y = m.x + b
m = model.coef_[0]
b = model.intercept_
limiar_idade = (0.5 - b) / m
print(limiar_idade)

plt.plot(ages, ages * m + b, color="blue")
plt.plot([limiar_idade, limiar_idade], [0, 0.5], "--", color="green")
plt.scatter(ages, labels, color="red")
plt.show()

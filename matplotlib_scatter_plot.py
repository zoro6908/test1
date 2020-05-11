import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)

print(x,y)

plt.scatter(x,y)
plt.show()

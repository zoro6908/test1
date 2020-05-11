import matplotlib.pyplot as plt
import numpy

# plt.plot([1,2,3,4,10])
# plt.show()

# x=range(5)
# plt.plot(x, [x1**2 for x1 in x])
# plt.show()

x=numpy.arange(0,5,0.01)
print(x)
plt.plot(x, [i**2 for i in x])
plt.show()

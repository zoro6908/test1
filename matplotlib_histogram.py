import matplotlib.pyplot as plt
import numpy

# 넘파이 램덤 함수 정의
y=numpy.random.randn(100,100)

# 히스토그램 전환
plt.hist(y)

# 표시
plt.show()



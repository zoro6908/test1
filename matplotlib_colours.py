import matplotlib.pyplot as plt
import numpy as np

y=np.arange(1,3, 0.2)

# 라인 컬러
# plt.plot(y,'y')
# plt.plot(y+5,'m')
# plt.plot(y+10,'c')
# plt.show()

# 라인 스타일
# plt.plot(y,'--', y+5,'-.',y+10,':')
# plt.show()

# 라인 마킹 스타일
plt.plot(y,'*', y+0.5,'o',y+1,'D',y+2,'^',y+3,'s')
plt.show()

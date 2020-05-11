import matplotlib.pyplot as plt

# 정의 1
x=range(5)
plt.plot(x,[x1 for x1 in x])
plt.plot(x,[x1*x1 for x1 in x])
plt.plot(x,[x1*x1*x1 for x1 in x])

# 정의 2
# x=range(5)
# plt.plot(x,[x1 for x1 in x], x,[x1*x1 for x1 in x], x,[x1*x1*x1 for x1 in x])

# 라벨정의
x=range(5)
plt.plot(x,[x1 for x1 in x], label='A')
plt.plot(x,[x1*x1 for x1 in x], label='B')
plt.plot(x,[x1*x1*x1 for x1 in x], label='C')
# 라벨표시
plt.legend()

# 라벨링
plt.xlabel('X')
plt.ylabel('Y')

# 타이틀링
plt.title('Study Matplotlib')

# 눈금표시
plt.grid(True)

# x축 5에서 10까지 y축 5에서 20까지
# plt.axis([1,5,5,20])

# x축 5에서 10까지
# plt.xlim(1,5)
# y축 5에서 20까지
# plt.ylim(5,20)

# 표시
plt.show()

# 저장
plt.savefig('mymatplotlibtest.png')

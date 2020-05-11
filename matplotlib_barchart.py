import matplotlib.pyplot as plt
import numpy

# 바차트 예제1
# plt.bar([1.5,2.6,4.8],[40,55,89])

# 딕셔너리를 이용한 예제2
# dic={'A':25,'B':70,'C':55,'D':90}
# for i, key in enumerate(dic):
#     print(i)
#     # print(key)
#     plt.bar(i,dic[key])

# 딕셔너리를 이용한 예제3
dic={'A':25,'B':70,'C':55,'D':90}
for i, key in enumerate(dic):
    print(i)
    # print(key)
    plt.bar(i,dic[key])

# 라벨을 x축에 표시
# plt.xticks(numpy.arange(len(dic)),dic.keys())

# 라벨을 x축에 표시(쉬운방법)
plt.xticks([0,1,2,3],['A','B','C','D'])

# 표시
plt.show()



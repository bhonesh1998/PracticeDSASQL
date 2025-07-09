import numpy
from scipy import stats

ls=[1,2,3,4,4]

print(numpy.mean(ls))
print(numpy.median(ls))
print(stats.mode(ls)[0][0])


# a=[[1,10],[3,4]]
# print(numpy.array(a))
# # print(numpy.prod(a,0))
# # print(numpy.transpose(a))
# x=numpy.transpose(a)
# # print(numpy.transpose(x))
# y=x.tolist()
# print(y)
# for i in range(len(y)):
#     y[i]=list(reversed(y[i]))
# print(numpy.array(y))


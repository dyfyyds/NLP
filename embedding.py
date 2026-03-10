import pandas as pd
import numpy as np

#独热编码
#1.词语
vec = ['我','喜欢','吃','苹果','我']

# 2.1 pandas函数
one_hot_vec = pd.get_dummies(vec,dtype=int)
print(one_hot_vec)

# 2.2 手动实现
unique_vec = set(vec)
#计算维度
len = len(unique_vec)
#print(len)
one_hot_vec = np.zeros((len,len),dtype=int)
#修改对于位置的值
for i in range(len):
    one_hot_vec[i][i] = 1
#print(one_hot_vec)
print('*'*20)
print('\t'.join(vec))
#使用map转换字符串进行拼接
for word in one_hot_vec.T:
    print('\t'.join(map(str,word)))
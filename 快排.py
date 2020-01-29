
# coding: utf-8

# In[1]:


import random
a = [random.randint(0,1000) for n in range(1000)]
print(a)


# In[2]:


def quick_sort(a):
    if len(a)==0: #但a为空，就返回空列表
        return []
    first = a[0] #选取一个数据（通常选用数组的第一个数）作为关键数据
    left = []  #保存比first小的数
    right = [] #保存比first大的数
    for n in range(1,len(a)):
        if a[n]<first:
            left.append(a[n])
        else:
            right.append(a[n])
    left = quick_sort(left) #左边递归排序
    right = quick_sort(right) #右边递归排序
    left.append(first) #以下两行将left first right 合并于left
    left.extend(right)
    return left


# In[3]:


a_sorted = quick_sort(a)
print(a_sorted)


# In[4]:


for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)


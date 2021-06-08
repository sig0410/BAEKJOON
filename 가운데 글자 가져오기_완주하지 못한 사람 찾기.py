#!/usr/bin/env python
# coding: utf-8

# In[23]:


i = 'string'
a = len(i)
if a % 2 == 0:
    print(i[(a//2-1): (a//2 + 1)])
else:
    print(i[a//2])


# In[28]:


s = 'string'


# In[29]:


def solution(s):
    if len(s) % 2 == 0:
        return (s[(len(s)//2 -1) : (len(s) //2 +1)])
    else:
        return (s[len(s)//2])


# In[30]:


solution(s)


# =====================================================+

# In[72]:


p = ['leo', 'kiki', 'eden']
c = ['eden', 'kiki']


# In[50]:


def s(participant, completion):
    for p,c in zip(participant,completion):
        if p != c:
            return p


# In[53]:


for i,j in zip(p,c):
    if p != c:
        print(p)


# In[83]:


def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            print(participant[i])
        print(participant[-1])


# In[84]:


s(p,c)


# In[64]:


for i in range(len(p)):
    for j in c:
        if p[i] != j:
            print(p[i])
        else:
            break


# In[43]:


for i in range(len(p)):
    for j in c:
        if p[i] != j:
            


# In[49]:


for i in range(len(p)):
    print(p[i])


# In[63]:


for i,j in zip(p,c):
    


# In[73]:


print(p.sort())


# In[85]:


participant, completion = p, c


# In[86]:


print(p)
print(c)


# In[91]:


for i in range(len(completion)):
    if participant[i] != completion[i]:
        print(participant[i])
print(participant[-1])


# In[90]:


for i in range(len(c)):
    print(i)


# In[92]:


def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
# 인터넷 참고 ㅎㅎ 
# sort가 중요 
# sort를 통해서 각 인덱스별 비교가 가능해짐 


# In[93]:


solution(p,c)


#!/usr/bin/env python
# coding: utf-8

# ### Общие друзья в ВКОНТАКТЕ у двух разных пользователей
# 

# In[14]:


import requests
import sys
api_url = 'https://api.vk.com/method/friends.get'
token = 'c7e88ca5c7e88ca5c7e88ca555c79c027ecc7e8c7e88ca5987b8722588aeb7996f14dd2'
version = 5.92


def get_friends(user_id):
    params = {
    'access_token' : token,
    'v' : version,
    'user_id': user_id,
    'oder' : 'name'
    }

    res = requests.get('https://api.vk.com/method/friends.get', params=params)
    friends = res.text
    return friends
    
#разбиваем полученную строку по запятой на отдельные части, получая список объектов    
def preprocess_friends(friends):
    friends_split = friends.split(',')
    return friends_split

#находим пересечение двух списков, на выходе получаем список общих id-друзей у двух пользователей
def mutual_id(user_id1, user_id2):
    list_friends=(list(set(user_id1)&set(user_id2)))
    return list_friends

#общие id-друзей прогоняем через цикл, получая имя и фамилию общих друзей
def mutual_friends(list_friends):
    i = 0
    for i in list_friends:
        result = requests.get('https://api.vk.com/method/users.get', params={'user_ids': i,'v': version, 'access_token' : token})
        print(i, result.text)


# In[16]:


print(sys.argv)
arguments = sys.argv[1:]
user_id1 = int(arguments[0])
user_id2 = int(arguments[1])
#user_id1 = 121976167
#user_id2 = 166900632
user_id1 = get_friends(user_id1)
#mutual_friends(user_id1)
user_id2 = get_friends(user_id2)
user_id1 = preprocess_friends(user_id1)
user_id2 = preprocess_friends(user_id2)
list_friends = mutual_id(user_id1, user_id2)
mutual_friends(list_friends)


# In[ ]:





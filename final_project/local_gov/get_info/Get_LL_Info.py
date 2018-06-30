
# coding: utf-8

# ### Take links for each leader, scrape for 2 csv files
# 1. personal info
# 2. resume

# In[1]:


import pandas as pd
pd.set_option('display.max_colwidth', 500)

import re


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


df = pd.read_csv("/root/local_leader_links.csv")


# In[5]:


# df.shape


# In[6]:


# df


# In[5]:


# raw_html = requests.get("http://ldzl.people.com.cn/dfzlk/front/personPage15514.htm").content
# info = BeautifulSoup(raw_html, "html.parser")

# title = info.find("dl").find("i").text
# name = info.find("dl").find("strong").text

# resume = info.find("div", attrs = {"class" : "box01"}).text.replace("\r\r\n\t\t \r\n\t\t\t\u3000\u3000", "；").split("；")
# short_bio = resume[0]
# publish_date = resume[-1]
# additional_info = resume[-2]

# print(name, title, short_bio)
# print("------------")
# print(publish_date,additional_info)

# for data in resume[1:-2]:
#     if len(data.split(" ")) == 2:
#         year = data.split(" ")[0]
#         content = data.split(" ")[1]
#     else:
#         year = "NaN"
#         content = data
#     print(year)
#     print(content)
#     print("------------")


# In[8]:


def get_leader_info(column):
    try:
        raw_html = requests.get(column["link"]).content
        info = BeautifulSoup(raw_html, "html.parser")

        leader_info_dict = {}

        title = info.find("dl").find("i").text
        name = info.find("dl").find("strong").text

        resume = info.find("div", attrs = {"class" : "box01"}).text.replace("\r\r\n\t\t \r\n\t\t\t\u3000\u3000", "；").split("；")
        short_bio = resume[0]
        publish_date = resume[-1]

        leader_info_dict.update({
            "name" : name,
            "title" : title,
            "short_bio" : short_bio,
            "publish_date" : publish_date,
            "group" : column["group"],
            "url" : column["link"],
            "province" : column["province"]
        })

        leader_info_list.append(leader_info_dict)

#         print(name, title, short_bio, publish_date)

        for data in resume[1:]:
            leader_resume_dict = {}
            if len(data.split(" ")) == 2:
                year = data.split(" ")[0]
                content = data.split(" ")[1]
            else:
                year = "NaN"
                content = data

            leader_resume_dict.update({
                "name" : name,
                "year" : year,
                "content" : content,
                "url" : column["link"]
            })
            leader_resume_list.append(leader_resume_dict)

#             print(name, year, content)
#         print("-------------------------------")
    except:
        problem = {}
        problem["name"] = column["name"]
        problem["url"] = column["link"]
        problem_list.append(problem)


# In[9]:


leader_resume_list = []
leader_info_list = []
problem_list = []


# In[7]:


# hlj = df[df.province == "黑龙江"]
# hlj.apply(get_leader_info, axis = 1)


# In[ ]:


df.apply(get_leader_info, axis = 1)


# In[56]:


local_leader_info = pd.DataFrame(leader_info_list)
local_leader_info.to_csv("local_leader_info.csv", index = False)


# In[55]:


local_leader_resume = pd.DataFrame(leader_resume_list)
local_leader_resume.to_csv("local_leader_resume.csv", index = False)

problem_leader = pd.DataFrame(problem_list)
problem_leader.to_csv("problem_leader.csv", index = False)
# In[60]:





# In[70]:

#!/usr/bin/env python
# coding: utf-8

# In[9]:


api_key = "AIzaSyC2ueszUwbMCU7G1_ukPGtNkBZke-YC4Nw"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)


# In[10]:


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import matplotlib.pyplot as plt
#import ytcreds


# In[22]:


#-------------Build YouTube Search------------#
def youtubeSearch(query, max_results=50,order="relevance", token=None, location=None, location_radius=None):
    #search upto max 50 videos based on query
    search_response = youtube.search().list(
    q=coworking,
    type="video",
    #pageToken=token,
    order = viewCount,
    part="id,snippet",
    maxResults=10
    #location=location,
    #locationRadius=location_radius
    ).execute()
    print("Search Completed...")
    print("Total results: {0} \nResults per page: {1}".format(search_response['pageInfo']['totalResults'], search_response['pageInfo']['resultsPerPage']))
    print("Example output per item, snippet")
    print(search_response['items'][0]['snippet'].keys())
    #Assign first page of results (items) to item variable
    items = search_response['items'] #50 "items"
    #Assign 1st results to title, channelId, datePublished then print
    title = items[0]['snippet']['title']
    channelId = items[0]['snippet']['channelId']
    datePublished = items[0]['snippet']['publishedAt']
    print("First result is: \n Title: {0} \n Channel ID: {1} \n Published on: {2}".format(title, channelId, datePublished))
    return search_response


# In[ ]:





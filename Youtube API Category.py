#!/usr/bin/env python
# coding: utf-8

# In[1]:


api_key = "AIzaSyAprru0SY6bIU1FdHYWaiPreRdE3PRCnoI"


# In[3]:


from apiclient.discovery import build


# In[5]:


youtube = build('youtube', 'v3', developerKey=api_key)


# In[6]:


type(youtube)


# In[23]:


def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos


# In[48]:


res=youtube.videoCategories().list(part="snippet",
                                   id="10").execute()
result=res.get("items",[])


print(res)


# In[54]:


request = youtube.videos().list(
       part="statistics",
       chart="mostPopular",
       maxResults=50,
       regionCode="AU"
   )
response = request.execute()

print(response)


# In[55]:



def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i+50]),
                                   part='statistics').execute()
        stats += res['items']
        
    return stats


# In[56]:


video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], response))


# In[1]:


stats = get_videos_stats(video_ids)


# In[2]:



videos = get_channel_videos('UCkUq-s6z57uJFUFBvZIVTyg')


# In[ ]:





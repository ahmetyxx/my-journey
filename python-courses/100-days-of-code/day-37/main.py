import os
import requests

USERNAME=os.getenv("USERNAME")
TOKEN=os.getenv("TOKEN")

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response=requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    
    "id": "graph1",
    "name": "time graph",
    "unit": "m",
    "type": "int",
    "color": "shibafu"
    
}

headers={
    
    "X-USER-TOKEN":TOKEN
}

response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response.text)



#post a pixel endpoint
#/v1/users/<username>/graphs/<graphID>

a_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

header={
    "X-USER-TOKEN":TOKEN
}

a_pixel_coonfig={
    
    "date":"20261004",
    "quantity":"14"
}

response=requests.post(url=a_pixel_endpoint,headers=header,json=a_pixel_coonfig)
print(response.text)
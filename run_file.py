import requests
import datetime as day_module

# My user details
username = "your username"
token = "my_token"
graph_name = "My study Graph"
graph_id = "firstgraph"
day = day_module.datetime.now().strftime("%Y%m%d")
header = {"X-USER-TOKEN": token}
endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# feedback = requests.post(url=endpoint, json=user_params)
# print(feedback.text)

# my_profile_url = "https://pixe.la/@daswealth"
#
# graph_endpoint = f"{endpoint}/{username}/graphs"
# graph_param = {
#     "id": graph_id,
#     "name": graph_name,
#     "unit": "minutes",
#     "color": "sora",
#     "type": "int"
# }

# graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=header)
# print(graph_response.text)

# CREATE A PIXEL
create_pixel_endpoint = f"{endpoint}/{username}/graphs/{graph_id}/"
pixel_param = {
    "date": day,
    "quantity": input("How many pages did you read today ?\n")
}
pixel_response = requests.post(url=create_pixel_endpoint, json=pixel_param, headers=header)
print(pixel_response.text)

# update_pixel = f"{endpoint}/{username}/graphs/{graph_id}/{day}"
# put_param = {"quantity": "20"}
# put_response = requests.put(url=update_pixel, json=put_param, headers=header)
# print(put_response.text)

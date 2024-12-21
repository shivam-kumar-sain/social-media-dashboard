import requests

def getUserInfo(ACCESS_TOKEN):
    url = "https://graph.instagram.com/me"
    params = {
        "fields": "id,username,account_type,biography,profile_picture_url",
        "access_token": ACCESS_TOKEN
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {'instaUid':data.get('id'),"instProfileImg":data.get("profile_picture_url"),"username":data.get("username")}
    else:
        print("Error:", response.json())

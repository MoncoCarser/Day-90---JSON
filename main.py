import requests, json


for i in range(10):

    #1 we get random user details - first and last name
    results = requests.get("https://randomuser.me/api/")
    if results.status_code == 200:
    
        
        user = results.json()
        name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}"""
    
        #2 we get photo of this random user and save it with name
        image = f"""{user["results"][0]["picture"]["large"]}"""
        picture = requests.get(image)
        f = open(f"{name}.jpg", "wb")
        f.write(picture.content)
        f.close()

        #in case of API access error
    else: 
        print("There was an error accesing the API")
        

# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import requests,

result = requests.get("randomuser.me/api/")
user = result.json() 

for person in user['results']: 
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 

  print(name)

```
<details> <summary> 👀 Answer </summary>

```python
import requests, json # didn't import json

result = requests.get("https://randomuser.me/api/") # missed the full URL
if result.status_code != 200: # No status check
  print("Error, couldn't get API")

user = result.json() 

for person in user['results']: 
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 

  print(name)
```
</details>
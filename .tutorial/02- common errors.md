# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## No Data

👉 What's the problem here?

One of the common problems with json is not getting any data back from the website.  This isn't something you can spot in your code. To check for it, you request a 'status code' from the API. A code of 200 means that all is well.  Here, I've coded in an `if` to generate an error message if the status code isn't 200.

```python
if result.status_code != 200:
  print("Error, couldn't get API")
```




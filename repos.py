import requests
url= "https://api.github.com/orgs/google/repos"
response=requests.get(url)
repos=response.json()
print(" Google open source repositories")
for repo in repos:
  print("Repository name:",repo["name"])
  print("Description:",repo["description"])
  print("URL:",repo["url"])
  print("-" * 30)
  

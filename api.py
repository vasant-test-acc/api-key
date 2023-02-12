import requests
import json
token = "7fc68be982376aca291352b9befa97"

headers = {
    "Authorization" : "token {}".format(token)
}
data = {
  "state" : "close"
}


username = input("Enter your Github username : ")
Repositoryname = input("Enter the name of the repository in which you want to close an issue : ")
issueno = input("Enter the issue number which you want to close : ")
url = "https://api.github.com/repos/{}/{}/issues/{}".format(username,Repositoryname,issueno)
requests.post(url,data=json.dumps(data),headers=headers)

import requests
import random
import json

from holehe.localuseragent import ua


def twitter(email):
    req = requests.get(
        "https://api.twitter.com/i/users/email_available.json",
        params={
            "email": email})
    if req.json()["taken"] == True:
        return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})

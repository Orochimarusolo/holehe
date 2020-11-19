import requests
import random
from bs4 import BeautifulSoup

from holehe.localuseragent import ua

def quizlet(email):
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
    }

    response = requests.get("https://quizlet.com/webapi/3.3/validate-email", headers=headers, params={'email': email})

    try:
        existingAccount = response.json()["responses"][0]["data"]["validateEmail"]["existingAccount"]
        return({"rateLimit": False, "exists": existingAccount != None, "emailrecovery": None, "phoneNumber": None, "others": None})
    except BaseException:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})

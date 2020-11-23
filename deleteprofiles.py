import os
import requests

# Conformity Region, API Key variables
CC_REGION = os.environ.get("CC_REGION", "us-west-2")
CC_APIKEY = os.environ["CC_APIKEY"]

session = requests.session()

url = "https://" + CC_REGION + "-api.cloudconformity.com/v1/profiles"

payload = {}
headers = {
    "Content-Type": "application/vnd.api+json",
    "Authorization": "ApiKey " + CC_APIKEY,
}
response = session.get(url, headers=headers, data=payload)
responsejson = response.json()
data = responsejson["data"]
profileids = [x["id"] for x in data]
for profileid in profileids:
    delprofile = session.delete(url + "/" + profileid, headers=headers, data=payload)
    if delprofile.status_code == 200:
        print("Successfully deleted profile id: {}".format(profileid))
    else:
        print(
            "Warning Received the following status code when trying to delete profile {}:".format(
                profileid
            ),
            delprofile.status_code,
        )
        print(delprofile.json())

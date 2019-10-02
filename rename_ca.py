# importing the requests library 
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Rename Custom Incident Action for Amazon EventBridge')
parser.add_argument('api', type=str, help='PagerDuty API Token')
parser.add_argument('new_name', type=str, help='The new name of the Custom Action for Amazon EventBridge')
args = parser.parse_args()

# defining a params dict for the parameters to be sent to the API

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token=" + str(args.api)
}


def rename(id, newname):
    putURL = "https://api.pagerduty.com/extensions/" + id
    putdata = {'name': newname,
               'extension_schema': {
                   'id': 'PF8FPF1',
                   'type': 'extension_schema_reference',
               }
               }

    #print(json.dumps(putdata))
    #print(putURL)

    putr = requests.put(putURL, data=json.dumps(putdata), headers=HEADERS)

    if (r.status_code != 200):
        print("Error: " + putr.text)
        exit(2)

    return putr.status_code


# api-endpoint
URL = "https://api.pagerduty.com/extensions"
limit = 100
more = True
offset = 0

while more:
    PARAMS = {"limit": limit, "offset": offset}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS, headers=HEADERS)

    if (r.status_code!= 200):
        print("Error: "+r.reason)
        print(r.text)
        exit(2)
    else:
        data = r.json()

        more = data['more']

        for extension in data['extensions']:
            if extension['extension_schema']['summary'] == "Amazon EventBridge":
                print("Changing from \"" + extension['name']+ "\" to \"" + args.new_name + "\"")
                more = False

                rename(extension['id'], args.new_name)

                break

        # printing the output
        # print("Data:%s",data)

        offset = offset + limit

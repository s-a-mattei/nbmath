from itertools import count

import requests
import json
import pandas as pd

url = "https://radius.mathnasium.com/Attendance/StudentRoster_Read"
username = 'samuel.mattei'
password = 'THREE327x!'

payload = {'date': 'Tue,+04+Mar+2025+05:18:46+GMT'}
headers = {
	'host': 'radius.mathnasium.com',
	'Accept': '*/*',
	'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'X-Requested-With': 'XMLHttpRequest',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"macOS"',
	'Cookie': 'VitSecCookie=VSC=9c962e41-0768-4aa0-b619-caf60a0dbe2d; CID=yYkHqNgU09rJDrJLsSGEEEVG3Ptf0zJVobYXjysLg2AAFZ3tEDsC4orYsgGz6bzdR%2ffio3NGPVwQMS3WdC4AhpAwJ74jYA%3d%3d; optimizelyEndUserId=oeu1728598971412r0.04785521189045627; OptanonAlertBoxClosed=2024-11-15T23:24:58.644Z; __RequestVerificationToken=QeZqlzAKhJR0iHSc7rQlivg-ctCXpMjvLCj_meqW_85vrvCj5914HR0aB4cQeIFP4sRH9MLA_9cZD0ODSa64lREFWvGsN25vs3RU4vvgrYo1; optimizelySession=1739912546836; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+18+2025+16%3A02%3A28+GMT-0500+(Eastern+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A0%2CC0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false&geolocation=%3B; cf_clearance=XNPNBNDkk.6Tc6CoVe8z_3K3MThUDE3FVexTwso6ooE-1739912548-1.2.1.1-3_e.KPVRDABIFQ3q8dmTuEvF4pBFrLh73rDLqRDYi6PJa7eoxhnAE9zhGtcfGGeAelMaa.E2.DpZlT8LnYVAx2xhWIpHH5a_tocwJm9c04OUfZiQlHmUDw_pNt.Rq3tMxGpuVmHd5muI0W0YGZu6LmEdIEMkUMMl5qIcrMgtko96FE_Zdopv40YoQlA2pwms3xwXw.nMW0oPaKcR6RKp_V_IK99Z6apFZi0URw6G7yBWmokb5iD4UJv2tT3nafglqCf9FjWZCfGMcrMFLMUlA1OzjR9acq6JLymi7y2KxcQ; WVS=lPTO%2foaCgQqYJJxUfazjF3VmXt%2fjKL%2bSf%2f5Qo4rPjSjPj0dHgFiebpgm2Rl%2bhRFXNDjdjxpBDds8g7ECFziif7ORZAnm0N1tCmtQ1xwL0gIC01neqJtYqZ5Pk1V%2fMwixY%2ffmZZxiTmOGgij9FbEwByygO0YiLOxvKHm2hVNVF9WxN5so9hhxhiJM%2bLrTDOtlpmcuBkDybIJXw8eQ5IDeFrnUeKD%2fmT1M297PLcMmLfa0PdE770amhdrmNE4EuwiqXh9PkAPdDqnPhPJbBxNmVMbdYrwDgMBcP4x%2fcGp0weMgkinv%2bY1g2qR8ZB1SmiYcFSc9nab%2blaFu0fE%3d%2cx7g5we7bl81oyCMHw72yNxwJr5b5QLr0CJOsUkjbiSY%3d; .AspNet.ApplicationCookie=4RGKzuXmULX9Btwa3n7xkN8F04dSF2TxvMKNXS3Qt_vKwzlBotWoKzqD45U_TadnHo43kuJBGWTOftooPwVYAMbMx2tPQtCS4tcX2Fx8wXnxARdMs34A8_TpqCMeABZAGvUPnTYEw-kcgd6oz7EozEEXYBHFvQwyQqe2OaMqXye0pON8zOpBUkkynFbiQl3gTE1mOPbOY4KEzz34nFm2TZJbKh7tAiL-oG-iSQn3wM-Iij2RVCZJQnSRwt-dznvF9NVcSTq4V66QCI_Z4ihdGiQtwZ2XeuDCFd7pQgH4UHrIRrReYhbi24UNYv7BgtjSmEf_XKrk45bvG9pd-r4shOJrs_hEJvkYSsGHjqnd-Xw74KFxg8CHQ-T5nWGdcNg7DqWM2iY7AK1VjRSk7FfjUDaUzxikq3OOM5IAlE-UsC5nNaUyC_wwuofkqM276k9JWjT-q6oAQAMnrNB6yZNvV0nEINdvIlsnBSpsV-sPpT1lgcdmZ4vbGIUIM0uXqMlzL4cbngqPGYvA2H9j3z5inQ; ASP.NET_SessionId=wfkl4k4xbqyfvqelaqivwqjp; Connected=UserConnected; AWSALB=pA2ZpHPv/kj3BIAuoM9exAHjSfz6ZG/P104EaV0aO8gJcQCCHtAdMA/GdRQQBdChTcGUZddVK2lLJZnMrosH71RJr1DXlkUDP/FYVMU0edL8b5uKf08tFnbDDq+W; AWSALBCORS=pA2ZpHPv/kj3BIAuoM9exAHjSfz6ZG/P104EaV0aO8gJcQCCHtAdMA/GdRQQBdChTcGUZddVK2lLJZnMrosH71RJr1DXlkUDP/FYVMU0edL8b5uKf08tFnbDDq+W'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False, auth=(username, password))

# print(response.text)

data = json.loads(response.text)

with open('payload1.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
# Define the fields you want to keep
fields_to_keep = ["StudentID", "StudentFirstName", "StudentLastName", "PrimaryEnrollmentDeliveryType"]

# Create a list of filtered data
filtered_data = []

for item in data["Data"]:
    filtered_item = {field: item[field] for field in fields_to_keep if field in item}
    filtered_data.append(filtered_item)

# Display the filtered data
print(json.dumps(filtered_data, indent=4))

filtered_json = json.dumps(filtered_data, indent=4)

# Save filtered data
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
data = json.dumps(filtered_data, indent=4)
list_title = f"Masterlist/Masterlist_Radius_{timestr}.csv"

df = pd.read_json(filtered_json)

df.to_csv(list_title, encoding='utf-8', index=False)
#
# # Start a session
# with requests.Session() as session:
#     # Log in
#     login_response = session.post(login_url, data=login_payload)
#
#     # Check if login was successful
#     if login_response.status_code == 200:
#         print("Logged in successfully.")
#
#         # Now you can access the target URL with the session
#         response = session.post(target_url, headers=headers, verify=False)
#
#         # Check the response status code
#         print(f"Status Code: {response.status_code}")
#
#         # Print the raw response text
#         print(f"Response Text: {response.text}")
#
#         # If the response is JSON, try to parse it
#         try:
#             json_data = response.json()
#             print(json_data)
#         except requests.exceptions.JSONDecodeError:
#             print("Response is not in JSON format.")
#
#         print(response.headers.get('Content-Type'))
#     else:
#         print("Failed to log in.")

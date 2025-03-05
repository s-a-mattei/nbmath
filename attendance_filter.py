import json

data = 'payload1.json'

# Define the fields you want to keep
fields_to_keep = ["StudentID", "StudentFirstName", "StudentLastName", "PrimaryEnrollmentDeliveryType"]

# Create a list of filtered data
filtered_data = []

for item in data["Data"]:
    filtered_item = {field: item[field] for field in fields_to_keep if field in item}
    filtered_data.append(filtered_item)

# Display the filtered data
print(json.dumps(filtered_data, indent=4))


# Create Attendance: generated AttendanceID in response. In-center: "1" then 1; virtual: "2" then 2
arrive_request= {
      "StudentID": 2563162,
      "AttendanceDate": "Fri, 27 Sep 2024 04:00:00 GMT",
      "ArrivalTime": "Fri, 27 Sep 2024 20:28:00 GMT",
      "DepartureTime": null,
      "EnrollmentID": 2063334,
      "IsRoster": true,
      "RosterUID": "16eb6d11-81da-4606-9b34-6022964a0920",
      "RosterArrivalTimePickerId": "#TimePicker_Arrival_2563162_null_2063334",
      "RosterDepartureTimePickerId": "#TimePicker_Departure_2563162_null_2063334",
      "HybridDeliveryOption": "1"
}

depart_request = {
      "StudentID": 2563162,
      "AttendanceDate": "Fri, 27 Sep 2024 04:00:00 GMT",
      "ArrivalTime": "Fri, 27 Sep 2024 20:28:00 GMT",
      "DepartureTime": "Fri, 27 Sep 2024 21:28:00 GMT",
      "AttendanceID": 68833660,
      "EnrollmentID": 2063334,
      "IsRoster": true,
      "RosterUID": "16eb6d11-81da-4606-9b34-6022964a0920",
      "RosterArrivalTimePickerId": "#TimePicker_Arrival_2563162_68833660_2063334",
      "RosterDepartureTimePickerId": "#TimePicker_Departure_2563162_68833660_2063334",
      "HybridDeliveryOption": 1
}

import requests
import json

# Your base URL for the Radius requests
url_create = "https://radius.mathnasium.com/Attendance/CreateAttendanceRoster"
url_update = "https://radius.mathnasium.com/Attendance/UpdateAttendanceRoster"

# Authentication credentials
username = "zzzz"
password = "zzzz"

# Headers - these should match what you use in Proxyman/Postman
headers = {
    'host': 'radius.mathnasium.com',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'your_cookies_here'
}

# Example of adding attendance for a specific student
payload_create = {
    "StudentID": 442171,
    "AttendanceDate": "Fri, 27 Sep 2024 04:00:00 GMT",
    "ArrivalTime": "Fri, 27 Sep 2024 21:00:00 GMT",
    "DepartureTime": None,
    "EnrollmentID": 1600270,
    "HybridDeliveryOption": 2,  # Virtual
    "IsRoster": True
}

# Make the POST request to create attendance
response_create = requests.post(url_create, headers=headers, json=payload_create, auth=(username, password))
create_response_data = response_create.json()

# Output the response for inspection
print(json.dumps(create_response_data, indent=4))

# Check if the AttendanceID is generated and stored
attendance_id = create_response_data.get('AttendanceID')

if attendance_id:
    print(f"Attendance created successfully with ID: {attendance_id}")

    # Example of updating the attendance with a departure time
    payload_update = {
        "StudentID": 442171,
        "AttendanceID": attendance_id,  # Use the returned AttendanceID
        "AttendanceDate": "Fri, 27 Sep 2024 04:00:00 GMT",
        "ArrivalTime": "Fri, 27 Sep 2024 21:00:00 GMT",
        "DepartureTime": "Fri, 27 Sep 2024 22:00:00 GMT",  # Adding a departure time
        "HybridDeliveryOption": 2  # Virtual
    }

    # Make the POST request to update attendance
    response_update = requests.post(url_update, headers=headers, json=payload_update, auth=(username, password))
    update_response_data = response_update.json()

    # Output the update response for inspection
    print(json.dumps(update_response_data, indent=4))

else:
    print("Failed to create attendance.")

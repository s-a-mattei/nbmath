import requests
import json

# Constants for URLs
url_roster_read = "https://radius.mathnasium.com/Attendance/StudentRoster_Read"
url_create_attendance = "https://radius.mathnasium.com/Attendance/CreateAttendanceRoster"
url_update_attendance = "https://radius.mathnasium.com/Attendance/UpdateAttendanceRoster"
payload = {}

# Credentials for authentication
username = 'samuel.mattei'
password = 'THREE327x!'

# Headers for requests
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


# Fetch existing attendance data from Radius
def fetch_student_roster():
    response = requests.post(url_roster_read, headers=headers, data=payload, verify=False, auth=(username, password))
    # response = requests.request("POST", url, headers=headers, data=payload, verify=False, auth=(username, password))

    data = json.loads(response.text)

    # Save the raw data (optional)
    with open('payload1.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return data



# Check if attendance exists for a given student on a specific date
def check_attendance_exists(student_id, attendance_data, target_date):
    for entry in attendance_data:
        if entry.get("StudentID") == student_id and entry.get("AttendanceDate") == target_date:
            return entry.get("AttendanceID")
    return None

#
# # Add attendance (create entry)
# def add_attendance(student_id, arrival_time, date, delivery_option):
#     payload = {
#         "StudentID": student_id,
#         "ArrivalTime": arrival_time,
#         "AttendanceDate": date,
#         "HybridDeliveryOption": delivery_option
#     }
#
#     response = requests.post(url_create_attendance, headers=headers, data=payload, verify=False,
#                              auth=(username, password))
#
#     # Parse the response to get AttendanceID (check for success/failure)
#     if response.status_code == 200:
#         attendance_id = json.loads(response.text).get("AttendanceID")
#         print(f"Attendance added. AttendanceID: {attendance_id}")
#         return attendance_id
#     else:
#         print(f"Failed to add attendance for StudentID {student_id}. Status: {response.status_code}")
#         return None
#
#
# # Update attendance (e.g., add departure time)
# def update_attendance(attendance_id, departure_time, delivery_option):
#     payload = {
#         "AttendanceID": attendance_id,
#         "DepartureTime": departure_time,
#         "HybridDeliveryOption": delivery_option
#     }
#
#     response = requests.post(url_update_attendance, headers=headers, data=payload, verify=False,
#                              auth=(username, password))
#
#     if response.status_code == 200:
#         print(f"Attendance updated successfully for AttendanceID: {attendance_id}")
#     else:
#         print(f"Failed to update attendance for AttendanceID {attendance_id}. Status: {response.status_code}")

# Step 1: Fetch the current attendance roster to check for existing attendance
def check_existing_attendance(student_id, attendance_date_string):
    payload = {}

    # Send the POST request
    response = requests.post(url_roster_read, headers=headers, data=payload, verify=False, auth=(username, password))

    # Debug: Print the status code and raw response content
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")  # Print raw text to inspect

    # Check if response is JSON
    try:
        data = response.json()
        date_string = attendance_date_string.replace('/','-')
        with open(f'payload_{date_string}.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Response JSON: {json.dumps(data, indent=4)}")  # Print parsed JSON for inspection

        for record in data['Data']:
            if record['StudentID'] == student_id and record['AttendanceDateString'] == attendance_date_string:
                print(f"Attendance already exists for {record['StudentFirstName']} {record['StudentLastName']}")
                return record  # Return the existing record with AttendanceID
        return None  # If attendance doesn't exist

    except requests.exceptions.JSONDecodeError:
        print("Failed to parse JSON. Response might not be in JSON format.")
        return None

# Step 2: Add new attendance if it doesn't exist
import requests
import json


# Create attendance record
def create_attendance_record(student_id, attendance_date, arrival_time, hybrid_delivery_option, headers):
    url_create = "https://radius-system.com/api/Attendance/CreateAttendanceRoster"
    payload = {
        "StudentID": student_id,
        "AttendanceDate": attendance_date,  # Format like "Fri, 27 Sep 2024 04:00:00 GMT"
        "ArrivalTime": arrival_time,  # Format like "Fri, 27 Sep 2024 21:00:00 GMT"
        "DepartureTime": None,  # Leave as None for now
        "HybridDeliveryOption": hybrid_delivery_option  # 1 for in-center, 2 for virtual
    }

    response = requests.post(url_create, headers=headers, json=payload, auth=(username, password), verify=False)

    if response.status_code == 200:
        print("Attendance record created successfully.")
        return response.json()  # This will contain the response with a generated AttendanceID
    else:
        print(f"Failed to create attendance: {response.status_code} - {response.text}")
        return None


# Example usage
student_id = 442171
attendance_date = "Fri, 27 Sep 2024 04:00:00 GMT"
arrival_time = "Fri, 27 Sep 2024 21:00:00 GMT"
hybrid_delivery_option = 2

create_response = create_attendance_record(student_id, attendance_date, arrival_time, hybrid_delivery_option, headers)


# Fetch student roster to get the system-generated AttendanceID
def fetch_attendance_record(student_id, attendance_date_string, headers):
    url_roster_read = "https://radius-system.com/api/Attendance/StudentRoster_Read"
    params = {
        "StudentID": student_id,
        "AttendanceDateString": attendance_date_string  # The date in "MM/DD/YYYY" format
    }

    response = requests.get(url_roster_read, headers=headers, params=params, auth=(username, password), verify=False)

    if response.status_code == 200:
        data = response.json()
        for record in data:
            if record['StudentID'] == student_id:
                return record['AttendanceID']
        print("Attendance record not found.")
    else:
        print(f"Failed to fetch attendance record: {response.status_code} - {response.text}")

    return None


# # Example usage
# attendance_date_string = "09/27/2024"  # The date in "MM/DD/YYYY" format
# attendance_id = fetch_attendance_record(student_id, attendance_date_string, headers)
# print("Retrieved AttendanceID:", attendance_id)
#

# Step 3: Update attendance with departure time
def update_attendance(student_id, attendance_id, attendance_date, arrival_time, departure_time, hybrid_delivery_option):
    payload = {
        "StudentID": student_id,
        "AttendanceID": attendance_id,
        "AttendanceDate": attendance_date,
        "ArrivalTime": arrival_time,
        "DepartureTime": departure_time,  # Now setting the departure time
        "HybridDeliveryOption": hybrid_delivery_option  # 1 for in-center, 2 for virtual
    }
    response = requests.post(url_update_attendance, headers=headers, json=payload, auth=(username, password))
    update_response_data = response.json()

    if response.status_code == 200:
        print("Attendance record updated successfully.")
    else:
        print(f"Failed to update attendance: {response.status_code} - {response.text}")

    # Output the update response for inspection
    print("Update Attendance Response:", json.dumps(update_response_data, indent=4))

# Main operation: check, add, and update attendance
def manage_attendance(student_id, attendance_date, arrival_time, departure_time, hybrid_delivery_option):
    # Format date for checking attendance
    attendance_date_string = attendance_date.split(" ")[2]  # Extract just the date (e.g., "27 Sep 2024")

    # Step 1: Check if attendance already exists
    existing_attendance = check_existing_attendance(student_id, attendance_date_string)

    if existing_attendance:
        attendance_id = existing_attendance['AttendanceID']
        print(f"Updating existing attendance record with ID {attendance_id}")
        # Step 3: Update attendance if it exists
        update_attendance(student_id, attendance_id, attendance_date, arrival_time, departure_time, hybrid_delivery_option)
    else:
        # Step 2: Add attendance if it doesn't exist
        attendance_id = create_attendance_record(student_id, attendance_date, arrival_time, hybrid_delivery_option)
        if attendance_id:
            # After adding, update attendance with departure time
            update_attendance(student_id, attendance_id, attendance_date, arrival_time, departure_time, hybrid_delivery_option)

# Example usage
student_id = 2563162
attendance_date = "Fri, 27 Sep 2024 04:00:00 GMT"  # Fixed 04:00:00 time for the date
arrival_time = "Fri, 27 Sep 2024 21:00:00 GMT"     # Example arrival time
departure_time = "Fri, 27 Sep 2024 22:00:00 GMT"   # Example departure time
hybrid_delivery_option = 2  # 1 for in-center, 2 for virtual

# Manage the attendance process
# manage_attendance(student_id, attendance_date, arrival_time, departure_time, hybrid_delivery_option)
# Step 1: Fetch the current attendance roster to check for existing attendance

#
# attendance_date_string = "9/27/2024"
# check_existing_attendance(student_id, attendance_date_string)

# Main function to orchestrate the logic
def main():
    # Step 1: Fetch student roster
    data = fetch_student_roster()

    # Step 2: Filter data to focus on specific fields
    filtered_data = filter_data(data)

    # Step 3: For each student, check if attendance exists for the target date
    target_date = "2024-09-27T04:00:00"  # Example date (GMT fixed time)
    arrival_time = "10:00:00"  # Example arrival time
    departure_time = "12:00:00"  # Example departure time
    delivery_option = "1"  # In-center (example)

    for student in filtered_data:
        student_id = student["StudentID"]

        attendance_id = check_attendance_exists(student_id, data["Data"], target_date)

        if attendance_id:
            # If attendance exists, update it
            update_attendance(attendance_id, departure_time, delivery_option)
        else:
            # If attendance does not exist, create a new entry
            attendance_id = create_attendance_record(student_id, arrival_time, target_date, delivery_option)

            if attendance_id:
                update_attendance(attendance_id, departure_time, delivery_option)


# # Run the main operation
# if __name__ == "__main__":
#     main()

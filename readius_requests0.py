import json
import requests

def fetch_student_roster(url, username, password):
    """
    Fetches the student roster from the server.

    Args:
    - url (str): The API endpoint for fetching the student roster.
    - username (str): The username for authentication.
    - password (str): The password for authentication.

    Returns:
    - list: List of students from the roster, or None if an error occurs.
    """
    try:
        response = requests.get(url, auth=(username, password), verify=False)  # Make sure to handle SSL warnings in production
        response.raise_for_status()
        return response.json()  # Return the parsed JSON response

    except requests.exceptions.RequestException as e:
        print(f"Error fetching student roster: {e}")
        return None

def extract_enrollment_id(roster_data, student_id):
    """
    Extracts the PrimaryEnrollmentID for a given student from the roster data.

    Args:
    - roster_data (dict): The roster data containing student information.
    - student_id (int): The ID of the student to look for.

    Returns:
    - int: The PrimaryEnrollmentID if found, None otherwise.
    """
    for record in roster_data['Data']:
        if record['StudentID'] == student_id:
            return record.get('PrimaryEnrollmentId')  # Return the enrollment ID
    return None  # Return None if student ID is not found



def build_attendance_payload(student_id, enrollment_id, attendance_date, arrival_time, departure_time, is_roster=True):
    """
    Builds the payload for the attendance record.

    Args:
    - student_id (int): The ID of the student.
    - enrollment_id (int): The enrollment ID of the student.
    - attendance_date (str): The date of attendance in the format 'Day, DD Mon YYYY HH:MM:SS GMT'.
    - arrival_time (str): The arrival time in the same format.
    - departure_time (str): The departure time or None if not applicable.
    - is_roster (bool): Indicates if the record is part of a roster.

    Returns:
    - dict: The constructed payload for the attendance record.
    """
    payload = {
        "StudentID": student_id,
        "AttendanceDate": attendance_date,
        "ArrivalTime": arrival_time,
        "DepartureTime": departure_time,
        "EnrollmentID": enrollment_id,
        "IsRoster": is_roster,
        "RosterUID": "some_unique_id",  # Replace with actual RosterUID if needed
        "RosterArrivalTimePickerId": f"#TimePicker_Arrival_{student_id}_null_{enrollment_id}",
        "RosterDepartureTimePickerId": f"#TimePicker_Departure_{student_id}_null_{enrollment_id}",
        "HybridDeliveryOption": "1"  # Adjust as necessary for your needs
    }
    return payload


def create_attendance_record(url, token, username, password, payload):
    """
    Sends a POST request to create a new attendance record.

    Args:
    - url (str): The API endpoint for creating attendance.
    - token (str): The authorization token.
    - username (str): The username for authentication.
    - password (str): The password for authentication.
    - payload (dict): The payload for the attendance record.

    Returns:
    - dict: The response from the server if successful, None otherwise.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, verify=False, auth=(username, password))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response data as JSON

    except requests.exceptions.RequestException as e:
        print(f"Error creating attendance record: {e}")
        return None

# Example Usage
roster_url = "https://radius.mathnasium.com/StudentRoster_Read"  # Replace with actual URL
url_create_attendance = "https://radius.mathnasium.com/Attendance/CreateAttendanceRoster"  # Replace with actual URL
token = "your_token"  # Replace with your actual token
username = "your_username"
password = "your_password"

# Fetch the roster data
roster_data = fetch_student_roster(roster_url, username, password)

if roster_data:
    # Example student ID to look for
    student_id = 2563162  # Replace with actual student ID

    # Extract the PrimaryEnrollmentID for the student
    enrollment_id = extract_enrollment_id(roster_data, student_id)

    if enrollment_id:
        print(f"Enrollment ID for Student ID {student_id}: {enrollment_id}")

        # Prepare to create the attendance record
        attendance_date = "Fri, 27 Sep 2024 04:00:00 GMT"  # Use actual date
        arrival_time = "Fri, 27 Sep 2024 20:21:00 GMT"
        departure_time = None  # Set to None if not applicable

        # Build the payload
        payload = build_attendance_payload(student_id, enrollment_id, attendance_date, arrival_time, departure_time)

        # Create the attendance record
        response = create_attendance_record(url_create_attendance, token, username, password, payload)

        if response:
            print("Attendance record created successfully:")
            print(json.dumps(response, indent=4))  # Pretty print the response
    else:
        print(f"No enrollment ID found for Student ID {student_id}.")
else:
    print("Failed to fetch roster data.")

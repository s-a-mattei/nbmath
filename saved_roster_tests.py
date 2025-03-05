import json


# Load the saved roster data
def load_roster_data(filename):
    # with open(filename, 'r') as json_file:
    #     return json.load(json_file)
    try:
        with open(filename, 'r') as file:
            roster_data = json.load(file)
            print("Roster data loaded successfully.")
            return roster_data
    except FileNotFoundError:
        print(f"File {filename} not found. Initializing empty roster data.")
        return {'Data': []}  # Initialize an empty list for records
    except json.JSONDecodeError:
        print("Failed to parse JSON. File might not be in the correct format.")
        return {'Data': []}


# Example usage
filename = "roster_short.json"
roster_data = load_roster_data(filename)
# print("Loaded roster data:", roster_data)


def check_existing_attendance(student_id, attendance_date_string, filename):
    # Load the saved roster file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        student_name = None

        # First, find the student name based on the entered student_id
        for record in data['Data']:
            if record['StudentID'] == student_id:
                student_name = f"{record['StudentFirstName']} {record['StudentLastName']}"
                break  # We found the student's name, no need to keep looping

        # If no student found, return "no"
        if not student_name:
            print(f"No student found with ID {student_id}.")
            return "no", None, None

        # Loop through each record to check for a match
        for record in data['Data']:
            if record['StudentID'] == student_id and record['AttendanceDateString'] == attendance_date_string:
                arrival_time = record.get('ArrivalTimeString', 'N/A')
                departure_time = record.get('DepartureTimeString', 'N/A')
                print(f"Attendance exists for {record['StudentFirstName']} {record['StudentLastName']}:")
                print(attendance_date_string + f" Arrival Time: {arrival_time}, Departure Time: {departure_time}")
                return record['AttendanceID'], arrival_time, departure_time  # Return attendance and times

            # If no match is found for attendance
        print(f"No attendance record found for {student_name} on {attendance_date_string}")
        return "no", None, None

    except json.JSONDecodeError:
        print("Failed to parse JSON. File might not be in the correct format.")
        return "no", None, None
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return "no", None, None


def create_attendance_record(roster_data, new_record):
    # Append the new record to the roster data
    roster_data['Data'].append(new_record)
    print(f"Added new attendance record for student ID: {new_record['StudentID']}")
    with open(filename, 'w') as file:
        json.dump(roster_data, file, indent=4)
        print(f"Roster data saved to {filename}.")
    return roster_data

# Example new record
new_record = {
    "StudentID": 1339809,
    "AttendanceDateString": "9/28/2024",
    "ArrivalTimeString": "10:00 AM",
    "DepartureTimeString": None,
    "AttendanceID": 99999999,
    "IsRoster": True
}

# Add the new record
roster_data = create_attendance_record(roster_data, new_record)

def update_attendance_record(roster_data, student_id, new_departure_time):
    # Search for the student's attendance record and update it
    for record in roster_data:
        if record['StudentID'] == student_id:
            record['DepartureTimeString'] = new_departure_time
            print(f"Updated departure time for student ID: {student_id}")
            return roster_data

    print(f"No record found for student ID: {student_id}")
    return roster_data

# Example update
# student_id_to_update = 442171
# new_departure_time = "11:00 AM"

# Update the departure time
# roster_data = update_attendance_record(roster_data, student_id_to_update, new_departure_time)

def save_roster_data(filename, roster_data):
    with open(filename, 'w') as json_file:
        json.dump(roster_data, json_file, indent=4)
    print(f"Roster data saved to {filename}")

# Save the modified roster data
# save_roster_data(filename, roster_data)
check_existing_attendance(442171, "9/27/2024", filename=filename)
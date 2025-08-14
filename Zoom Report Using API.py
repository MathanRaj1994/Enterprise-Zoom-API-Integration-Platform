import requests
import pandas as pd
import base64
import json
import ast
#import urllib.parse
from datetime import datetime
from typing import Dict, List, Optional
#======================================================Token & ID ============================================================#
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
ACCOUNT_ID = "ACCOUNT_ID"
auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_bytes = base64.b64encode(auth_string.encode("utf-8"))
auth_header = auth_bytes.decode("utf-8")

all_participants = pd.DataFrame()

#===================================================== Request token ========================================================#
url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={ACCOUNT_ID}"
headers = {
    "Authorization": f"Basic {auth_header}"
}
response = requests.post(url, headers=headers)
account=response.json()
ACCESS_TOKEN=account['access_token']

#======================================================Meeting List ============================================================#
url_meetings = "https://api.zoom.us/v2/users/me/meetings?type=past"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
response = requests.get(url_meetings, headers=headers)
Data = response.json()
if "meetings" in Data:
    meeting_list = pd.DataFrame(Data["meetings"])
    output_file = r"File_path\zoom_Meeting.xlsx"
    meeting_list.to_excel(output_file, index=False)
    print(f"Meetings list saved to {output_file}")
else:
    print("No meeting data found.")
#====================================================== Meeting participants ============================================================#
if "meetings" in Data:
    for item in Data["meetings"]:
        meeting_id = item["id"]
        topic= item["topic"]
        start_time= item["start_time"]
        uuid=item["uuid"]
#-----------------------------------------------------------------------------------------------------------------------------------------#
        url = f"https://api.zoom.us/v2/report/meetings/{meeting_id}/participants"
        meeting_response = requests.get(url, headers=headers)
        data = meeting_response.json()

        #print(f"Meeting ID: {meeting_id}")
        
        if "participants" in data:
            df = pd.DataFrame(data["participants"])
            df["meeting_id"] = meeting_id
            df["topic"] = topic
            df["start_time"]=start_time
            df.rename(columns={
            "start_time": "Meeting_Date"
            }, inplace=True)
            df["Meeting_Date"] = pd.to_datetime(df["Meeting_Date"]).dt.date
            all_participants = pd.concat([all_participants, df], ignore_index=True)
        else:
            print("No participants data found.")
output_file = r"File_path\zoom_participants.csv"
all_participants.to_csv(output_file, index=False)
print(all_participants)
#====================================================== Meeting Polls ============================================================#
url = f"https://api.zoom.us/v2/report/meetings/{meeting_id}/polls"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()
if "questions" in data:
    poll_df = pd.DataFrame(data["questions"])
    poll_df.to_csv(r"File_path\meeting_poll_report.csv", index=False)
    print("Poll report saved as meeting_poll_report.csv")
else:
    print("No poll data found:", data)
#====================================================== Meeting survey ============================================================#

url=f'https://api.zoom.us/v2/report/meetings/{meeting_id}/survey'

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
resp = requests.get(url, headers=headers)
data = resp.json() 
print(resp.status_code, data)
print(data)


if "questions" in data and data["questions"]:
    survey_df = pd.DataFrame(data["questions"])
    survey_df.to_csv(r"File_path\meeting_survey_report.csv", index=False)
    print("Survey report saved.")
elif "questions" in data and not data["questions"]:
    print("Meeting found, but no survey responses exist.")
else:
    print("Error:", data)

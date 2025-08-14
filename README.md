# 📊 Zoom API Data Extraction Script

**## 📌 1. Introduction**
This Python script connects to the **Zoom API** using the **Server-to-Server OAuth** authentication method to retrieve various meeting-related reports, including:

- ✅ Past meetings  
- ✅ Participant lists  
- ✅ Polls  
- ✅ Surveys  

The script saves the extracted data into **Excel** and **CSV** files for further analysis.

---

**## ⚙️ 2. Prerequisites**
Before running the script, ensure that you have:

1. A **Zoom account with admin privileges**.
2. A **Server-to-Server OAuth app** created in the [Zoom App Marketplace](https://marketplace.zoom.us/).
3. **Python 3.x** installed on your system.
4. The following Python libraries installed:

pip install requests pandas openpyxl
##🔑 3. Getting API Credentials
Follow these steps to get your API credentials:
Log in to the Zoom App Marketplace.
Click Develop → Build App.
Select Server-to-Server OAuth and click Create.
Fill in the required information (App name, company name, etc.).
Under App Credentials, copy:
Client ID
Client Secret
Account ID
Under Scopes, add:
meeting:read
meeting:read:admin
report:read:admin
user:read
Activate your app.

**##🛠 4. Script Workflow**

The script is divided into several sections:

Token Request – Retrieves an OAuth token using account credentials.

Meeting List – Fetches a list of past meetings for the authenticated user.

Meeting Participants – Retrieves participant lists for each meeting.

Meeting Polls – Retrieves poll data for each meeting.

Meeting Surveys – Retrieves survey results for each meeting.

**##🚀 5. How to Run**

Open the script file and replace:
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
ACCOUNT_ID = "YOUR_ACCOUNT_ID"

Update the output file paths in the script to match your desired location.
Run the script:
python zoom_reports.py
The script will save:
zoom_Meeting.xlsx → List of past meetings
zoom_participants.csv → Participant details
meeting_poll_report.csv → Poll data (if available)
meeting_survey_report.csv → Survey data (if available)

**##📂 6. Output Files**
File Name	Description
zoom_Meeting.xlsx	List of past meetings
zoom_participants.csv	Participants for each meeting
meeting_poll_report.csv	Poll data (if available)
meeting_survey_report.csv	Survey data (if available)

**##📝 7. Notes**
If no meetings are found, make sure your account has hosted past meetings.
If participant or poll data is missing, ensure the meeting had these features enabled.
Zoom API rate limits may apply — check the Zoom API Documentation for details.

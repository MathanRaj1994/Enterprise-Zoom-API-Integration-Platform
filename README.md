# 📊 Zoom API Data Extraction Script

**📌 1. Introduction**</p>
This Python script connects to the **Zoom API** using the **Server-to-Server OAuth** authentication method to retrieve various meeting-related reports, including:

- ✅ Past meetings  
- ✅ Participant lists  
- ✅ Polls  
- ✅ Surveys  

The script saves the extracted data into **Excel** and **CSV** files for further analysis.</p>

---

**⚙️ 2. Prerequisites**</p>
Before running the script, ensure that you have:

1. A **Zoom account with admin privileges**.</p>
2. A **Server-to-Server OAuth app** created in the [Zoom App Marketplace](https://marketplace.zoom.us/).</p>
3. **Python 3.x** installed on your system.</p>
4. The following Python libraries installed:</p>

---
pip install requests pandas openpyxl</p>
**🔑 3. Getting API Credentials**</p>
Follow these steps to get your API credentials:</p>
Log in to the Zoom App Marketplace.</p>
Click Develop → Build App.</p>
Select Server-to-Server OAuth and click Create.</p>
Fill in the required information (App name, company name, etc.).</p>
Under App Credentials, copy:</p>
Client ID</p>
Client Secret</p>
Account ID</p>
Under Scopes, add:</p>
meeting:read</p>
meeting:read:admin</p>
report:read:admin</p>
user:read</p>
Activate your app.</p>

---
**🛠 4. Script Workflow**</p>

The script is divided into several sections:</p>
Token Request – Retrieves an OAuth token using account credentials.</p>
Meeting List – Fetches a list of past meetings for the authenticated user.</p>
Meeting Participants – Retrieves participant lists for each meeting.</p>
Meeting Polls – Retrieves poll data for each meeting.</p>
Meeting Surveys – Retrieves survey results for each meeting.</p>

---
**🚀 5. How to Run**</p>

Open the script file and replace:</p>
**CLIENT_ID** = "YOUR_CLIENT_ID"</p>
**CLIENT_SECRET** = "YOUR_CLIENT_SECRET"</p>
**ACCOUNT_ID** = "YOUR_ACCOUNT_ID"</p>
Update the output file paths in the script to match your desired location.</p>
Run the script:</p>
python zoom_reports.py</p>
The script will save:</p>
zoom_Meeting.xlsx → List of past meetings</p>
zoom_participants.csv → Participant details</p>
meeting_poll_report.csv → Poll data (if available)</p>
meeting_survey_report.csv → Survey data (if available)</p>

---
**📂 6. Output Files**</p>
File Name	Description</p>
zoom_Meeting.xlsx	List of past meetings</p>
zoom_participants.csv	Participants for each meeting</p>
meeting_poll_report.csv	Poll data (if available)</p>
meeting_survey_report.csv	Survey data (if available)</p>

---
**📝 7. Notes**</p>
If no meetings are found, make sure your account has hosted past meetings.</p>
If participant or poll data is missing, ensure the meeting had these features enabled.</p>
Zoom API rate limits may apply — check the Zoom API Documentation for details.</p>

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDF_DIR = os.path.join(BASE_DIR, "raw_sources", "pdfs")

os.makedirs(PDF_DIR, exist_ok=True)


styles = getSampleStyleSheet()
style = styles["Normal"]


def create_pdf(filename, content):
    file_path = os.path.join(PDF_DIR, filename)

    doc = SimpleDocTemplate(file_path, pagesize=letter)
    story = []

    for paragraph in content.split("\n\n"):
        story.append(Paragraph(paragraph, style))
        story.append(Spacer(1, 12))

    doc.build(story)

    print(f"Created: {file_path}")

remote_work_policy = """
ACME CORPORATION - REMOTE WORK POLICY (2026)

1. PURPOSE
This policy defines eligibility and operational guidelines for remote work across Acme Corporation.

2. ELIGIBILITY
Employees are eligible for remote work based on role classification, manager approval, and performance standing.

3. REMOTE WORK LIMITS
Employees may work remotely up to 3 days per week unless explicitly approved for extended remote arrangements.

4. CORE HOURS REQUIREMENT
All remote employees must maintain availability between 10:00 AM and 4:00 PM local time.

5. EQUIPMENT AND SECURITY
Company-issued devices must be used for all remote work. Personal devices are not permitted for accessing internal systems.

6. DATA HANDLING
Employees must not store or process sensitive company data on unsecured local environments.

7. APPROVAL PROCESS
Remote work requests must be approved by the direct manager and recorded in the HR system.

8. COMPLIANCE
Violation of remote work policy may result in suspension of remote privileges or disciplinary action.
"""

leave_policy = """
ACME CORPORATION - LEAVE POLICY (2026)

1. PURPOSE
This document defines leave entitlement and approval procedures for employees.

2. ANNUAL LEAVE
Employees are entitled to 20 paid leave days per year.

3. SICK LEAVE
Employees are entitled to 10 sick leave days annually, subject to manager notification.

4. BEREAVEMENT LEAVE
Employees may avail up to 5 days of bereavement leave.

5. LEAVE CARRY FORWARD
A maximum of 5 unused annual leave days may be carried forward to the next calendar year.

6. PROBATION PERIOD RULES
Employees on probation are eligible for prorated leave benefits only.

7. APPROVAL WORKFLOW
All leave requests must be approved by the reporting manager in the HR system.

8. EXCEPTIONS
Emergency leave requests may be reviewed post-facto in exceptional cases.
"""

if __name__ == "__main__":
    create_pdf("remote_work_policy.pdf", remote_work_policy)
    create_pdf("leave_policy.pdf", leave_policy)
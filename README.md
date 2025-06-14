Job Portal – Django Project

A professional Job Portal web application built using **Django**. This platform enables **companies** to post jobs and manage listings, and allows **users** to browse, view details, and apply for jobs with their resume and cover letter.

---

Features
User & Admin Authentication (Login/Logout)
Company Management (Add, Update, View)
Post and Manage Job Listings (Title, Description, Location, Salary, etc.)
User Dashboard to Track Applications
Job Application with Resume Upload
Admin Dashboard to View Applications
Professionally Styled Frontend (CSS, fonts, colors for a clean UI)

---

Tech Stack

- Python 3.x
- Django 5.x
- SQLite (default database)
- HTML, CSS (Responsive UI)
- Bootstrap (optional – for styling, if added)
- Git/GitHub for version control

---

Installation & Setup

1. Clone the repository:

bash
git clone https://github.com/parul65/job-portal.git
cd job-portal

2. On Windows
python -m venv venv
venv\Scripts\activate

On macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py makemigrations
python manage.py migrate

5. How to Run the Project
python manage.py runserver

Open your browser and visit:
Admin Panel (for superuser)
URL:
http://127.0.0.1:8000/admin/ (USERNAME - KIIT  PASSWORD - Parul@1966)
User Login
URL:
http://127.0.0.1:8000/user/login/ (USERNAME - parul  PASSWORD - newpassword123)

6. USUAGE : 
6.1 Admin
Go to the Django admin panel: http://127.0.0.1:8000/admin/ 
Login using your superuser credentials.

You can:
Add and manage Companies.
Post and manage Job Listings.
View and manage all Job Applications.

6.2 User
Go to the user login page: http://127.0.0.1:8000/user/login/ 
Login or register to access your dashboard.

On the homepage, users can:
View available jobs with details like title, description, company, and salary.
Click “Apply” on any job listing to:
Submit name, email, cover letter, and upload resume (PDF format).
View all their submitted applications from their dashboard.

License
This project is licensed under the MIT License.

Contact
Your Name - parul.kumari1966@gmail.com
GitHub: https://github.com/parul65


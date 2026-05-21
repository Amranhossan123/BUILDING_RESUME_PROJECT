# Resume Builder Web Application using Django

This project is a simple Resume Builder Web Application developed with Django.  
Users can create, view, update, and delete resumes with profile information, education history, work experience, skills, certifications, projects, and references.

---

# Features

## Resume Management (CRUD)
- Add Resume
- View Resume
- Update Resume
- Delete Resume

## Resume Information
- Profile Picture Upload
- Full Name
- Address
- Phone Number
- Email Address
- Career Objective
- Skills
- Certifications
- Projects
- References

## Education Information
- Degree
- Institution
- Graduation Year

## Work Experience
- Company Name
- Position
- Start Date
- End Date

---

# Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite3

---

# Project Structure

```bash
ResumeBuilder/
│
├── resumeApp/
│   ├── migrations/
│   ├── templates/
│   │   ├── resume.html
│   │   ├── addResume.html
│   │   ├── editResume.html
│   │   └── viewResume.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media/
├── db.sqlite3
├── manage.py
└── README.md

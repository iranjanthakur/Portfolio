from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint("main", __name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")

# Home page
@main_bp.route("/")
def home():
    return render_template("index.html", name="Ranjan Thakur", title="Python Developer")

# About page
@main_bp.route("/about")
def about():
    about_info = {
        "profile": "Enthusiastic Python Developer seeking a challenging role in a forward-thinking tech company. "
                   "Proficient in Python, Django, Flask, and SQL with hands-on experience in building web applications and APIs. "
                   "Passionate about learning new technologies, solving problems, and delivering clean, scalable solutions.",
        "skills": {
            "technical": ["Python", "Django", "Flask", "SQL", "REST API", "HTML", "CSS", "JavaScript", "Git"],
            "tools": ["VS Code", "GitHub", "MySQL", "PostgreSQL", "Docker (basic)", "AWS basics"]
        },
        "certifications": [
            "Python Fundamentals – Aug’25",
            "Flask Full Stack Development – Jul’25",
            "SQL (Basic) – Jul’25"
        ]
    }
    return render_template("about.html", about=about_info)

# Projects page
@main_bp.route("/projects")
def projects():
    project_list = [
        {
            "title": "Weather App (CLI-Based)",
            "duration": "11/24 – 12/24",
            "description": [
                "Developed a weather forecasting app using OpenWeatherMap API and Python.",
                "Integrated real-time API data and displayed using Tkinter GUI."
            ],
            "github": "#"
        },
        {
            "title": "School Management System",
            "duration": "07/24 – 08/24",
            "description": [
                "Developed a responsive front-end web application using HTML5, CSS3 (Flexbox & Grid) and JavaScript.",
                "Created functionalities like login, dashboard, student & teacher management, attendance tracking, notice."
            ],
            "github": "#"
        }
    ]
    return render_template("projects.html", projects=project_list)

# Resume page
@main_bp.route("/resume")
def resume():
    resume_data = {
        "name": "Ranjan Thakur",
        "title": "Python Developer",
        "contact": {
            "phone": "+91 9142145152",
            "email": "ranjanreignsthakur@gmail.com",
            "portfolio": "#",
            "github": "https://github.com/yourusername",
            "linkedin": "https://linkedin.com/in/ranjanthakur"
        },
        "profile": "Enthusiastic Python Developer seeking a challenging role in a forward-thinking tech company. "
                   "Proficient in Python, Django, Flask, and SQL with hands-on experience in building web applications and APIs. "
                   "Passionate about learning new technologies, solving problems, and delivering clean, scalable solutions.",
        "education": [
            {
                "college": "Sinhgad College of Science, Pune, India",
                "degree": "Bachelor of Business Administration in Computer Application",
                "year": "2021 – 2024",
                "details": [
                    "Among the top 5% of the batch",
                    "Relevant coursework in Database Management, Python Programming, Web Development"
                ]
            },
            {
                "college": "Sitamarhi Inter+2 College, Patna, India",
                "degree": "12th",
                "year": "2020 – 2021",
                "details": [
                    "Among the top 5% of the batch",
                    "Relevant coursework in Physics, Chemistry, Biology"
                ]
            }
        ],
        "achievements": [
            "Academic Achievement: Successfully completed BCA with a CGPA of 7.84 from Savitribai Phule Pune University.",
            "Self-Learning: Learned Django framework independently and built mini projects without formal training.",
            "Online Presence: Maintained a professional GitHub profile with multiple public repositories and an active LinkedIn profile sharing tech content."
        ],
        "languages": ["English", "Hindi"],
        "interests": ["Cricket", "Coding"]
    }
    return render_template("resume.html", resume=resume_data)

# Contact page
@main_bp.route("/contact")
def contact():
    contact_info = {
        "email": "ranjanreignsthakur@gmail.com",
        "phone": "+91 9142145152",
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/ranjanthakur"
    }
    return render_template("contact.html", contact=contact_info)

# 🚀 Task Management System

A Django-based web application for managing tasks efficiently. This system allows users to create, assign, track, and manage tasks with ease.

## ✨ Features

- 📝 Task Creation and Management
- 👥 Task Assignment
- 📅 Due Date Tracking
- 🔄 Status Updates
- 📋 Task Descriptions
- 🔐 User Authentication
- 📱 Responsive Design

## 🛠️ Tech Stack

- **Backend**: Django 5.0.6
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system

## 📸 Screenshots

[Add screenshots of your application here]
- 📊 Dashboard
- ➕ Task Creation Form
- 📋 Task List View
- 🔍 Task Details Page

## ⚙️ Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd TaskManagement
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
- Create a MySQL database named 'taskmanagement'
- Update the database settings in `TaskManagement/settings.py` with your MySQL credentials

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## 📁 Project Structure

```
TaskManagement/
├── myapp/                 # Main application
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   └── urls.py           # URL routing
├── TaskManagement/       # Project configuration
│   ├── settings.py       # Project settings
│   └── urls.py           # Main URL configuration
└── manage.py             # Django management script
```

## 💻 Usage

1. Access the application at `http://localhost:8000`
2. Log in with your credentials
3. Create, assign, and manage tasks
4. Track task progress and due dates

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


## Contact

[Mohammed Zulqarnain] - [zulqarnain4292@gmail.com]

Project Link: [(https://github.com/zulqarnain02/TaskManagement/)](https://github.com/zulqarnain02/TaskManagement/)) 

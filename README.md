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

- 📊 Dashboard
  ![image](https://github.com/user-attachments/assets/aeed8691-f1bf-4ad4-92ae-788f37f355fc)

- ➕ Task Creation Form
  ![image](https://github.com/user-attachments/assets/266e50a0-9638-4fa2-a491-b2c971bfee08)
  
- ✍️ Edit Existing Task
  ![image](https://github.com/user-attachments/assets/ae7b6e9c-bf0a-4792-b064-432f8cc1dce9)

- ✂️ Delete Existing Task
  ![image](https://github.com/user-attachments/assets/abdefd1d-efce-4e51-9dd2-a21e13abf45f)

- 📋 Task List View
  ![image](https://github.com/user-attachments/assets/3c0dfdd6-f27f-48b7-b151-6dfd6420506a)

- 🔍 Task Details Page
  ![image](https://github.com/user-attachments/assets/76c631d8-1d15-492e-bd8d-e7989923d2b3)

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

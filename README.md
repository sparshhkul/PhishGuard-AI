PhishGuard AI 🛡️

An AI-powered phishing detection system that analyzes Emails, URLs, and SMS messages using Machine Learning and Flask.








📖 About

PhishGuard AI is a cybersecurity-based web application that helps users identify phishing attacks before they become victims.

The application provides an intuitive interface where users can scan:

📧 Emails
🌐 URLs
💬 SMS Messages

The Email Scanner uses a Machine Learning model trained on phishing email datasets to classify content as Safe or Phishing.

✨ Features
🛡️ AI-Powered Email Phishing Detection
🌐 URL Scanner Interface
💬 SMS Scanner Interface
⚡ Premium AI Loading Animation
📊 Dynamic Risk Score
🎨 Modern Glassmorphism UI
🚀 Flask Backend
🤖 Machine Learning Integration
📱 Responsive Design
🔍 Real-Time Scan Results
🛠 Tech Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Flask
Machine Learning
Scikit-learn
Pandas
NumPy
Joblib
TF-IDF Vectorizer
Logistic Regression
📂 Project Structure
PhishGuard-AI/

│── app.py

│
├── dataset/
│     ├── phishing_email.csv
│
├── model/
│     ├── train_model.py
│     ├── phishing_model.pkl
│     └── vectorizer.pkl
│
├── utils/
│     └── predictor.py
│
├── static/
│     ├── css/
│     ├── js/
│     └── images/
│
├── templates/
│     ├── index.html
│     ├── scanner.html
│     ├── email.html
│     ├── url.html
│     ├── sms.html
│     └── result.html
│
└── README.md
🚀 Installation

Clone the repository

git clone https://github.com/your-username/PhishGuard-AI.git

Go to the project directory

cd PhishGuard-AI

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open your browser

http://127.0.0.1:5000
🧠 Machine Learning Workflow
Email Input
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Logistic Regression
      │
      ▼
Prediction
      │
      ▼
Risk Analysis
      │
      ▼
Result Page
📷 Screenshots

Add screenshots of:

Home Page
Scanner Page
Email Scanner
Loading Animation
Result Page

Example:

screenshots/
├── home.png
├── scanner.png
├── email.png
├── loading.png
└── result.png
🎯 Future Improvements
🌐 Real AI-based URL Detection
💬 AI-based SMS Detection
📊 Dashboard & Analytics
📜 Scan History
📄 PDF Report Generation
👤 User Authentication
☁️ Cloud Deployment
🔒 Threat Intelligence Integration
📈 Current Progress
Module	Status
Landing Page	✅
Scanner UI	✅
Email AI	✅
URL Scanner	🚧 In Progress
SMS Scanner	🚧 In Progress
Flask Backend	✅
Machine Learning	✅
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch
Commit your changes
Push the branch
Open a Pull Request
👨‍💻 Author: Sparsh kulshrestha

MCA Student | Tech Enthusiast

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub. It helps others discover the project and motivates further development.

📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for learning and educational purposes.
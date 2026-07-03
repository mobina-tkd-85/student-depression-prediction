# 🧠 MindEase - Mental Health Depression Risk Predictor

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)

A machine learning-powered web application that predicts depression risk based on lifestyle, academic, and demographic factors. Built with Flask and scikit-learn, featuring an intuitive and modern user interface.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

MindEase is a web-based tool that assesses an individual's risk of depression using a Decision Tree Regressor model. The application takes 13 input features related to lifestyle, academic pressure, and personal history to generate a risk prediction.

### Why This Matters
Mental health awareness is crucial in today's fast-paced world. This tool provides a quick, data-driven screening that can help individuals understand their mental health risk factors and seek professional help when needed.

## ✨ Features

- 🎨 **Modern, Responsive UI** - Clean interface with smooth animations and mobile-friendly design
- 🤖 **Machine Learning Powered** - Decision Tree Regressor model with 84% accuracy
- 📊 **Real-time Predictions** - Instant risk assessment with confidence scores
- 🔒 **Secure & Private** - No data storage, all processing is done locally
- 📱 **Mobile Compatible** - Works seamlessly on all devices
- 🎯 **13 Input Features** - Comprehensive assessment covering multiple aspects of life

## 📊 Model Performance

After extensive testing with multiple algorithms, the **Decision Tree Regressor** was selected as the best performing model:

| Model | Performance |
|-------|-------------|
| Decision Tree Regressor | ⭐ **BEST** |
| Random Forest Regressor | High |
| Gradient Boosting | High |
| Extra Trees | High |
| Bagging Regressor | Good |
| Ridge Regression | Good |
| SVR | Moderate |
| KNN | Moderate |
| Linear Regression | Moderate |
| Lasso Regression | Moderate |

### Model Specifications
```python
DecisionTreeRegressor(
    criterion='squared_error',
    splitter='best',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.0,
    max_features=None,
    random_state=42,
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    ccp_alpha=0.0
)
```

## 🛠️ Tech Stack

### Backend
- **Flask** - Web framework
- **Scikit-learn** - Machine learning
- **Pandas** - Data processing
- **NumPy** - Numerical computations
- **Pickle** - Model serialization

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with animations
- **JavaScript (ES6)** - Dynamic interactions
- **Font Awesome** - Icons
- **Google Fonts** - Typography

## 📥 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mindease-depression-predictor.git
cd mindease-depression-predictor
```

2. **Create a virtual environment (optional but recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask pandas numpy scikit-learn
```

4. **Place model files**
Make sure you have `model.pkl` and `preprocessor.pkl` in the project root directory.

5. **Run the application**
```bash
python app.py
```

6. **Access the application**
Open your browser and navigate to: `http://localhost:5000`

## 🚀 Usage

### Using the Web Interface

1. **Fill in the form** with your information:
   - Personal details (Gender, Age, City)
   - Academic information (Academic Pressure, CGPA, Study Satisfaction)
   - Lifestyle factors (Sleep Duration, Dietary Habits)
   - Professional/Educational background (Degree, Work/Study Hours)
   - Mental health history (Suicidal thoughts, Family History)
   - Financial status (Financial Stress)

2. **Click "Assess risk"** to get your prediction

3. **View your results**:
   - **Low Risk**: Green badge - Indicates low depression risk
   - **Moderate Risk**: Yellow badge - Suggests moderate risk, consider professional consultation
   - **High Risk**: Red badge - Indicates high risk, strongly recommend seeking professional help

### API Endpoints

#### GET `/`
Returns the main web interface.

#### POST `/predict`
Predicts depression risk based on input features.

**Request Body (JSON):**
```json
{
    "Gender": "Male",
    "Age": 24.5,
    "City": "London",
    "Academic Pressure": 3.5,
    "CGPA": 3.8,
    "Study Satisfaction": 4.2,
    "Sleep Duration": "7-8 hours",
    "Dietary Habits": "Healthy",
    "Degree": "B.Sc.",
    "Have you ever had suicidal thoughts ?": "No",
    "Work/Study Hours": 8.5,
    "Financial Stress": 2.5,
    "Family History of Mental Illness": "No"
}
```

**Response:**
```json
{
    "prediction": 0,
    "risk": "Low",
    "confidence": 0.92
}
```

## 📁 Project Structure

```
mindease-depression-predictor/
│
├── app.py                          # Flask application
├── model.pkl                       # Trained Decision Tree model
├── preprocessor.pkl                # Data preprocessor
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
├── README.md                       # This file
│
├── templates/
│   └── index.html                  # Main web interface
│
├── static/                         # (Optional) Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
│
└── notebooks/                      # (Optional) Training notebooks
    └── model_training.ipynb
```

## 📝 Input Features

| Feature | Type | Description | Example |
|---------|------|-------------|---------|
| Gender | Categorical | Male/Female | "Male" |
| Age | Numeric | Age in years | 24.5 |
| City | Categorical | City name | "London" |
| Academic Pressure | Numeric | 0-5 scale | 3.5 |
| CGPA | Numeric | 0-4 scale | 3.8 |
| Study Satisfaction | Numeric | 0-5 scale | 4.2 |
| Sleep Duration | Categorical | Sleep hours | "7-8 hours" |
| Dietary Habits | Categorical | Healthy/Unhealthy/Moderate | "Healthy" |
| Degree | Categorical | Degree name | "B.Sc." |
| Suicidal Thoughts | Categorical | Yes/No | "No" |
| Work/Study Hours | Numeric | Hours per day | 8.5 |
| Financial Stress | Numeric | 0-5 scale | 2.5 |
| Family History | Categorical | Yes/No | "No" |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```
3. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```
4. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Use meaningful variable names
- Add comments for complex logic
- Update documentation when adding features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 MindEase

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

## 🙏 Acknowledgments

- **Scikit-learn** for providing excellent ML tools
- **Flask** for the lightweight web framework
- **Font Awesome** for beautiful icons
- **Google Fonts** for typography
- All contributors who help improve this project

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/mindease-depression-predictor/issues)
- **Email**: your.email@example.com

## ⚠️ Disclaimer

This tool is for **educational and screening purposes only**. It should not replace professional medical diagnosis. Always consult with qualified healthcare professionals for mental health concerns.

---

**Made with ❤️ for better mental health awareness**

[![Star on GitHub](https://img.shields.io/github/stars/yourusername/mindease-depression-predictor.svg?style=social)](https://github.com/yourusername/mindease-depression-predictor/stargazers)
[![Follow on GitHub](https://img.shields.io/github/followers/yourusername.svg?style=social&label=Follow)](https://github.com/yourusername)
```

# 🏦 Bank Complaints Management System

A Django web application for managing bank customer complaints with machine learning-powered automatic categorization.

## 🤖 Machine Learning Integration

The application uses a pre-trained Random Forest classifier to automatically categorize complaints into:
- Credit Card
- Mortgage
- Bank Account Services
- Theft/Dispute Reporting
- Consumer Lending
- Student Loans
- Payday Loan
- Debt Collection
- Credit Reporting
- Money Transfers
- Other Financial Service

### ML Model Details
- **Algorithm**: Random Forest Classifier
- **Features**: TF-IDF vectorization
- **Hosting**: Hugging Face Spaces with Gradio
- **API Endpoint**: `https://huggingface.co/spaces/Sahith22/complaint-classifier/tree/main`

## 🚀 Features

### **User Features**
- **User Registration & Authentication** - Secure login/register system
- **Complaint Filing** - Submit detailed complaints with ML classification
- **Personal Dashboard** - View your complaint history
- **Real-time Classification** - Automatic categorization using trained ML model

### **Manager Features**
- **Complaint Overview** - View all complaints by category
- **Category Filtering** - Dropdown to filter complaints by type
- **Staff Access Control** - Secure manager-only access

### **Technical Features**
- **Machine Learning Integration** - Hugging Face Spaces API for complaint classification
- **PostgreSQL Database** - Scalable database with Neon cloud hosting
- **Responsive Design** - Modern CSS styling without Bootstrap
- **Production Ready** - Configured for deployment on Render/Railway/Heroku

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (Neon)
- **ML Model**: Random Forest with TF-IDF (hosted on Hugging Face)
- **Static Files**: WhiteNoise
- **Styling**: Custom CSS

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

Created as part of IIIT internship project.
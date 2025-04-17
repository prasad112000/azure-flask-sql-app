
# 🚀 Azure Flask SQL Web App – Secure, Scalable & Integrated

This project is a complete demonstration of how to deploy a secure, highly available, and fault-tolerant **Flask web application** connected to an **Azure SQL Database**, with integration to external services and designed to handle **1000+ requests per second**.

---

## 📌 Project Goal

> **Assignment:** Architect the infrastructure, deployment, and release plan for a web service with the following:
- ✅ SQL Database
- ✅ External Service Integration
- ✅ RPS Target of 1000/s
- ✅ High Availability & Fault Tolerance
- ✅ Secure Design
- ✅ Deployed on Microsoft Azure

---

## 🧠 Architecture Overview

![Architecture](https://drive.google.com/uc?export=view&id=1w6jSr5liS-kmjVr-vvZpkeVG-2k02gAZ)

### Key Components:
- **Flask App:** Python-based lightweight web framework
- **Azure SQL Database:** Managed relational database service
- **External Service:** Placeholder (can be payment API, logging, etc.)
- **Azure App Service:** For deployment of Flask application
- **Azure Resource Group:** Logical container for all resources
- **VS Code + Azure Extension:** For easy deployment

---

## 🔧 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python + Flask | Web framework |
| Azure SQL | Cloud SQL Database |
| SQLAlchemy | ORM for DB connection |
| Azure App Service | Hosting & Deployment |
| Gunicorn | Production WSGI Server |
| Git & GitHub | Version control |
| VS Code | Development Environment |

---

## 🛠 Setup & Run Locally

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/prasad112000/azure-flask-sql-app.git
cd azure-flask-sql-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask App
```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ☁️ Deploy to Azure App Service

> Easiest Way: Using **VS Code Azure App Service Extension**

### Steps:
1. Open project in VS Code
2. Install “Azure App Service” extension
3. Sign into Azure in VS Code
4. Click **App Service** → Right-click → **Create New Web App**
5. Select:
   - Resource Group
   - Runtime: Python 3.11
   - Region (ex: Central India)
6. App will be zipped and deployed live

✅ You’ll see your app URL like: `https://flask-on-azure.azurewebsites.net`

---

## 🧪 Testing & Performance

- **RPS Testing:** Azure App Service auto-scales with load balancer
- **Fault Tolerance:** Azure SQL is geo-replicated with backups
- **Security:** SQL credentials stored in environment variables

---

## 📎 Screenshots

Screenshots of setup, code, deployment and final working app available in the [Google Drive Folder](https://drive.google.com/drive/folders/1bMDtHiTZd8FmD7wDzwtE-wFaWt3kCl4Q?usp=sharing)

---

## 👨‍💻 Author

**Prasad Vinod Pardeshi**

- 📧 Email: pardeshiprasad42@gmail.com  
- 📱 Phone: +91 7083563821  
- 🔗 LinkedIn: [@prasad-pardeshi11](https://www.linkedin.com/in/prasad-pardeshi11/)  
- 💻 GitHub: [@prasad112000](https://github.com/prasad112000)

---

## 📌 Conclusion

This project reflects real-world cloud infrastructure and web app deployment best practices using Microsoft Azure. It emphasizes secure, scalable, and production-ready design — making it ideal for modern cloud engineers and DevOps roles.

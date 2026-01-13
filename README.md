# 🎓 Student UI – Full Stack DevOps Project

A production-style **frontend–backend microservices application** built with **Flask**, **Docker**, **GitHub Actions CI/CD**, and **Terraform**, deployed on **AWS EC2**.

This project demonstrates **real DevOps workflows** used in industry:
- CI builds Docker images
- CD deploys containers to EC2
- Infrastructure provisioned using Terraform
- Secure configuration using environment variables

---

## 🏗️ Architecture Diagram

![Architecture Diagram](/Architecture-Diagram/architecture.png)

---

## 🧠 Key Concepts Demonstrated

- Microservices architecture
- Docker containerization
- Docker networking
- CI/CD using GitHub Actions
- Infrastructure as Code (Terraform)
- Environment-based configuration (12-factor app)

---

## 📁 Project Structure

```bash
student-ui/
├── frontend/
│ ├── app.py
│ ├── templates/
│ ├── Dockerfile
│ └── requirements.txt
│
├── backend/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── terraform/
│ ├── provider.tf
│ ├── main.tf
│ └── outputs.tf
│
├── .github/
│ └── workflows/
│ ├── ci.yml
│ └── cd.yml
│
└── README.md
```

---

## 🔧 Services Overview

### Frontend Service
- Flask-based UI
- Student registration form
- Admin login & dashboard
- Communicates with backend via `BACKEND_URL`

**Port:** 5000

---

### Backend Service
- Flask REST API
- Endpoints:
  - `/health`
  - `/students` (GET, POST)
- Gracefully handles database unavailability

**Port:** 5001

---

## 🐳 Docker Images

| Service | Image | 
|------|------|
| Backend | ```dockerhub-username/student-ui-backend:latest``` |
|          |                                                    |
| Frontend | ```dockerhub-username/student-ui-frontend:latest``` |

---

## 🐳 Docker Commands Used

### Create Docker Network
```bash
docker network create student-ui-net
docker run -d \
  --name student-ui-backend \
  --network student-ui-net \
  -p 5001:5001 \
  dockerhub-username/student-ui-backend:latest
```

### Run Backend
```bash
docker run -d \
  --name student-ui-backend \
  --network student-ui-net \
  -p 5001:5001 \
  dockerhub-username/student-ui-backend:latest
```

### Run Frontend
```bash
docker run -d \
  --name student-ui-frontend \
  --network student-ui-net \
  -p 5000:5000 \
  -e BACKEND_URL=http://student-ui-backend:5001 \
  dockerhub-username/student-ui-frontend:latest
```

---

## 🚀 CI/CD Pipeline

### CI (Continuous Integration)

- Performs:
   - Python import checks
   - Docker image build
   - Push images to Docker Hub
   
### CD (Continuous Deployment)

- Performs:
    - SSH into EC2
    - Docker installation verification
    - Docker network creation
    - Image pull
    - Container deployment

---

## 🏗️ Terraform Commands Used
```bash
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

---

## 🌍 Application Access

- Frontend -> ```http://EC2_PUBLIC_IP:5000```
- Backend Health -> ```http://EC2_PUBLIC_IP:5001/health```

---

## 🔐 Security Practices

- No secrets in code
- SSH keys ignored via ```.gitignore```
- Secrets stored in GitHub Actions
- Environment variables for configuration

---

## 📌 Summary

✔ Microservices architecture
✔ CI/CD automation
✔ Docker networking
✔ Terraform-based infrastructure
✔ Production-style configuration

---

## 👤 Author

Nikhil Acholiya
DevOps / Cloud Engineer

---  

## ⭐ Notes

This project is resume-ready and interview-ready.

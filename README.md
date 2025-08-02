# Flask Redis Microservice App 🐍🔁🧱

This is a real-world DevOps project that implements a **containerized microservice architecture** using **Flask**, **Redis**, and **Docker Compose**. The goal is to simulate modern app infrastructure with in-memory caching using Redis, service modularity, and container orchestration.

---

## 📦 Tech Stack

- **Python (Flask)** – API service
- **Redis** – In-memory data store
- **Docker** – Containerization
- **Docker Compose** – Service orchestration

---

## 📁 Project Structure
flask-redis-app/
│
├── app.py # Main Flask API logic
├── Dockerfile # Docker image for Flask app
├── requirements.txt # Python dependencies
├── docker-compose.yml # Multi-container definition


---

## 🚀 Features

- Simple **Flask REST API** with endpoints for:
  - User registration
  - User retrieval
- **Redis-backed caching** to improve performance
- Clean separation of services (Flask & Redis)
- Local deployment using **Docker Compose**
- Easy to extend into a Kubernetes setup

---

## ⚙️ How to Run (Locally)

> Requires Docker and Docker Compose

```bash
# 1. Clone the repo
git clone https://github.com/Manasi6901/flask-redis-app.git
cd flask-redis-app

# 2. Start the application
docker-compose up --build

# 3. Access API
curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"name":"manasi","email":"manasi@test.com"}'
curl http://localhost:5000/users

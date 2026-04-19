

# ♻️ Smart Recycling Waste System (SRWS) - Backend

This repository contains the backend infrastructure for the Smart Recycling Waste System (SRWS). The system is built using a Microservice Architecture to ensure high performance, scalability, and a clean separation between AI processing and data management.


 ## Architecture Overview
The backend is composed of three independent services containerized via Docker, communicating to provide a seamless waste management experience:

.NET Core API (Core Business Logic): Handles user data, scan history orchestration, and database management using Entity Framework Core.

FastAPI AI Service (Computer Vision): A high-performance Python service dedicated to image processing and waste classification.

PostgreSQL (Persistence Layer): Relational database storing waste categories, metadata (HEX colors, icons), and historical scan logs.

## Tech Stack
Orchestration: Docker & Docker Compose

Primary API: .NET 8 / C#

AI Service: Python 3.11 / FastAPI

Database: PostgreSQL 15

ORM: Entity Framework Core

## Key Features
Microservice Isolation: Decoupled services ensure that even if the AI service is under heavy load, the core API remains responsive.

AI-Powered Classification: Identifies 5 main categories: Plastic, Paper & Cardboard, Metal, Battery, and Glass.

Enriched Metadata: Returns the category, Recycling Bin Color, HEX codes for UI consistency, and Confidence Scores.

Automatic Database Seeding: The .NET service automatically creates tables and populates the database with initial categories on the first run.

## 📂 Project Structure
Plaintext
backend_srws/
├── dotnet_api/          # C# .NET Core Service (Web API)
├── fastapi_ai/          # Python FastAPI Service (AI/ML)
├── database/            # SQL Initialization scripts
└── docker-compose.yml   # Main orchestration file
# Getting Started
Prerequisites
Docker Desktop installed.
Git installed.

# Installation & Deployment
## Clone the repository:

git clone https://github.com/melisozdgn/Smart-Recycling-Waste-System--backend.git
cd Smart-Recycling-Waste-System--backend

## Run with Docker Compose:

Bash
docker-compose up --build
Access the Services:

### .NET API (Swagger UI): http://localhost:5000/swagger

### AI Service (FastAPI Docs): http://localhost:8000/docs

# API Endpoints
## 1. AI Classification (fastapi_ai)
### POST /api/ai/classify

### Input: multipart/form-data (image file).

### Output: Returns category, confidence, description, and color_hex.

## 2. History & Metadata (dotnet_api)
### GET /api/categories: Retrieves the list of recycling categories.

### POST /api/scan/history: Saves a new scan record.

### GET /api/scan/history: Retrieves all previous scan logs.Anladım, kopyaladığında satırların birbirine girmemesi ve GitHub'da tam istediğin gibi (başlıklar büyük, maddeler düzenli) görünmesi için Markdown (MD) formatında, aralarda boşluklar bırakarak hazırladım.



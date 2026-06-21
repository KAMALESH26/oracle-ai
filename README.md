# ORACLE AI

AI-Powered Trend Intelligence Platform

---

## Overview

ORACLE AI is a full-stack Artificial Intelligence platform designed to collect, analyze, forecast, and explain emerging technology and industry trends from multiple public data sources.

The platform continuously gathers information from:

- RSS Feeds
- GitHub Trending
- Hacker News
- Reddit
- Technology News Sources

ORACLE AI processes incoming data using Natural Language Processing (NLP), trend analysis algorithms, forecasting models, and Generative AI to identify emerging topics and generate actionable intelligence.

---

## Key Features

### Trend Collection

- Multi-source data aggregation
- RSS feed ingestion
- GitHub trend monitoring
- Hacker News monitoring
- Reddit monitoring

### Trend Intelligence

- Keyword extraction
- Topic clustering
- Topic categorization
- Emerging trend detection
- Trend scoring

### Forecasting

- Topic forecasting
- Historical trend analysis
- Momentum analysis
- Growth prediction

### Artificial Intelligence

- Gemini-powered insights
- Automated report generation
- Trend explanation engine
- Conversational AI interface

### Dashboard

- Real-time analytics
- Trend visualizations
- Forecast dashboards
- AI-generated intelligence reports

---

## Architecture

```
Data Sources
│
├── RSS Feeds
├── GitHub Trending
├── Hacker News
└── Reddit
│
▼

Collection Layer
│
▼

NLP Processing
│
├── Keyword Extraction
├── Topic Detection
├── Topic Clustering
└── Trend Scoring
│
▼

Intelligence Layer
│
├── Emerging Topics
├── Forecasting
├── Confidence Analysis
└── AI Reports
│
▼

React Dashboard
```

---

## Tech Stack

### Frontend

- React
- Vite
- Recharts
- JavaScript
- CSS

### Backend

- Flask
- Python

### Databases

- PostgreSQL
- MongoDB
- Redis

### Artificial Intelligence

- Google Gemini API
- NLP
- Machine Learning

### Infrastructure

- Docker
- Docker Compose

---

## Project Structure

```text
ORACLE-AI/

backend/
frontend/
infrastructure/

README.md
.gitignore
```

---

## Screenshots

### Dashboard

Add:

```
docs/screenshots/dashboard.png
```

### Forecasting

Add:

```
docs/screenshots/forecasts.png
```

### AI Insights

Add:

```
docs/screenshots/insights.png
```

### Oracle Chat

Add:

```
docs/screenshots/oracle-chat.png
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/KAMALESH26/oracle-ai.git

cd oracle-ai
```

### Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Frontend

```bash
cd frontend

npm install
```

### Environment Variables

Create:

```env
backend/.env
```

Example:

```env
POSTGRES_USER=oracle

POSTGRES_PASSWORD=password

POSTGRES_DB=oracle_analytics

MONGO_URI=mongodb://localhost:27017

GEMINI_API_KEY=YOUR_KEY
```

---

## Run PostgreSQL & MongoDB

```bash
docker compose up -d
```

---

## Run Backend

```bash
cd backend

source venv/bin/activate

python -m app.main
```

Backend:

```
http://localhost:5000
```

---

## Run Frontend

```bash
cd frontend

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

## API Endpoints

### Health

```
GET /health
```

### Trends

```
GET /api/trends
```

### Momentum

```
GET /api/momentum
```

### Forecasts

```
GET /api/topic-forecast
```

### Emerging Topics

```
GET /api/emerging-topics
```

### AI Insights

```
GET /api/insights
```

### Oracle Chat

```
POST /api/chat
```

---

## Future Enhancements

- Real-time streaming analytics
- Advanced forecasting models
- Sentiment intelligence
- Trend correlation engine
- Enterprise reporting
- Multi-agent AI system (Vegapunk AI)

---

## Author

Kamalesh R

B.Sc Information Technology

Sri Ramakrishna College of Arts & Science

GitHub:
https://github.com/KAMALESH26

Portfolio:
https://kamalesh26.github.io
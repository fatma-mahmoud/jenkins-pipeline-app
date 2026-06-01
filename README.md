# Jenkins Pipeline App

A Python Flask application with a full CI/CD pipeline using Jenkins.

## Project Structure

```
jenkins-pipeline-app/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container definition
├── Jenkinsfile         # CI/CD pipeline
├── templates/
│   └── index.html      # App UI
└── tests/
    └── test_app.py     # Pytest tests
```

## Pipeline Stages

| Stage | Description |
|-------|-------------|
| **Build** | Install Python dependencies |
| **Test** | Run pytest test suite |
| **Docker Build** | Build & tag container image |
| **Deploy** | Stop old container, run new one |
| **Health Check** | Verify app is up via `/health` |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
```

## Run with Docker

```bash
docker build -t jenkins-pipeline-app .
docker run -p 5000:5000 jenkins-pipeline-app
```

## Jenkins Setup

1. Install Jenkins and the **Pipeline** + **Docker** plugins
2. Create a **New Item → Pipeline** job
3. Under *Pipeline*, set **Definition** to `Pipeline script from SCM`
4. Point it to this Git repo — Jenkins will use the `Jenkinsfile` automatically
5. Click **Build Now**

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard UI |
| GET | `/health` | Health check |
| GET | `/api/info` | App metadata |

# Azure Operations Platform

A learning project for practising cloud operations, Docker, Azure, Terraform, CI/CD,

monitoring \& troubleshooting.





### Current Functionality

* A root endpoint
* A health-check endpoint
* List of simulated company service statuses
* Automated API tests
* A Dockerfile for running the app in a container



### 

### Technology used

* Python
* FastAPI
* Uvicorn
* Pytest
* Docker
* Git \& GitHub





### Run Locally with Python



Create a python virtual environment



python - m venv .venv



Activate the virtual environment



.venv\\Scripts\\Activate.ps1



Install dependencies



python -m pip install -r requirements.txt



Start application



python -m uvicorn app.main:app --reload



Open API documentation



http://127.0.0.1:8000/docs





#### Available endpoints



/

/health

/services

/version

/docs



#### Run Tests



Run automated tests from project root



python -m pytest



These tests verify that root,health-check and service-status endpoints give the expected responses.



#### Run with docker



Build Docker image



docker build -t azure-operations-platform:0.1.0 .



Run application container



docker run --name azure-operations-platform -p 8000:8000 azure-operations-platform:0.1.0



Open API documentation



https://localhost:8000/docs



Test the container from another terminal



curl http://localhost:8000/

curl http://localhost:8000/health

curl http://localhost:8000/services



View container logs



docker logs azure-operations-platform



Stop and remove container



docker stop azure-operations-platfrom

docker rm azure-operations-platform


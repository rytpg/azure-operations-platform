\# Runbook: Docker Container Operations



\## Purpose



This runbook documents the basic commands for running, inspecting and troubleshooting the Azure-Operations-Platform container.



\## Starting the container



docker -run -d --name azure-operations-platform -p 8000:8000 azure-operations-platform:0.1.0



\## Check whether the container is running



docker ps

docker ps -a



\## Testing the application



curl.exe http://localhost:8000/

curl.exe http://localhost:8000/health

curl.exe http://localhost:8000/services



\# Viewing logs



docker logs azure-operations-platform



\# Entering the container shell



docker exec -it azure-operations-platform sh



\# Stopping/removing the container



docker stop azure-operations-platform

docker rm azure-operations-platform




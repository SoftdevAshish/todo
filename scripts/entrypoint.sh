#!/bin/bash

  set -e

  CONTAINER_IP=$(hostname -i)
  echo "Starting Todo API..."
  echo "Working Directory is : ${pwd}"
  echo f"API URL: http://${CONTAINER_IP}:8000/api/v1/"
  echo "Swagger UI: http://${CONTAINER_IP}:8000/api/v1/docs"

  exec uvicorn app.main:app \
       --host "${CONTAINER_IP}" \
       --port 8000 --reload
# notification-system
This is a notification system made using FastAPI
1. install the requirements:
  pip install fastapi uvicorn websockets pika
2. create the docker-compose-yaml file
3. docker-compose up (to run rabbitmq in a docker container)
4. uvicorn src.app.main:app --reload --port=8900 (for running the FastAPI server)

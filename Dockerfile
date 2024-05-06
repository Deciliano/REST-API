FROM python:3.9-slim-buster

WORKDIR /app

# Install all necessary tools
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/list/*

# Creation of the virtual environment
RUN python3 -m venv venv

# Copy the application directory and install the packages later
COPY app /app
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"


COPY . .

EXPOSE 5000

ENV FLASK_APP=main.py
CMD [ "venv/bin/python", "-m", "flask", "run", "--host", "0.0.0.0"]
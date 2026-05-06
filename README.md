# Iris Classification Flask App

A simple machine learning web application built with **Flask** that predicts the species of an Iris flower using the classic **Iris dataset**. The project is containerized with **Docker** and uses **GitHub Actions** for CI/CD automation.

---

## Overview

This project demonstrates an end-to-end ML deployment workflow:

- Train a model using the Iris dataset
- Serve predictions using a Flask web app
- Containerize the application with Docker
- Automate build and testing with GitHub Actions

The model predicts one of three Iris species:
- Setosa
- Versicolor
- Virginica

---

## Tech Stack

- Python 
- Flask 
- Scikit-learn 
- Pandas / NumPy 
- Docker 
- GitHub Actions 

---

## Project Structure

.
├── app.py                  # Flask application
├── model.py                # Model training script
├── iris_model.pkl          # Trained ML model
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker configuration
├── .github/workflows/      # GitHub Actions pipeline
└── README.md

---

## Dataset

The project uses the built-in **Iris dataset** from Scikit-learn:

- Sepal length
- Sepal width
- Petal length
- Petal width

Target:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

## Run the Project with Docker

Step 1: Build the Docker image
docker build -t iris-flask-app .

Step 2: Run the Docker container
docker run -p 5000:5000 iris-flask-app

Step 3: Open the application in browser
http://localhost:5000

## GitHub Actions CI/CD

The project includes an automated pipeline using GitHub Actions.

On every push to the main branch, the workflow:
- Checks out the code
- Sets up Python environment
- Installs dependencies
- Trains the model
- Builds the Docker image

# Todo App

This project is a basic Todo application built with **FastAPI**.
## Project Structure
```text
todo/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │
│   ├── core/
│   │
│   └── features/
│       ├── auth/
│       │
│       ├── todos/
│       │   
│       │
│       └── users/
│
├── migrations/
│   └── versions/
│
├── tests/
│   ├── auth/
│   ├── todos/
│   └── users/
│
├── docker/
│
└── scripts/
```
The main purpose of this project is to practice setting up a FastAPI application, configuring environment variables, installing required packages, and connecting PostgreSQL with Docker.

## Features

- FastAPI project setup
- Environment variable configuration
- PostgreSQL database
- PostgreSQL running with Docker
- Health check endpoint
- Create Todo
- Read Todo
- Update Todo
- Delete Todo

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- Docker
- SQLAlchemy
- Pydantic

## Project Goal

The goal of this project is to build a simple CRUD API while learning how to structure and configure a FastAPI backend application with PostgreSQL and Docker.
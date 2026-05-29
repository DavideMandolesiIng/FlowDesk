# FlowDesk

A full-stack desktop productivity app built as a learning project. It covers Python, TypeScript, REST APIs, relational databases, authentication, containerization, and CI/CD within a single codebase.

---

## What is FlowDesk?

FlowDesk is a personal productivity desktop application that combines three main tools:

- **Task board**: a kanban-style board with customizable columns, priorities, and deadlines.
- **Structured notes**: a markdown editor with tagging and full-text search.
- **Habit tracker**: a tool for daily habit logging that calculates streaks and shows a heatmap calendar.

All data is stored in a PostgreSQL database. This is accessed through a FastAPI REST backend and shown through a React/TypeScript frontend. The whole application is packaged as a native desktop app using Electron.

---

## Educational Purpose

This project serves as the main learning tool of a structured self-study plan focused on full-stack development with Python and JavaScript/TypeScript. Each development phase connects directly to a study topic, allowing for the immediate application of new concepts to a real, evolving codebase.

| Phase | Study Topic | What gets built |
|-------|-------------|-----------------|
| 1 | Python fundamentals, transition from Java | Domain model classes, business logic, JSON mock persistence, pytest |
| 2 | Software architecture, APIs, databases, system design | FastAPI REST endpoints, PostgreSQL schema, SQLAlchemy ORM, Alembic migrations |
| 3 | JavaScript/TypeScript and full-stack architecture | React/TypeScript frontend, Electron desktop packaging, API client, analytics dashboard |
| 4 | Version control (advanced) and privacy & security | JWT authentication, bcrypt password hashing, OWASP hardening, structured Git workflow |
| 5 | Microservices and containerization | Dockerfile, Docker Compose dev environment, GitHub Actions CI/CD, Fly.io deployment |

The project is designed to be built step by step. Each phase leaves the codebase in a functional state, ensuring that progress is always clear and testable.

---

## Tech Stack

**Backend**
- Python 3.11+
- FastAPI: REST API framework
- SQLAlchemy: ORM
- Alembic: database migrations
- PostgreSQL: relational database
- pytest: testing
- ruff: linting

**Frontend**
- TypeScript
- React
- Electron and electron-vite: desktop packaging
- React Query: server state management
- Recharts: analytics charts

**Infrastructure**
- Docker and Docker Compose
- GitHub Actions: CI/CD pipeline
- Fly.io: cloud deployment


## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20 and above (phase 3+)
- Docker (phase 5+)

### Run tests

```bash
cd backend
pytest
```

### Lint

```bash
ruff check .
```

---

## Development Roadmap

- [x] Phase 1: Python domain models and mock persistence
- [ ] Phase 2: FastAPI REST API and PostgreSQL integration
- [ ] Phase 3: React/TypeScript frontend and Electron desktop app
- [ ] Phase 4: JWT authentication and security hardening
- [ ] Phase 5: Docker, CI/CD pipeline, and production deployment

---

## Key Design Decisions

**Repository pattern**: data access is separated from domain logic from the start. The JSON mock repository in phase 1 is replaced with a PostgreSQL repository in phase 2 without affecting the domain model classes.

**Separation of domain models and API schemas**: `models/` holds pure Python dataclasses that do not rely on frameworks. `schemas/` (added in phase 2) contains Pydantic models for HTTP validation. This separation helps prevent coupling of domain logic to the transport layer.

**Habit streaks are computed, not stored**: streak counts come from the `habit_logs` table when queried instead of being kept as a variable field. This approach avoids inconsistencies and is a key architectural choice that influences the design of the `habit_logs` table in phase 2.

---

## License

This project is for educational purposes.
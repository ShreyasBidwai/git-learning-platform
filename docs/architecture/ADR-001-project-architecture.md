# ADR-001: Project Architecture

## Status

Accepted

## Context

The Git Learning Platform is an interactive educational application for teaching Git concepts through guided lessons and a visual playground.

The initial technology stack is:

React + TypeScript for the frontend
FastAPI + Python for the backend
PostgreSQL for persistent storage

The application is expected to expand later with additional learning domains such as Docker.

The project is intentionally being designed with a small initial scope while maintaining strong software engineering practices, security boundaries, testability, and long term maintainability.

## Decision

The application will use a layered architecture with the following high level dependency flow:

Frontend
→ API
→ Application Services
→ Domain
→ Infrastructure

The core Git simulation/domain logic must remain independent of FastAPI, PostgreSQL, React, and other infrastructure concerns.

The Git simulation engine will model Git as a deterministic state transition system.

Conceptually:

State + Command → New State + Events

The frontend visualization will consume the resulting state and events rather than containing Git business logic itself.

The initial implementation will support a deliberately limited Git command set. Additional commands will be introduced only after the underlying domain model and existing behavior are stable.

## Consequences

This architecture makes the Git engine independently testable.

The frontend can change without changing the core Git logic.

The persistence mechanism can evolve without coupling database concerns to the Git domain.

Future learning domains, such as Docker, can reuse the broader learning and exercise architecture while maintaining their own domain engines.

The initial implementation requires slightly more architectural discipline than placing all logic directly inside API routes or React components, but provides a stronger foundation for future expansion.

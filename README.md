# User Registration API with Unique Email Constraint

## Task Overview

You are tasked with developing a user registration backend for a fast-growing SaaS platform. The business requires that each user registers with a unique email address, as duplicate registrations have caused confusion and support issues. The current system does not prevent duplicate emails, resulting in multiple accounts per email and potential security risks. Your job is to design a robust API that enforces email uniqueness at both the API and database levels, ensuring a reliable user onboarding process.

## Guidance

This project represents a simplified but realistic user management microservice. Focus on separating API validation from database schema enforcement: both should independently prevent duplicate email entries. Use async SQLAlchemy for database operations and Pydantic models for input/output validation. Proper error handling is critical; the API must return clear, actionable error messages when a duplicate registration is attempted. Containerize your solution for reliable local development using Docker Compose, and ensure all configuration is managed via environment variables. Structure your code for maintainability, with routers, services, and configuration organized into appropriate modules.

## Objectives

- Implement a user registration endpoint that accepts email, full name, and password, and creates a new user only if the email does not already exist.
- Ensure the email field is unique using both API-level checks and a database-level unique constraint.
- Provide a user listing endpoint that returns all registered users (excluding passwords) in a structured format.
- Handle duplicate registration attempts gracefully, returning an appropriate HTTP status and error message.
- Use async/await patterns for all database operations, and leverage Pydantic for request/response validation.
- Containerize the application and database with Docker and Docker Compose, using environment variables for configuration.

## How to Verify

After implementing the solution, verify that registering a new user with a unique email succeeds and returns the correct response. Attempting to register another user with the same email should result in a clear error message and a 400 or 409 status code, without creating a duplicate in the database. Listing users should return all registered users, with no duplicate emails present. The API should be fully functional when both the backend and PostgreSQL are running via Docker Compose, and all environment variables should be respected. Inspect the database schema to confirm the unique constraint on the email column.

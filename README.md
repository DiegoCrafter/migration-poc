migration-poc
===========================================

Globant Challenge.

This project is a FastAPI-based RESTful service that connects to Google Cloud SQL (PostgreSQL), processes large datasets using Polars, and supports batch data insertion. It also includes backup and restore functionality using the Avro format.

Key Use Cases:
Migrating historic data from CSV files into a PostgreSQL database.
Inserting batch transactions (up to 1,000 rows) via a REST API.
Backing up and restoring data in Avro format for reliability and performance.

Tech Stack
FastAPI – For building the REST API.
PostgreSQL (Cloud SQL) – Database management.
Polars – High-performance DataFrame library for handling and validating large datasets.
Avro – For efficient data serialization (backup and restore).
Docker – For containerization.
Google Cloud Platform (GCP) – Hosting and deployment.

Visualization
Available on Looker Studio
https://lookerstudio.google.com/reporting/4f768aa7-b5e0-4171-be2c-5463881193c9


class Constants:
    DB_USER = "postgres"
    DB_PASSWORD = "root"
    DB_NAME = "globant_dec_db"
    INSTANCE_CONNECTION_NAME = "globant-challenge-68198:us-central1:de-challenge-globant-instance"
    TABLES_INSTANCES = {"jobs": ["id", "job"], "departments": ["id", "department"],
                        "hired_employees": ["id", "name", "datetime", "department_id", "job_id"]}

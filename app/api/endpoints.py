from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy import create_engine, MetaData
from app.constants import Constants
from sqlalchemy.exc import SQLAlchemyError
from app.utils.utils import Utils

app = APIRouter()
metadata = MetaData()
utils = Utils()


engine = create_engine(
    "postgresql+pg8000://",
    creator=utils.get_connection,
)

metadata.reflect(bind=engine)


@app.post("/upload-file/")
async def upload_historic_files(table_name: str, file: UploadFile = File(...)):
    if table_name not in metadata.tables:
        raise HTTPException(status_code=400, detail=f"Table '{table_name}' does not exist.")
    column_names = utils.get_value_as_list(Constants.TABLES_INSTANCES, table_name)
    try:
        file_content = await file.read()
        res = utils.insert_csv_to_db(file=file_content,
                                     table_name=table_name,
                                     column_names=column_names,
                                     engine=engine
                                     )
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    if res != 0:
        return {"Error table."}
    return {"message": f"Successfully inserted rows into '{table_name}' table."}

import sqlite3 as sql
from middleware.errorhandlers import SQLError


def push_to_db(dataframe, table_name):
    """
    Method to push dataframe to dataframe to a specific table
    :param dataframe: dataframe
    :param table_name: table name
    """
    try:
        db_engine = sql.connect("db.sqlite")
        dataframe.to_sql(
            table_name,
            con=db_engine,
            if_exists="replace",
            index=True,
        )
    except Exception as err:
        raise SQLError(err)
    else:
        print(f"Table with name {table_name.title()} is migrated successfully")

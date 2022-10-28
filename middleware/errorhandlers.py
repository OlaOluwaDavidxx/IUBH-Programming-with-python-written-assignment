"""Error handlers."""


class EmptyDataError(Exception):
    """
    Handles empty csv files
    """
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f" status: error \nerror: {__class__.__name__} \nmessage: dataset is empty. " \
               f"Please check your file resource."


class EmptyColumnX(Exception):
    """
    Dataframe does not have X features
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__} \nmessage: dataset does not contain x features. " \
               f"Please check your file resource."


class EmptyColumnY(Exception):
    """
    Dataframe does not have Y features
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__}  \nmessage: dataset does not contain y features. " \
               f"Please check your file resource."


class DataTypeError(Exception):
    """
    Handle errors related to dataset type is not numerical
    """
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__}  \nmessage: contains invalid value type."


class NoDataBaseError(Exception):
    """
    Handles no database error
    """
    def __init__(self, database):
        self.database = database

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__}  \nmessage: Database does not exist."


class WrongDataNameError(Exception):
    """
    Handles no database error
    """
    def __init__(self, database_name):
        self.database_name = database_name

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__}  \nmessage: Database name is invalid. " \
               f"Only lowercase letters."


class FileError(Exception):
    """
    Handles file not found error
    """
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f"status: error \nerror: {__class__.__name__}  \nmessage: File not found"


class SQLError(Exception):
    pass

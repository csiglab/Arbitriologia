class Dataset:

    def __init__(self, name=None, schema=None, records=None, metadata = None):
        """
        Initialize the Dataset class.

        Args:
            name (str, optional): Name of the dataset.
            schema (dict, optional): Schema of the dataset as a dictionary (e.g., column names and types).
            data (pd.DataFrame, optional): A pandas DataFrame containing the data.
        """
        self.records = records
        self.name = name
        self.schema = schema
        self.metadata =  metadata

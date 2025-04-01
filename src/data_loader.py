import pandas as pd

def load_data(filepath='data/iris.csv'):
    """Load the Iris dataset from a CSV file."""
    data = pd.read_csv(filepath)
    return data
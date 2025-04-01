def clean_data(df):
    """Cleans the input DataFrame by handling missing values and duplicates."""
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    return df

def encode_species(df):
    """Encodes the species column as numeric values."""
    df['species'] = df['species'].astype('category').cat.codes
    return df

def normalize_data(df):
    """Normalizes the numeric columns of the DataFrame."""
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df
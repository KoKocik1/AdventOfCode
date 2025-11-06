import pandas as pd


def get_csv_data(path, names=None, add_index=True):
    """
    Read CSV file with whitespace delimiter and return DataFrame.

    Args:
        path: Path to the CSV file
        names: Optional list of column names
        add_index: If True, add index as a column (default: True)

    Returns:
        pd.DataFrame: DataFrame with the data
    """
    df = pd.read_csv(
        path,
        delim_whitespace=True,
        names=names
    )

    if add_index:
        df['index'] = df.index

    return df

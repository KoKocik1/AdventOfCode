# load csv file
import matplotlib.pyplot as plt
import pandas as pd


def get_data(path, names=None) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        delim_whitespace=True,
        names=names)
    # add index as a column
    df['index'] = df.index

    return df

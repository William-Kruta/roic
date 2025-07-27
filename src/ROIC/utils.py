import numpy as np
import pandas as pd


def clean_dataframe(df: pd.DataFrame):
    df = df.replace({"- -": np.nan})
    df = df.replace({",": ""}, regex=True)
    return df

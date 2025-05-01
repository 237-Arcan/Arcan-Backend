import dask.dataframe as dd

def load_distributed_data(path):
    df = dd.read_csv(path)
    return df.compute()

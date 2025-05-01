# app/meta_levels/data_weaver/parallel_engine.py
import dask.dataframe as dd

def parallel_process(df_path):
    ddf = dd.read_csv(df_path)
    return ddf.groupby("team").mean().compute()

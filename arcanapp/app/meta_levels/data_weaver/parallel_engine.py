from dask import delayed, compute

@delayed
def process_match(match):
    return match.analyze()

def parallel_process(matches):
    tasks = [process_match(m) for m in matches]
    results = compute(*tasks)
    return results

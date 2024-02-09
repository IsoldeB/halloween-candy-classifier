import pandas as pd
def read_file(filename):
    candy = pd.read_csv(filename)
    return candy

import pandas as pd

def dedup():
    df = pd.read_csv("Contributors.csv",header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv("Contributors.csv")
    print('Done!')

if __name__ == "__main__":
    dedup()
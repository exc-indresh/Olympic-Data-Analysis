import pandas as pd

def preprocess(df, region_df):

    # filtering for summer olympic
    df = df[df['Season']=='Summer']
    # merging with the region_df
    df = df.merge(region_df, on='NOC', how='left')

    # dropping duplicates
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

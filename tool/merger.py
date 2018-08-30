import pandas as pd


def series_normalize(series_):
    series_ = (series_ - series_.min()) / (series_.max() - series_.min())
    return series_


def df_normalize(df_, column):
    df_[column] = (df_[column] - df_[column].min()) / (df_[column].max() - df_[column].min())


def df_rank_no_return(df_, column, method='min'):
    df_[column] = df_[column].rank(method=method)


def df_rank_with_return(df_, column, method='min'):
    return df_[column].rank(method=method)


def series_rank(series, method='min'):
    return series.rank(method=method)


def merge(base, target, id_, map_, save_='out.csv'):
    df = None
    keys = []
    weights = []
    for key_ in map_:
        if df is None:
            df = pd.read_csv(base + key_)
            df.rename(index=str, columns={target: key_}, inplace=True)
        else:
            df_ = pd.read_csv(base + key_)
            df[key_] = df_[target]
        keys.append(key_)
        weights.append(map_[key_])
    df[target] = df[keys].mul(weights).sum(1)
    df_normalize(df, target)
    df[[id_, target]].to_csv(save_, index=False)

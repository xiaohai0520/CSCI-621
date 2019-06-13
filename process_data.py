
import pandas as pd


def read_data(file,cols):
    """
    read the csv file with pandas
    :return: the movie data
    """
    # get all the data
    data = pd.read_csv(file)

    # print(data.columns.values.tolist())

    # get the cols title, genres, year, score, budget, director, actors
    data = pd.read_csv(file,usecols=cols)

    # clear the nan
    data = data.dropna(axis=0,how='any')

    # print(len(data))
    # print(data.head())
    return data


# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split 
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

def pre_process(x):
    if x>3:
        return 'positive'
    elif x<3:
        return 'negative'
    else :
        return 'neutral'
    
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    # Loading data and adding labels
    df = pd.read_csv("./data/raw/tripadvisor_hotel_reviews.csv")
    df['Label'] = df['Rating'].apply(pre_process)

    # Separating the data by labels
    df_pos = df[df['Label']=="positive"]
    df_neg = df[df['Label']=="negative"]
    df_neu = df[df['Label']=="neutral"]

    # Split the data
    pos_train, pos_test = train_test_split(df_pos,test_size=0.3)
    neg_train, neg_test = train_test_split(df_neg,test_size=0.3)
    neu_train, neu_test = train_test_split(df_neu,test_size=0.3)

    # Concatenate the dataframes
    df_train = pd.concat([pos_train,neg_train,neu_train])
    df_test  = pd.concat([pos_test,neg_test,neu_test])

    # Save the data
    df_train.to_csv("./data/processed/train.csv")
    df_test.to_csv("./data/processed/test.csv")


if __name__ == '__main__':
    main()

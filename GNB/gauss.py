import pandas as pd
from sklearn.naive_bayes import GaussianNB

def GNB_model (file_path):
    training_df = pd.read_csv (file_path, header=None)

    # the label is the last column of the dataset
    labels = training_df[1024].to_numpy()

    # deletes label of EACH ROW (somehow pandas makes magic like this happen) and sends features to array
    del training_df[1024]

    # df.to_numpy() is csv in 2d array format
    training_features = [x for x in training_df.to_numpy()]

    # fit model 
    model = GaussianNB()
    model.fit(training_features,labels)

    return model
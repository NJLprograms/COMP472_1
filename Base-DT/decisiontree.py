import pandas as pd
from sklearn import tree

def DT_model(training_file):

  # Read csv file
  df = pd.read_csv ('../Assig1-Dataset/train_1.csv', header=None)

  # Store labels
  labels = df[1024].to_numpy()

  # Trim labels from features
  del df[1024]

  # each row is a list and all rows are in a bigger list that contains the whole lot
  features = [feature for feature in df.to_numpy()]

  # DT model
  model = tree.DecisionTreeClassifier()
  model = model.fit(features, labels)
  return model
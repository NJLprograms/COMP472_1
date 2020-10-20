from sklearn.linear_model import Perceptron
import pandas as pd

def perceptron_model(training_file):
  df = pd.read_csv(training_file, header=None)
  
  labels = df[1024]

  del df[1024]

  features = [feature for feature in df.to_numpy().tolist()]

  model = Perceptron()
  model.fit(features, labels)

  return model
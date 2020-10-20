import matplotlib.pyplot as plt

def plot_distribution(data_set, title):
  plt.title(title)
  plt.hist(data_set)
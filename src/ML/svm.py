from sklearn.svm import SVC
import numpy as np
from scraper import scrape
import data

dataset = data.Dataset(500, 8)

X = dataset.load_dataset('train')
Y = dataset.load_dataset('test')

clf = SVC()
clf.fit(X, Y, verbose='True')
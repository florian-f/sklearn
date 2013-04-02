import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC()
clf.fit(X, y)

from sklearn.svm import jSVC
jclf = jSVC()
jclf.fit(X, y)
jclf.jpredict([0,0])

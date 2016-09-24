import numpy as np
from sklearn import metrics

def time_series_cv(estimator, X, y, folds=5, metrics_f=metrics.mean_squared_error):
    '''
    Performs cross validation on ESTIMATOR and the data (X, y) using
    forward chaining.
    The score is the result of metrics_f(prediction, train_part_y)
    Here is the example of the data split to 6 folds
    for list [1 2 3 4 5 6]:
    TRAIN | TEST
    [1] | [2]
    [1 2] | [3]
    [1 2 3] | [4]
    [1 2 3 4] | [5]
    [1 2 3 4 5] | [6]
    '''
    assert X.shape[0] == y.shape[0], "Features and targets of different sizes {} != {}".format(\
    X.shape[0], y.shape[0]
    )

    results = []
    fold_size = int(np.ceil(X.shape[0] / folds))

    for i in range(1, folds):
        split = i*fold_size
        trainX, trainY = X[:split], y[:split]
        testX, testY = X[split:], y[split:]
        estimator.fit(trainX, trainY)
        predictions = estimator.predict(testX)
        results.append(metrics_f(predictions, testY))

    return np.array(results)

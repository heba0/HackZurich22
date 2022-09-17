import joblib


def serialize(value, filename):
    joblib.dump(value=value, filename=filename)


def deserialize_and_return(filename):
    return joblib.load(filename=filename)

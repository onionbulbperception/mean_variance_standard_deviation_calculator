import numpy as np

def calculate(list):

    # Throws ValueError if list contains less than 9 elements
    # "Must contain 9" so '<' is not valid here
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshaping input
    input = np.array(list).reshape((3, 3))

    # Calculations in dict and returned as lists
    calculations = {
        # https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html
        'mean': [
            np.mean(input, axis=0).tolist(),
            np.mean(input, axis=1).tolist(),
            np.mean(input).tolist()
        ],
        'variance': [
            np.var(input, axis=0).tolist(),
            np.var(input, axis=1).tolist(),
            np.var(input).tolist()
        ],
        'standard deviation': [
            np.std(input, axis=0).tolist(),
            np.std(input, axis=1).tolist(),
            np.std(input).tolist()
        ],
        'max': [
            np.max(input, axis=0).tolist(),
            np.max(input, axis=1).tolist(),
            np.max(input).tolist()
        ],
        'min': [
            np.min(input, axis=0).tolist(),
            np.min(input, axis=1).tolist(),
            np.min(input).tolist()
        ],
        'sum': [
            np.sum(input, axis=0).tolist(),
            np.sum(input, axis=1).tolist(),
            np.sum(input).tolist()
        ]
    }

    return calculations
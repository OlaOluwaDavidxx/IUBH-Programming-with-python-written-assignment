import pandas as pd


def final_data(test, delta, match):
    """
    The final dataset from calculated test, and delta
    :param test: the test dataset
    :param delta: the calculated delta
    :param match: the calculated match
    :return: Dataframe or raises an error
    """
    try:
        dicts = {
            "X (test function)": test.x,
            "Y (test function)": test.y,
            "Delta Y (test function)": delta,
            "No. of ideal func": match,
        }

        return pd.DataFrame(dicts)

    except Exception as err:
        print(f"status: Error Code \ncode: {err.code} \nmessage: {err.message}")
        
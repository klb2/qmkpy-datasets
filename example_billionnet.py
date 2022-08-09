import os
import os.path
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import qmkpy

REG_FILENAME = r"qmkp_([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+).txt"
COLUMNS = ["problem", "N", "K", "d"]

def main(dataset):
    ALGORITHMS = {
                  "CP": qmkpy.algorithms.constructive_procedure,
                  "FCS": qmkpy.algorithms.fcs_procedure,
                  "Random": qmkpy.algorithms.random_assignment,
                 }
    COLUMNS.extend(list(ALGORITHMS.keys()))

    problems = os.listdir(dataset)
    results = pd.DataFrame.from_records([{"problem": _p} for _p in problems],
                                        index="problem", columns=COLUMNS)
    for problem in problems:
        _filename_match = re.match(REG_FILENAME, problem)
        num_items, dens, num_ks, counter = _filename_match.groups()

        # Filter problems to only use the ones with at most 100 items
        # and 5 knapsacks
        # and 50 or 25 as density
        if int(num_items) > 100: continue
        if not int(num_ks) == 5: continue
        if not (dens == "50" or dens == "25"): continue

        print(f"Working on problem: {problem}")
        problem_path = os.path.join(dataset, problem)
        qmkp = qmkpy.QMKProblem.load(problem_path, strategy='txt')
        for _name, _algorithm in ALGORITHMS.items():
            qmkp.algorithm = _algorithm
            _assignments, _profit = qmkp.solve()
            _row = pd.DataFrame.from_records([{
                "problem": problem,
                _name: _profit,
                "N": int(num_items),
                "K": int(num_ks),
                "d": float(dens),
                }], columns=COLUMNS, index="problem")
            results = results.combine_first(_row)

    results = results.dropna()
    print(results)

    # Plot results
    group_dens = results.groupby("d")
    group_dens.mean().plot(y=list(ALGORITHMS.keys()), kind="bar")
    return results


if __name__ == "__main__":
    THIS_DIR = os.path.dirname(__file__)
    DATASET = os.path.join(THIS_DIR, "datasets", "billionnet")
    results = main(DATASET)
    plt.show()

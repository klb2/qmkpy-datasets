import os
import os.path

import pytest

from qmkpy import QMKProblem


CUR_DIR = os.path.dirname(__file__)
DATASETS = [d for d in os.listdir(CUR_DIR)
            if os.path.isdir(os.path.join(CUR_DIR, d))
            and not d.startswith("_")
            and not d.startswith(".")
           ]

def _map_extension_to_strategy(ext):
    mapping = {".txt": "txt",
               ".npz": "numpy",
               ".qmkpy": "pickle",
              }
    return mapping[ext]

@pytest.mark.parametrize("dataset", DATASETS)
def test_load_all_problems(dataset):
    dataset_path = os.path.join(CUR_DIR, dataset)
    problems = os.listdir(dataset_path)
    for problem in problems:
        strategy = _map_extension_to_strategy(os.path.splitext(problem)[1])
        problem_path = os.path.join(dataset_path, problem)
        qmkp = QMKProblem.load(problem_path, strategy=strategy)

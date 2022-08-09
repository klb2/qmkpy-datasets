# QMKPy Datasets
This repository contains a collection of reference datasets for the quadratic
multiple knapsack problem (QMKP).
They are intended to be used with the [QMKPy
library](https://github.com/klb2/qmkpy).

## Installation and Usage
In order to install and use the datasets, you simply need to download (or
clone) this repository.
Additionally, you need to have `qmkpy` installed, e.g., by using
```bash
pip3 install qmkpy
```

The datasets can then be loaded via the `qmkpy.io.load_problem` function.
For more details and examples, please refer to the [documentation of
QMKPy](https://qmkpy.readthedocs.io/en/latest/datasets.html).


## Available Datasets
All datasets can be found in the `datasets/` directory.
The currently available datasets are the following:

- `billionnet`: This is a popular dataset created by Billionnet and Soutil. It
  was originally created for the quadratic single knapsack problem[^1][^2].
  The original problems can be found
  [here](https://cedric.cnam.fr/~soutif/QKP/QKP.html). For the adaption to the
  quadratic _multiple_ knapsack problem, all knapsacks are set to have the same
  capacity which is equal to 80% of the sum of all item weights divided by the
  number of knapsacks. This version of the dataset has already been used in
  literature for the QMKP[^3][^4][^5][^6].


## Examples
Some example script are additionally provided in this repository.
They demonstrate how the datasets can easily be used with any solution
algorithm.

In order to run the examples, you need to install additional packages via
```bash
pip3 install -r requirements.txt
```

The following examples are provided:

- `example.py`: Generic script to run through all problems in a dataset and
  solve them with multiple algorithms.
- `example_billionnet.py`: Example script to use the Billionnet dataset. It
  demonstrates how the dataset can be filtered to only consider problems with a
  certain density and/or number of items/knapsacks.



## References

[^1]: Alain Billionnet and Eric Soutif. "Using a Mixed Integer Programming Tool
	  for Solving the 0-1 Quadratic Knapsack Problem", INFORMS J. on Comput
	  vol. 16(2): 188-197, 2004.

[^2]: Alain Billionnet and Eric Soutif. "An exact method for the 0-1 Quadratic
	  Knapsack Problem based on Lagrangian Decomposition", European J. of
	  Operational Research vol. 157(3): 565-575, 2004.
	
[^3]: Amanda Hiley and Bryant A. Julstrom. "The quadratic multiple knapsack
	  problem and three heuristic approaches to it", Proceedings of the 8th
	  annual conference on Genetic and evolutionary computation (GECCO ‘06),
	  pp. 547–552, 2006.

[^4]: Carlos García-Martínez, Francisco J. Rodriguez, and Manuel Lozano.
	  "Tabu-enhanced iterated greedy algorithm: a case study in the quadratic
	  multiple knapsack problem." European Journal of Operational Research
	  232(3): 454-463, 2014.

[^5]: Yuning Chen, Jin-Kao Hao, and Fred Glover. "An evolutionary path
	  relinking approach for the quadratic multiple knapsack problem."
	  Knowledge-Based Systems 92, pp. 23-34, 2016.

[^6]: Méziane Aïder, Oussama Gacem, and Mhand Hifi. "Branch and solve
	  strategies-based algorithm for the quadratic multiple knapsack problem",
	  Journal of the Operational Research Society, vol. 73, no. 3, pp. 540-557,
	  2022.

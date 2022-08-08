# Datasets

The provided datasets in this directory are the following

## Billionnet
This is a adjusted dataset from the original quadratic single knapsack problem
dataset by Billionnet and Soutif, which can be found at
[https://cedric.cnam.fr/~soutif/QKP/QKP.html](https://cedric.cnam.fr/~soutif/QKP/QKP.html).

The dataset has been adapted to the QMKP for the number of knapsacks
$K \in \{3, 5, 10\}$ knapsacks.
In each case, the knapsacks have the capacity of 80% of the total weight of all
items divided by the number of knapsacks $K$.

The file naming is as follows: `qmkp_<N>_<d>_<K>_<id>.txt` where `<N>` is the
number of items, `<d>` is the density (in percent), `<K>` is the number of
knapsacks, and `<id>` is a running counter.

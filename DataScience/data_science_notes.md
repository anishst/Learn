# Data Science

- data wrangling


## Role

- Data Scientist
- Data Analyst - uses BI tools
- Data Engineer - env

## Common Statistics Terms

- **Probability** is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.
- measures of central tendency
    - mean - arithmetic average
    - median - middle value; if even number then average of 2 middle values 
    - mode - most frequent value

## Common Libraries

- NumPy
    - support for large n-dimensional arrays (ndarray)
    - written in C lang
    - faster than python Lists; more memory efficient
    - get help : ```help(np.genfromtxt)```
    - Examples
        - calc median of each row ```np.mean(dataset, axis=0)```
        - ```np.sort(dataset)```
        - find out shape: ```dataset.shape```
        - reshape: ```x.reshape(1,3)```
        
- SciPy
- Pandas
    - built on top of NumPy
    - easy to use than NumPy
- Scikit-learn : built on top of SciPy
- matplotlib


## Data Set Sources

- Stack Overflow: https://insights.stackoverflow.com/survey
## plotly
https://plot.ly/python/

```pip install plotly```

### Anancoda package
- comes with all common libs; and juypter notebook
conda list - show list of packages

### Common Issues
- https://community.plot.ly/t/why-plotlyrequesterror-no-message/8307/8

## Jupyter

- http://jupyter.org/index.html
- https://jupyter.readthedocs.io/en/latest/index.html
- https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

shutdown  jupyter command window: ctr+c 2 times

## Jupyter commands
- Ctrl + Enter - run code
- Shitt + Enter
- m - markdown mode
- b - add cell below
- a - add cell above
- j - to moved down in command mode
- k - to move up in command mode
- d - delete current cell

## Magic commands
- pwd - current working dir
- %quickref - shows quick refs
- %env - show env vars
- %timeit EXPRESSION - time to execute
- ! - excecute os command; ex. !python-V / !dir c:\myfolder

## Numpy

```python
import numpy as np
python_list = [1,2,3,4,5]
np_array = np.array(python_list)

# get size or array
np_array.shape

# create dummy data - one dim array
np.random.seed(10)
sales = np.array((100 * np.random.rand (5)).astype(int)); sales


# create dummy data - multi-dim array of 3 rows and 5 columns
np.random.seed(10)
sales = np.array((100 * np.random.rand (3,5)).astype(int)); sales
```

## Descriptive statistics

- mean, median, mode
    - mean(), std()
- min/max values
    - min(), max()
- correlation - relationshipt between 2 vars
- covariance

## Code examples

import numpy as np

np.st*?
 - list of functions that start with st. 


## LaTex Equation editing

## Tools

- Goodle colabs: https://colab.research.google.com/
- Jupyter notebooks
- Google Data Studio - https://datastudio.google.com/
    - Tutorials:
        - https://towardsdatascience.com/how-to-build-a-great-dashboard-ee0518c3d3f7
## Vidoes

- https://www.youtube.com/watch?v=_P7X8tMplsw&t=29s

# Machine Learning (ML)

3 main types of ML

- unsupervised learning
    - clustering
        - k-means
        - db scans
- supervised learning
- reinforcement learning

- features and observations
- ROC Curve
- k-Nearest neighbors
- clustering: https://scikit-learn.org/stable/modules/clustering.html
-XGboost

free book: An Introduction to Statistical Learning; http://faculty.marshall.usc.edu/gareth-james/ISL/

https://scikit-learn.org/stable/

	

## Tools

- Tableau
- R/RStudio
- Jupyter
- Matlab
- Google Data Studio
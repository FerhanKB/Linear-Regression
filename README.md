# Linear Regression Model from Scratch in Python
## Libraries
First thing you need to build a linear regression model is to install the following libraries.
* [NumPy](https://numpy.org/install/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

## Data Generation
To generate train data pick any reasonable value of m and c as ground truth model parameters. For a sorted array of values x, generate the corresponding y values by using the equation `y = mx + c + rand()`

Save these datapoints in a csv file so that you don't lose these values using csv library.

To get a visual representation of these values plot them using matplotlib.

## Training the Model
Your loss function is `(t_i -y_i)^2`
where `y_i = mx_i + c` **(Note: no rand() function in this fitting part)**

You can select the step size **h** and learning rate **alpha** according to your need.
Start with a random value of m and c (generated using rand()) and iteratively optimize the objective through numerical derivative calculation and the update equation.
The numerical derivate w.r.t m and c is, `dl/dm = f(m+h,c) - f(m,c) / h` and `dl/dc = f(m,c+h) - f(m,c) / h` respectively.
Whenever the sign of either of the dl/dm and dl/dc gradients changes in between two consecutive iterations we halve the size of alpha so that we don't miss optimum values for **m** and **c**.

Run this for a number of epochs/iterations and choose the values of parameter where loss is minimum. These are the optimum parameters for the Model. 

Now you can test your model on a random input value.

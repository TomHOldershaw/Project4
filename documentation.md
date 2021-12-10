# Documentation

## Data Processing

* We filter the Etherium results from our SQL table as we are building a model to predict Etherium values. 

* Analyise for null values (of which there were none is our dataset). 

* We then set our index, the correct format for datatime and convert all dimensions to numerical values. 

## Model Selecting

* For this model, we want to be able to predict the closing value of Etherium and set this our label. Meanwhile all other features become our X values. 

As our data is time-dependent, we need to use times series split for validation. 

n_splits = 3. As we have 4 years of data it will split like this:

### 1st Split: 

TRAIN: Year 1

TEST: Year 2

### 2nd Split: 

TRAIN: Year 1 and Year 2

TEST: Year 3

### 3rd Split: 

TRAIN: Year 1, Year 2 and Year 3

TEST: Year 4

After conducting our algorithm comparisson, we can see that linear regression is our best choice (0.996457).

At this point, we can proceed with creating training and test sets for our linear regression model. 

![](lr_img1.jpg?raw=true "Title")

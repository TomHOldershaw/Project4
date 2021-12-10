# Crypto Prediction

## Team members
* [Abdurrahman Raja](https://github.com/Abzraja)
* [James Lilley](https://github.com/jimbleslilley)
* [Serdar Bayramov](https://github.com/serdar-bayramov)
* [Tom Oldershaw](https://github.com/TomHOldershaw)

## Project overview
The project is designed to predict the future value of crypto currency. The data extracted covers a number of coins, and in theory there is no restriction on the application of the model, subject to re-training the model for each coin. 

At present, the project produces models only for Ethereum.

## Intended use
The intended use of the project is to produce forecasts of coin prices to inform investment decisions. With time, the intention is to develop a front end to display these predictions. In this use case, the trained model would be used to forecast from the latest price points obtained from the API at the point of prediction.

## Database
The project made use of the [previous code produced by the team](https://github.com/Abzraja/project-3) to extract information from the Binance API. In a change to the previous code, data was extracted for 4 years and stored in an AWS database.

The data was obtained from the AWS database by the model scripts using a SQL Alchemy connection. The connection details and password were stored in a configuration file.

## Project steps
The project steps are illustrated below.

Technical details are provided on key stages in this process:
 - [Model investigation](documentation.md#model)
 - [Linear Regression model](documentation.md#lr)
 - [Long Short Term Memory model](documentation.md#lstm)

Model notebooks are:
 - Model investigation
 - Linear Regression
 - [Long Short Term Memory](ETH_RNN_1.ipynb)

# Conclusions
We investigated several model forms, and developed models for two of them. Following this work, we would recommend adopting the WHICH MODEL
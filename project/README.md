# Midterm project instructions

### due Tuesday, March 2 at 12:30 pm

## Overview

You have been randomly assigned **two datasets** to explore using the tools and concepts from class to date. Respond clearly to each of the data-based and written questions.

In general, **do this like you would a homework** (see exception below in 'honor code')

- Syllabus instructions on how to display your answers to computational questions apply here as well. Please review this in the syllabus, as I will be less lenient about it than for homework.

- Written answers must be clearly argued using concepts from the course.

## Honor code, open-book test-like conditions

- Unlike for homework, **you must work on this alone. No collaboration or communication among students about topics related to this project is allowed whatsoever.**

- you can however use various online sources to help you with excel or python, as we've done for homework.

- **explicitely disallowed are asking for or gathering help for this project on any online forums**.

Running afoul of these policies will be considered a potential honor code violation.



## How to get your datasets

1. On the sakai page, in resources, select the 'project_assignments.csv' file (open in excel or python). There, you will find a spreadsheet with your name onyen in one column and your project ID in another.

2. Download the **two** project datasets associated with your ID on the course github page, at `github.com/brendanrbrown/stor155_sp21/project` in the CV and FRED folders

For example, if my project ID is 21 then I would download the datasets called

- `FRED_21.xlsx`
- `CV_21.xlsx`

**If you are uncertain about how this process works, speak to me immediately.** There will be no extensions or other leniency for failing to use the correct dataset. You must use the data assigned to you.

## How to turn in your project

- The exact same way as for homework.
- **If you are working in excel:** You will turn in two spreadsheets. Do not change the names of your assigned datasets. So if your project ID is 21, you will turn in two completed excel workbooks called `FRED_21.xlsx` and `CV_21.xlsx`.
- If working in python, you may turn in one notebook so long as the file path for importing the data is clear (just do what we've been doing in homework).


## Total: 100 points

# Part one (40 points): FRED economic time series

Load the appropriate FRED dataset associated with your project ID. See instructions above.

The dataset file name will begin with `FRED_`

## Q1 (2.5 points)

There are three variables in the dataset: date, and three time series variables.

- **search for the codes of the non-date variables in FRED** in the search bar at [https://fred.stlouisfed.org/](https://fred.stlouisfed.org/)
- there should be exactly one result for each variable
- **replace the original variable name with one that is more human-readable** using that resource. 
- **write a brief sentence describing what the dataset includes, touching on**:
    - variable types available (numeric, categorical etc)
    - scope in terms of span and frequency in time of your observations, and the geography to which they relate

Name it what you like, but it should be short and as clear as possible. Use the variable names from past homework as a guide if needed.

You might need to use basic methods to look at your data, seen in homework, along with the information on the FRED website, to write the summary sentence.

## Q2 (5 points)

- **count** the number of missing values (including blanks if using excel) in each non-date variable
- **calculate and display the following summary statistics** about each non-date variable
    - variance
    - mean
    - median
    - range
    - 90 percentile/quantile
    

## Q3 (2.5 points)

- create and display a **time series plot** where each of the non-date variables is plotted on the y-axis against the date variable on the x axis.
- Your plot must have at least a relevant title and otherwise be clearly legible.

You may use the default colors in the tool of your choice to differentiate the variables

## Q4 (10 points)

- **create a new variable with the period-to-period changes** in your time series variables --- one for each non-date variable. Give them reasonable names of your choice.
- **create a scatterplot** between two of these newly created variables. You may choose any pair of variables to compare here.

## Q5 (10 points)

- using the scatterplot created in Q4 between your two chosen variables, **describe in one or two sentences what the plot says about the relationship between those two variables.**

You should use concepts discussed in class and homework in your answer.

## Q6 (10 points)

- **compute and display the correlations between all of your non-date variables** 
- in two or three sentences, **explain why these correlations do or do not make sense relative to the plots created in Q4, Q3**



# Part two (60 points): NYT coronavirus data

See instructions above for downloading your assigned dataset. The dataset file name will begin with `CV_`

You have been assigned coronavirus data for a single state, with county-level data for

- cases
- deaths
- survey results on mask usage

These datasets are described in greater detail at [https://github.com/nytimes/covid-19-data](https://github.com/nytimes/covid-19-data)

The cases and deaths data come from the `counties.csv` file at that site, and the mask usage data are in the `mask-use` subfolder. I have done some data cleaning, joining and aggregating, so the data you have is not the raw dataset there.



## Q1 (10 points)

- **create histograms** for the cases and the deaths variables. These may be on separate plots or not, your choice. Your plot must have a reasonable title.

## Q2 (5 points)

- **compute and display the following statistics** for each of the cases and deaths variables
    - range
    - 25th quantile/percentile
    - median
    - 75th quantile/percentile
    - mean
    - variance
    
- **in a sentence or two, compare these statistics with the histograms** and explain exactly why they do or do not make sense, using concepts from class and the definitions of those statistics.

## Q3 (5 points)

- **create a new variable** called `masks_check` that adds up all `masks` variables for each observation
- **check** (using a function) what proportion new variable values do not sum to 1 (including possibly all or none).


## Q4 (10 points)

- **create a new variable** called `masks_use` that is the sum of `masks_frequently` and `masks_always`
- **calculate the correlation** between `masks_use` and `cases`
- **calculate the correlation** between `masks_use` and `deaths`

## Q5 (10 points)
- **create a new variable** called `masks_group` that has value 1 if `masks_use` is greater than 0.5 and 0 otherwise. As in homework, pandas users may use variables with True/False values.
- **calculate** the average value of `masks_group`
- **briefly explain** what this average value represents

#### IMPORTANT:
If (and only if) *all* of your observations have a `masks_use` that is greater than 0.5, then use a 0.9 cutoff instead.

## Q6 (15 points)

- **create a pivot table** (or a grouped data frame summary table for pandas users, as in homework) which groups observations by `masks_group` and calculates the following quantities for each subgroup
    - average deaths
    - average cases
    - number of observations in the group

## Q7 (5 points)

- **briefly compare**, in two or three sentences, your results from Q6 and Q4
- state clearly why they do or do not make sense together, using concepts from class

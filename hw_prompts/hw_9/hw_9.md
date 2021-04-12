# hw 9
### due April 13, 12:30 pm

### data
We will work with food inspections data (restaurants mainly) from the City of Albequerque, in particular inspections for violations of requirements a facility is 'following current COVID Safe Practices for employee mask use'.'

Data from: http://www.cabq.gov/abq-data
Some (limited) info on the data: http://data.cabq.gov/business/foodinspections/MetaData.pdf

I have taken only the subset of the data dealing with violation code 04c210, the violation described above.

The data cover inspections in the time period from Oct. 31, 2020 to March 24, 2021.

#### important variables
You have many variables you won't use here. That is typical. Feel free to explore more of the data. You can even find out exactly which businesses were forced to close for such violations.

These variable descriptions are based on my exploration of the data, reading the docs, and brief internet searches elsewhere. They are not meant to be super precise. In a real scenario, you'd spend more time to understand exactly what you have.

- `result_desc` gives the result of the inspection
- `action_desc` gives the action taken by the city based on the results of the inspection
- `not_masked` is a variable I created to mark which businesses passed inspection for checks of the employee mask use violation. It is `False` if `action_desc = approved` and `True` otherwise.

#### `abq_bigsamp`

- 100 random samples from the original dataset
- each of size 50

#### `abq_smallsamp`

- 100 random samples from the original dataset
- each of size 5

# Q1

- **get** the `abq_bigsamp.csv` and `abq_smallsamp.csv` files
- **Excel users:**  must put these in different sheets of a single workbook. **Do not submit separate files**. You've been warned!
- **List** the possible values for the `result_desc`, `action_desc` and the `not_masked` variables (same for both datasets)

# Q2

- **create** a pivot table (excel) or grouped data frame summary (python) showing the **number of observations in the bigsample data** by pairs of `action_desc` and `result_desc` values
- **create** ... by pairs of `action_desc` and `not_masked` values

Remember, groups defined by pairs of variables means, for example that all observations with `action_desc = approved` and `result_desc = in compliance` are in one group. All observations with `action_desc = approved` and `result_desc = not in compliance` are in a *different* group, etc.

# Q3
Remember `sampid` identifies the random sample of rows taken from the original dataset. All rows in the big dataset with the same `sampid` are in the same sample. Same for the small dataset.

- **create a variable called `phat`** giving the proportion of rows where `not_masked` is true **only using data for the group `sampid = 0` in the bigsamp dataset**
- **create a variable called `sehat_small`** giving a *point estimate* for the standard deviation *of the sample mean* **for a sample of the same size as those in the smallsamp** dataset (see the `sampsize` variable)
- **create a variable called `sehat_big`** ... **for a sample of the same size as those in the bigsamp** dataset

# Q4
- **create a variable called `mhat_big`** calculating the proportion of rows **within each `sampid` group** where `not_masked` is true **for the bigsamp** dataset
- **create a variable called `mhat_small`** ... **for the smallsamp** dataset

Hint: Use a pivot table / groupby

# Q5

- **For each observation in `mhat_small` calculate** a 95 percent confidence interval for `phat` centered at the `mhat_small` value and using `sehat_small`. **Create different variables for the low and high endpoints of the interval, called `ci_small_low` and `ci_small_high`.**
- **For each observation in `mhat_big` calculate** ... centered at the `mhat_big` and using with `sehat_big` ... **`ci_big_low` and `ci_big_high`.**

# Q6

- **write a brief interpretation** of **one** of the confidence intervals for the unknown proportion using `sehat_big` in terms of concepts from class. In particular, what does this interval tell you about the true value of this proportion, and what does it not? It doesn't matter which of the intervals you choose.

# Q7

**Using the data in `abq_truepar`**

- **calculate** the true proportion of cases in the original data where `not_masked` is true, and call this `ptrue`. **Unlike other hw Qs, you can just enter the numbers from the abq_truepar dataset viewed on github**. You don't need to load the data if you don't want to.
- **calculate** the proportion of times `ptrue` lies within the confidence interval you calculated using `sehat_small`, meaning the proportion of times `ci_small_low <= ptrue <= ci_small_high`
- **calculate** ... (the same stuff but with) `sehat_big` ... proportion of times `ci_big_low <= ptrue <= ci_big_high`

# Q8

- **explain in words** your answer in Q7 using concepts from class
- **in particular:**
    - how does the result from Q7 compare with your answer to Q6?
    - how does the small-sample CI compare to the big-sample CI?
    - if they are different, why might they be different? If not, why not?

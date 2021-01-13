# Stor155
### section 2, spring 2021
This repository primarily serves as an easy way for me to share data with students in the course, and also holds other course-related content.

### To get data for homework

If using excel (default):

1. click the 'data' folder link
2. find the dataset you need. **click the .xlsx version link**


If using python

1. click the 'data' folder link
2. find the dataset you need. **click the .csv version link**
3. in the preview pane, on the top right, click the 'raw' Instructions
4. copy the url to the 'raw' icon
5. add the code below to your Jupyter notebook to load the data as a dataframe called d

```
import pandas as pd

d = pd.read_csv('link_to_raw_file_on_github')
```

For example, to load the `wb_lifexpec.csv` dataset this way, you would include the following code

```
import pandas as pd

d = pd.read_csv('https://raw.githubusercontent.com/brendanrbrown/stor155_sp21/main/data/wb_lifexpec.csv')
```

Check that it loaded what you thought by running the following

```
d.describe()
```

or to see the first few lines

```
d.head()
```

### Instructions for submitting homework

If using excel:

If using python:





### Go to Sakai instead for

- syllabus
- links to video recordings of lectures

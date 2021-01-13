# Stor155
### section 2, spring 2021
This repository primarily serves as an easy way for me to share data with students in the course, and also holds other course-related content.

## Get data for homework/exercises

#### if using excel (default):

1. click the 'data' folder link
2. find the dataset you need. **click the .xlsx version link**
3. click the 'download' button

If using excel on your home computer, you can just open the downloaded file.

If using excel through Office 365, go to office.com and login with your UNC credentials. Click the 'Upload and open' link under the 'Recommended' list of files to upload your xlsx file.

Alternatively, you could navigate to onedrive in the left-hand menu and upload it to some folder of your choosing there.


#### if using python:

1. click the 'data' folder link
2. find the dataset you need. **click the .csv version link**
3. in the preview pane, on the top right, click the 'raw' button
4. copy the url to the 'raw' icon
5. add the code below to your Jupyter notebook for this assignment to load the data as a dataframe called d

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

## Instructions for submitting homework
Grades will appear on sakai

#### if using excel (default):
1. upload your excel workbook to Office 365 (if not already there).
2. open it, and click the 'share' link in the top right corner
3. enter my UNC email address (see the syllabus on Sakai) and click 'send'


#### if using python:





### Go to Sakai instead for

- syllabus
- links to video recordings of lectures

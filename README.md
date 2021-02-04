# Stor155: section 2, spring 2021
This repository primarily serves as an easy way for me to share data with students in the course, and also holds some resources for completing data homework.

## Help! Tips for data homework

### Expectations

- demos are to **give you a little head start** on the homework by demonstrating some relevant tools
- but you **should not expect to end the session with homework done** --- far from it
- expect to spend a substantial amount of time, if needed, learning how to do things
- by cutting back on other assignments, **I am giving you the time needed to do this**

The best way to follow along is to use exactly the tool I am using in the demos: Excel online or jupyter lab.

I can't spend class time debugging each person's slightly different Excel version. If you choose to use something different, that's up to you. What I demo should still give you a head start.

### If you're stuck

- **come to office hours**, which is why they exist
- **excel users** can come to either mine or the TA's office hours
- **python users** come to mine
- **email me** or the TA, but please see the email policy in the syllabus

### If you are in a different time zone / have poor connectivity

This definitely will make it more difficult for you to attend the Thursday demos. Email me and we'll work it out.

## Getting started

#### using excel (default):
I will be using the Office 365 online version of excel. If your internet connection is slow, you should consider downloading the desktop version of excel from software.sites.unc.edu if you don't already have it.

- **log in** to Office 365 with **username onyen@ad.unc.edu** and password at office, and select the excel app from the left-hand menu
- or **access onedrive / excel** directly in the top-left-hand menu of your email at live.unc.edu
- **download the excel_cookbook.xlsx** from the excel_help folder at github.com/brendanrbrown/stor155_sp21
- **upload this file to Office 365** and test it out!

**Note:** If you care about not being tracked online I suggest you use a browser such as Brave or Firefox (or Duckduckgo on mobile), which block many trackers automatically. The office.com and the live.unc.edu related sites have a large number of Microsoft-related trackers that have nothing to do with providing a useful service to you.

#### using python:
This will help you get started. Remember, it is **your responsibility** to handle any issues with installation, and any future computer issues related to running this software. I will **support you only in learning the coding tasks needed to do the work in this course.**

That said, this procedure should be smooth and easy for almost everyone.

- **install** Anaconda for Python 3.x (3.8 as of this syllabus writing) for your operating system at this link: https://www.anaconda.com/products/individual
- once installed, **open the Anaconda Navigator** application
- select **Jupyter Lab** or Jupyter Notebook from the Anaconda Navigator menu
- Jupyter Lab lets you create notebooks and also to manage your related files. Jupyter Notebook takes you straight to a single notebook. A notebook is the best way to run and display code for this course.
- **download the pandas_cookbook.ipynb** file in the notebooks folder of github.com/brendanrbrown/stor155_sp21 notebook to check that everything went smoothly
- test it out!


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
3. in the preview pane, on the top right, click the **'raw' button**
4. copy the url to the 'raw' icon
5. add the code below to your Jupyter notebook for this assignment to load the data as a dataframe called d (you could give it another name, but it is d in the example below)

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
Grades will appear on Sakai.

#### if using excel (default):
1. upload your excel workbook to Office 365 (if not already there). See the instructions under 'Getting started' above for how to log on.
2. open it, and click the 'share' link in the top right corner
3. enter my UNC email address (see the syllabus on Sakai) and click 'send'


#### if using python:
1. open your Jupyter notebook
2. select the Kernel menu item up top, and select 'Restart kernel and run all cells'. This restarts your session and runs all code cells from top to bottom, a great way to check for silly errors (I make them all the time).
3. Check for errors: If you did something like refer to an object name before creating it, you might get an error. This is a good chance to fix them.
4. **Export to html**: Under the file menu, click Export notebook as > Export notebook to html
4. Log onto Office 365 (see 'Getting started' excel instructions up top) and navigate to one drive
5. Upload your html file to one drive
6. Click the share button
7. enter my UNC email address (see the syllabus on Sakai) and click 'send'


## Working with others, using resources

Please do read the data homework section of the syllabus for these details. Your best option, in general, will be to simply attend the data lab sessions where we will cover much of what you need to do.

If you cannot attend those sessions, for example because you are in a different time zone, please email me. If there is enough demand I will set up an additional session at a more convenient time. Otherwise, I will work with those students on a case-by-case basis.

## Go to Sakai instead for

- syllabus
- lecture slides
- links to video recordings of lectures
- links to all other class resources

https://sakai.unc.edu/portal/site/stor15502_sp21

#!/usr/bin/env python3

"""
DO NOT PUT STUDENT-IDENTIFIABLE INFORMATION IN THIS SCRIPT

Course grade calculation. Takes gradebook_full.csv, calculates the final grade, the appends this as a new column to the original sakai gradebook for re-export.
"""

import pandas as pd


# HELPERS

def clean_sakai_names(d):
    """
    strips garbage columns from sakai gradebook export, clean names
    """
    d = d.drop(columns = d.columns.to_series().loc[d.columns.str.startswith(r"*")]).drop(columns = "Unnamed: 0")
    d.columns = d.columns.str.lower().str.replace("\\[[0-9]+\\]", "").str.strip().str.replace("\\s+", "_")
    
    return d

def clean_webassign(d):
    """
    takes output from _clean_sakai_names and cleans up the ND / NS values, converting those cols to numeric
    """
    webcols = d.columns.str.startswith("webassign")
    badcols = d.dtypes.eq("object") & webcols
    
    d.loc[:, badcols] = d.loc[:, badcols].apply(lambda s: s.str.replace("NS|ND", "0").astype("int64"))
    
    return d

def find_lowest_hw(d_weighted):
    """
    d_weighted should be the gradebook from gradebook_full after weights are applied as in weight_grades
    
    returns a series with student_id indices and values being the column name where min weighted grade is reached
    
    note this treats zeros as equal and will identify the first zero it encounters for dropping.
    """
    
    
    return d_weighted.set_index("student_id").filter(regex = "^hw|^webassign").idxmin(axis = 1)

def new_hw_weighted(x, worst_hw, weights, max_points):
    """
    computes new homework total for row x, representing a single student, by dropping worst_hw (a string) 
    and re-applying the weights. To be used in apply statement on the *unweighted* homework score, 
    so that the correct denominator for max_points can be applied.
    """
    
    # max_points index should already be set to assignment, but just in case I move this around later
    if max_points.index.name != "assignment":
        max_points = max_points.set_index("assignment")
        
    if weights.index.name != "item":
        weights = weights.set_index("item")
        
    max_points = max_points.filter(regex = "^hw|^webassign", axis = 0).drop(worst_hw)
    x = x.filter(regex = "^hw|^webassign").drop(worst_hw)
    
    hw_prop = weights.loc["datahw", "weight"] * x.filter(regex = "^hw").sum() / max_points.filter(regex = "^hw", axis = 0).sum()
    web_prop = weights.loc["webassign", "weight"] * x.filter(regex = "^webassign").sum() / max_points.filter(regex = "^webassign", axis = 0).sum()
    
    return hw_prop + web_prop
    

# MAIN FUNCTIONS
def numeric_grades(d, weights, max_points, full = False):
    """
    weights raw grades using the weights and max_points tables, returning a df with the same columns and index
       two-step process:
           - first calculate d_pre with preliminary weighted grade calcs as though all HW items included
           - find which homework has the lowest overall weighted score
           
    returns the numeric grades as a number between [0, 1]
    """
    
    d = clean_webassign(clean_sakai_names(d))
    
    # this is needed for .div which matches indices
    # and requires assignment in max_points to match colnames as output from the two operations above
    weights = weights.set_index("item")
    max_points = max_points.set_index("assignment")
    
    # weight all graded items by max
    d_pre = d.loc[:, "hw0":].apply(lambda x: x.div(max_points.pts), axis = 1)
    
    hw = d_pre.filter(regex = "^hw") * weights.loc["datahw", "weight"]
    web = d_pre.filter(regex = "^webassign") * weights.loc["webassign", "weight"]
    midterm = d_pre.loc[:, "mt"] * weights.loc["midterm", "weight"]
    final = d_pre.loc[:, "final"] * weights.loc["final", "weight"]
    pollev_part = d_pre.loc[:, "pollev_participation"] * weights.loc["pollev", "weight"] / 2
    pollev_acc = d_pre.loc[:, "pollev_accuracy"] * weights.loc["pollev", "weight"] / 2
    
    # grade calcs if no HW were dropped
    d_pre = pd.concat([d.loc[:, "student_id"], hw, web, midterm, final, pollev_part, pollev_acc], 
                     axis = 1)
    
    worst_hw = find_lowest_hw(d_pre)
        
    # final weighted grades. new_hw_weighted *already* acounts for 0.2 weighting
    out = d_pre.filter(regex = "student_id|^poll|mt|final"
                      ).assign(hw_total = d.apply(lambda x: new_hw_weighted(x, worst_hw.loc[x.student_id], weights, max_points), 
                                                  axis = 1))
    
    if full:
        return [out, out.set_index("student_id").sum(axis = 1)]
    else:
        return out.set_index("student_id").sum(axis = 1)
    


def letter_grades(grd_numeric):
    """
    """
    
    def _assign_letter(x):
        if x >= 0.93:
            g = "A"
        elif x >= .9:
            g = "A-"
        elif x >= (86 + 1/3)/100:
            g = "B+"
        elif x >= (83 + 2/3)/100:
            g = "B"
        elif x >= .8:
            g = "B-"
        elif x >= (76 + 1/3)/100:
            g = "C+"
        elif x >= (73 + 2/3)/100:
            g = "C"
        elif x >= .7:
            g = "C-"
        elif x >= (66 + 1/3)/100:
            g = "D+"
        elif x >= (63 + 2/3)/100:
            g = "D"
        elif x >= .6:
            g = "D-"
        else:
            g = "F"
        
        return g
    
    return grd_numeric.apply(_assign_letter)

    
# RUN
if __name__ == "__main__":
    
    d = pd.read_csv("grades/gradebook_full.csv")
    weights = pd.read_csv("grade_weights.csv")
    max_points = pd.read_csv("max_points.csv")
    
    grd_numeric = numeric_grades(d, weights, max_points)
    grd_letter = letter_grades(grd_numeric)
    
    out = pd.concat([grd_numeric, grd_letter], axis = 1).rename(columns = {0: "numeric_grade", 1: "letter_grade"})
    
    names = d.rename(columns = {"Student ID": "student_id", "PID": "pid", "Name": "name"}).set_index("student_id").loc[:, ["pid", "name"]]
    
    out = pd.concat([names, out], axis = 1)
    
    # want index here
    out.to_csv("grades/grades_course.csv")

    
    # prep for sakai reupload
    grd_numeric = 100 * grd_numeric.rename("course [100]")
    d = d.loc[:, "Student ID":"pollev_participation [100]"].merge(grd_numeric, left_on = "Student ID", right_index = True)
    d.to_csv("grades/gradebook_sakai_complete.csv", index = False)
    

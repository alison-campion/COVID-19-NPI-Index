import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from metadata import state_list, us_state_abbrev, npi, npi_weights

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['text.latex.preamble'] = [r'\usepackage[cm]{sfmath}']
mpl.rc('font',**{'family':'serif','serif':['Palatino']})
mpl.rc('text', usetex=True)
plt.rc('text', usetex=True)
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
mpl.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
mpl.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'



# get date range from the beginning of the year
date1 = '2020-01-01'
date2 = datetime.datetime.today().strftime("%Y-%m-%d")
mydates = [x.strftime("%Y-%m-%d") for x in pd.date_range(date1, date2).tolist()]

ph_data = {}

# ---------------------- #
# Structure the NPI Data #
# ---------------------- #
ph_codes = pd.read_csv("data/Public Health Events Data - Sheet1.csv", header=2)
ph_codes = ph_codes.set_index("Code", drop=True)

# cycle though thte states
for state in ph_codes.index:
    
    # create an empty dataframe for the state with all dates as columns and variables as index
    ph_data[state] = pd.DataFrame(index=ph_codes.columns, columns=mydates) 
    
    # cycle through the variables
    for var in ph_codes.loc[state].index:
        
        # skip if empty
        if type(ph_codes.loc[state].loc[var]) != str:
            continue
        
        # get the date range for this variable form the cell
        date_range = ph_codes.loc[state].loc[var].split("|")
    
        # convert the spreadsheet syntax to a date range
        dates = []
        for d in date_range:
                        
            # make sure there are no spaces in the date
            d = d.replace(" ", "")
            
            # if multiple dates listed, take last one (these are updated dates)
            if "*" in d:
                d = d.split("*")[-1]
                
            # drop information on required vs. recommended for now
            if "(" in d:
                d = d.split("(")[0]
                
            # if no date listed, insert today
            if d == "x":
                d = datetime.datetime.today().strftime("%Y-%m-%d")

            # put the dates in a list
            dates.append(d)

        # if there is only one date given, add on today
        if len(dates) == 1:
            dates.append(datetime.datetime.today().strftime("%Y-%m-%d"))
        
        # get all dates in the date range and store as a string
        try:
            dates = pd.date_range(dates[0], dates[1]).tolist()
        except ValueError:
            continue
            
        dates = [x.strftime("%Y-%m-%d") for x in dates]

        # for each date specified in the range, set this variable to 1
        for d in dates:
            ph_data[state].loc[var, d] = 1
            
# ---------------------- #
# Merge in COVID-19 Data #
# ---------------------- #
datafiles = os.listdir("COVID-19/csse_covid_19_data/csse_covid_19_daily_reports")
cases = {}
for file in datafiles:
    # check to make sure this is a datafile
    try:
        date = datetime.datetime.strptime(file,"%m-%d-%Y.csv")
    except:
        continue
    
    # set the date in the preferred format
    date = date.strftime("%Y-%m-%d")
    
    # read in the file
    df = pd.read_csv(f"COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/{file}")
    
    # identify the column names for country and state
    country_col = [x for x in df.columns if "Country" in x][0]
    state_col = [x for x in df.columns if "State" in x][0]
    
    # keep only the US data
    df = df.loc[df[country_col] == "US"].reset_index(drop=True)
    

    # split off the state from the province column
    temp = df[state_col].str.split(",", expand=True)
    if temp.shape[1] == 1:
        df = df.rename(columns={state_col: "state"})
    else:
        df["state"] = df[state_col].str.split(",", expand=True)[1]
        df["state"] = df["state"].str.split("(", expand=True)[0]

    # drop states that weren't really states (unassigned)
    df = df.dropna(subset=["state"])
    
    # replace sttate abbreviations with the full name
    df["state"] = df["state"].str.lstrip()
    df["state"] = df["state"].str.rstrip()
    df = df.replace({"state": us_state_abbrev})
    
    # manual cleaning/replacement
    df = df.replace({"state": {"D.C.": "Washington D.C."}})
    
    # group to the state level
    df = df[["state", "Confirmed", "Deaths"]].groupby(by="state").sum()
    
    for state in df.index:
        if state not in list(cases.keys()):
            cases[state] = {date: {"cases": df.loc[state, "Confirmed"],
                                   "deaths": df.loc[state, "Deaths"]}}
        else:
            cases[state][date] = {"cases": df.loc[state, "Confirmed"],
                                   "deaths": df.loc[state, "Deaths"]}
            
# convert case dictionaries to dataframes 
for state, v in cases.items():
    # only add the data if it already exists in the public health data
    if state in list(data.keys()):
        data[state] = data[state].append(pd.DataFrame(v))
        
# ------------------- #
# Calculate NPI Index #
# ------------------- #       
for state, d in data.items():
    df = d.T.fillna(0)
    df["npi_index"] = 0
    for k, v in npi_weights.items():
        df["npi_index"] = df["npi_index"] + df[k]*v
    data[state] = df.T.replace({0: np.nan}) 
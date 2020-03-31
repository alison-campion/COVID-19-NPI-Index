import os
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
from metadata import state_list

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['text.latex.preamble'] = [r'\usepackage[cm]{sfmath}']
mpl.rc('font',**{'family':'serif','serif':['Palatino']})
mpl.rc('text', usetex=True)
plt.rc('text', usetex=True)
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
mpl.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
mpl.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'

for state in state_list:
    print(f"Createing figure for {state}")
    
    # create figure
    f, ax = plt.subplots(figsize=[12, 8])

    # get state data 
    df = data[state].copy()
    df.columns = [datetime.datetime.strptime(x, "%Y-%m-%d") for x in df.columns]

    # plot case statistics
    ax.bar(df.columns, df.loc["cases"], color="#0086e6")
    ax.bar(df.columns, df.loc["deaths"], color="#a32100")

    # set xlimit for plot
    xlimits = [datetime.date(2020, 2, 15), datetime.date(2020, 4, 10)]

    # set date formatter
    date_fmt = mpl.dates.DateFormatter('%b %d %Y')

    # instantiate a second axes that shares the same x-axis
    ax2 = ax.twinx()  
    height = 0
    for var in df.index:
        if df.loc[var].sum() == 0:
            pass
        elif ((var == "cases") | (var == "deaths") | (var == "Unnamed: 17") | (var == "FC")):
            pass
        else:   
            xrange = list(df.loc[var].dropna().index)
            xrange = [mpl.dates.date2num(x) for x in xrange]

            # convert to matplotlib date representation
            width = xrange[-1] - xrange[0]

            # Plot rectangle
            length = 0.85
            rect = mpl.patches.Rectangle((xrange[0], height+1), width, length, color='#ffa600', alpha=0.25)

            # Add the patch to the Axes
            ax2.add_patch(rect)
            ax2.text(mpl.dates.date2num(xlimits[1]) + 0.5, 
                     height + 0.85 + length/2, npi[var]["name"], color='#ffa600', fontsize=14)

            # increment the height counter
            height = height + 1

    # Primary axis settings
    ax.legend(["Cases", "Deaths"], loc=2, fontsize=12)
    ax.yaxis.grid("--", alpha=0.5)
    ax.set_ylabel("Number of People", fontsize=12)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_xlim(xlimits)
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator(interval=1))
    ax.xaxis.set_minor_locator(mpl.dates.DayLocator([5, 10, 15, 20, 25]))
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%b %Y'))
    ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%d'))
    f.autofmt_xdate()
    ax.set_title(state, fontsize=16)

    # secondary axis settings
    ax2.set_yticks([])
    ax2.set_ylim(1, height+1)
    plt.savefig(os.path.join("data", "state_plots", f"{state}_npi.png"), bbox_inches="tight", dpi=300)
    plt.close('all')
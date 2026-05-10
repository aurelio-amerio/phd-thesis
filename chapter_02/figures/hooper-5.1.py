#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def init_matplotlib():
    plt.rcParams['figure.figsize'] = (6, 5)  # Set figure size

    plt.rcParams['axes.labelsize'] = 18  # fontsize of the x any y labels
    plt.rcParams['xtick.labelsize'] = 16  # fontsize of the tick labels
    plt.rcParams['ytick.labelsize'] = 16  # fontsize of the tick labels
    plt.rcParams['xtick.direction'] = 'in'  # direction: in, out, or inout
    plt.rcParams['ytick.direction'] = 'in'  # direction: in, out, or inout
    plt.rcParams['xtick.major.size'] = 6  # size of tick marks
    plt.rcParams['ytick.major.size'] = 6  # size of tick marks
    plt.rcParams['xtick.minor.size'] = 3  # size of tick marks
    plt.rcParams['ytick.minor.size'] = 3  # size of tick marks
    plt.rcParams['xtick.major.pad'] = 7  # distance between ticks and tick labels
    plt.rcParams['ytick.major.pad'] = 7  # distance between ticks and tick labels
    plt.rcParams['axes.grid'] = True  # Turn grid on by default
    plt.rcParams['grid.alpha'] = 0.5  # Set grid transparency to 0.5
    plt.rcParams['legend.fontsize'] = 16  # fontsize of the legend
    return

init_matplotlib()
#%%
# load hooper-fig5.1.csv
df = pd.read_csv("hooper-5.1.csv", comment="#")
#%%
#1GeV,,10GeV,,100GeV,,1TeV,,10TeV,
x_1GeV = df[df.columns[0]]
y_1GeV = df[df.columns[1]]
x_10GeV = df[df.columns[2]]
y_10GeV = df[df.columns[3]]
x_100GeV = df[df.columns[4]]
y_100GeV = df[df.columns[5]]
x_1TeV = df[df.columns[6]]
y_1TeV = df[df.columns[7]]
x_10TeV = df[df.columns[8]]
y_10TeV = df[df.columns[9]]

# sort according to the x column of each respective energy
idx_1GeV = np.argsort(x_1GeV)
x_1GeV = x_1GeV[idx_1GeV]
y_1GeV = y_1GeV[idx_1GeV]

idx_10GeV = np.argsort(x_10GeV)
x_10GeV = x_10GeV[idx_10GeV]
y_10GeV = y_10GeV[idx_10GeV]

idx_100GeV = np.argsort(x_100GeV)
x_100GeV = x_100GeV[idx_100GeV]
y_100GeV = y_100GeV[idx_100GeV]

idx_1TeV = np.argsort(x_1TeV)
x_1TeV = x_1TeV[idx_1TeV]
y_1TeV = y_1TeV[idx_1TeV]

idx_10TeV = np.argsort(x_10TeV)
x_10TeV = x_10TeV[idx_10TeV]
y_10TeV = y_10TeV[idx_10TeV]
#%%
plt.figure(figsize=(8,6))
plt.plot(x_1GeV, y_1GeV, label="1 GeV")
plt.plot(x_10GeV, y_10GeV, label="10 GeV")
plt.plot(x_100GeV, y_100GeV, label="100 GeV")
plt.plot(x_1TeV, y_1TeV, label="1 TeV")
plt.plot(x_10TeV, y_10TeV, label="10 TeV")
plt.legend(ncol=3, fontsize=12)
plt.xscale("log")
plt.yscale("log")
plt.xlim(1e-3,2e4)
plt.ylim(1e-28, 1e-23)
plt.xlabel(r"$E_\gamma$ [GeV]")
plt.ylabel(r"$E_\gamma d\sigma_{ICS}/dE_\gamma$ [cm$^2$]")
plt.savefig("ics-spectrum.pdf", dpi=300, bbox_inches="tight")
plt.show()
# %%

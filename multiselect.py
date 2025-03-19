import marimo

__generated_with = "0.11.21"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import matplotlib.colors as mcolors
    return mcolors, np, os, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Download data""")
    return


@app.cell
def _(os):
    import owncloud

    if not os.path.exists('data'):
        print('Creating directory for data')
        os.mkdir('data')
        os.mkdir('data/ses-715093703')
        os.mkdir('data/meta_data')

    if not os.path.exists('data/ses-715093703/units.parquet'):
        print('Downloading data')
        owncloud.Client.from_public_link('https://uni-bonn.sciebo.de/s/y9FtA26NOUxVeTt').get_file('/', 'data/ses-715093703/units.parquet')
    else:
        print('Session units data already downloaded')

    if not os.path.exists('data/meta_data/units.csv'):
        owncloud.Client.from_public_link('https://uni-bonn.sciebo.de/s/UUpOWgX8Chep9cZ').get_file('/', 'data/meta_data/units.csv')
    else:
        print('Units meta data already downloaded')
    return (owncloud,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Load session units data""")
    return


@app.cell
def _(os, pd):
    data_dir = 'data/ses-715093703'
    filename_units_ses = 'units.parquet'
    loadpath_ses = os.path.join(data_dir, filename_units_ses)
    units_ses = pd.read_parquet(loadpath_ses)
    return data_dir, filename_units_ses, loadpath_ses, units_ses


@app.cell
def _(units_ses):
    units_ses.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Select brain area

        Pick which part of the brain you want to investigate by clicking the dropdown menu below.
        """
    )
    return


@app.cell
def _(mo, units_ses):
    multiselect_structure = mo.ui.multiselect.from_series(units_ses['structure_acronym'])
    multiselect_structure
    return (multiselect_structure,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Plot average firing rate of neurons in selected areas""")
    return


@app.cell
def _(multiselect_structure, pd, plt, sns, units_ses):
    names_selected_structures = []

    for structure_acronym in multiselect_structure.value:
        nunits_structure = (units_ses['structure_acronym'] == structure_acronym).sum()
        names_selected_structures.extend([structure_acronym]*nunits_structure)

    for istructure, structure_name in enumerate(multiselect_structure.value):

        if istructure == 0:
            print(istructure, structure_name)
            firing_rate_structures = units_ses[units_ses.structure_acronym == structure_name]['firing_rate']
        else:
            print(istructure, structure_name)
            firing_rate_structures = pd.concat([firing_rate_structures, 
                                                units_ses[units_ses.structure_acronym == structure_name]['firing_rate']])

    firing_rate_structures = firing_rate_structures.to_frame()
    firing_rate_structures['structure_acronym'] = names_selected_structures

    sns.histplot(firing_rate_structures, x= 'firing_rate', hue = 'structure_acronym', kde=True)
    plt.title('Average firing rate across different areas')
    return (
        firing_rate_structures,
        istructure,
        names_selected_structures,
        nunits_structure,
        structure_acronym,
        structure_name,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Make raster plots of spikes in selected areas""")
    return


@app.cell
def _(mcolors, multiselect_structure, np, plt, units_ses):
    plt.figure(figsize = (6,6))

    colors = list(mcolors.TABLEAU_COLORS.keys())

    n_units_allstructs = 0
    for _istructure, _structure_name in enumerate(multiselect_structure.value):

        timestamps_structure = units_ses[units_ses.structure_acronym == _structure_name]['spike_times']

        unit_nrs_timestamps = []
        timestamps_structure_flat = []
        iunit = 0
        for unit_id, unit_timestamps in timestamps_structure.items():
            unit_nrs_timestamps.extend(np.zeros(len(unit_timestamps))+iunit)
            timestamps_structure_flat.extend(unit_timestamps)
            iunit += 1


        unit_nrs_timestamps = np.array(unit_nrs_timestamps)
        timestamps_structure_flat = np.array(timestamps_structure_flat)

        time_start_window = 999
        time_stop_window = 1000
        mask_window = np.logical_and(timestamps_structure_flat > time_start_window, 
                                     timestamps_structure_flat < time_stop_window)

        plt.plot((timestamps_structure_flat[mask_window]-time_start_window)*1E3, 
                 unit_nrs_timestamps[mask_window]+n_units_allstructs, 
                 '|', 
                 color = colors[_istructure], 
                 label =_structure_name)
        n_units_allstructs += unit_nrs_timestamps[-1]
    plt.title('Raster plot of spiking neurons in different areas')
    plt.xlabel('Time (milliseconds)')
    plt.ylabel('Neuron #')
    plt.legend(bbox_to_anchor = (1.1,0.9))
    return (
        colors,
        iunit,
        mask_window,
        n_units_allstructs,
        time_start_window,
        time_stop_window,
        timestamps_structure,
        timestamps_structure_flat,
        unit_id,
        unit_nrs_timestamps,
        unit_timestamps,
    )


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Explore spike data""")
    return


@app.cell
def _(mo, units_ses):
    mo.ui.data_explorer(units_ses['firing_rate'])
    return


@app.cell
def _():
    return


@app.cell
def _(data_dir, os, pd):
    _filename = 'running.parquet'
    _loadpath = os.path.join(data_dir, _filename)
    running_ses = pd.read_parquet(_loadpath)
    return (running_ses,)


@app.cell
def _(running_ses):
    running_ses
    return


@app.cell
def _():
    return


@app.cell
def _(data_dir, os, pd):
    _filename = 'stimuli.parquet'
    _loadpath = os.path.join(data_dir, _filename)
    stimuli_ses = pd.read_parquet(_loadpath)
    stimuli_ses
    return (stimuli_ses,)


@app.cell
def _():
    return


@app.cell
def _(mo, stimuli_ses):
    mo.ui.data_explorer(stimuli_ses['stimulus_name'])
    return


@app.cell
def _(stimuli_ses):
    stimuli_ses.columns
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

# Neuropixels Dataset Visualization with Marimo
This repository contains a ``marimo`` notebook with interactive visualizations of spike data in the Allen Visual Coding electrophysiological dataset.[<sup>1</sup>](#fn1) 

## Installation

Run the following commands to create and activate a conda environment with marimo and all other libraries used in the notebook installed:
```sh
conda env create -f environment.yml
conda activate marimo_env
```

## Quick start marimo

After you have activated the environment with the commands above or installed marimo in your own environment, you can start the ``marimo`` from the terminal. Below are some useful terminal commands when using and working with ``marimo``.

- Open up the notebook to visualize the Allen data with code included that can be edited:

```sh
marimo edit visualize_data.py
```

- Create a new ``marimo`` notebook (if the notebook already exist, it will simply be opened in the editable mode):

```sh
marimo edit your_notebook_name.py
```

- Deploy a ``marimo`` notebook as an app with the code hidden and uneditable:

```sh
marimo run your_notebook_name.py
```

- Convert existing ``jupyter`` notebook to a ``marimo`` notebook:

```sh
marimo convert your_notebook.ipynb -o your_notebook.py
```

- When you have opened a ``marimo`` notebook in editable mode, the code in the cells can be hidden with the shortcut ``ctrl + h``

<span id="fn1"><sup>1</sup>Siegle, J. H., Jia, X., Durand, S., Gale, S., Bennett, C., Graddis, N., ... & Koch, C. (2021). Survey of spiking in the mouse visual system reveals functional hierarchy. Nature, 592(7852), 86-92. doi: https://doi.org/10.1038/s41586-020-03171-x</span>

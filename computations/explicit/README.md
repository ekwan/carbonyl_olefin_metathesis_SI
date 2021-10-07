# Explicit Solvent Calculations

This directory contains key file for running the explicit solvent calculations in [presto](https://github.com/corinwagen/presto).

### Workflow

- Ensemble generation in PACKMOL of 2-methyl-2-butene + acetone + FeCl3 in 100 molecules of DCE
- Pre-equilibration and equilibration
- Dynamics constrained to a grid of C1-C2 and C3-O1 bond distances
- Analysis via WHAM2D to generate the free energy surface:
	- `python wham2d.py -C 1500 analyze 2 3 500 1 4 500 coords.csv "s*.chk"`
	- `wham-2d Px=0 1.45 3 152 Py=0 1.95 3 106 0.001 323 0 metadata.txt wham-output 0`
	- run Jupyter notebook to plot

### Contents

- __`xyz/`__ starting configuration
	- `solvated.xyz` PACKMOL output
- __`yaml/`__ configuration files
	- `prequil.yaml` for preequilibration
	- `equil_0000.yaml` sample `yaml` for equilibration
	- `wham.yaml` for generating constrained trajectory yaml files
	- `starting_configuration*.yaml` for constrained trajectories
- __`py/`__ Python scripts
	- `run.py` runs the trajectories (`python run.py NAME` where `NAME` is the name of trajectory)
	- `wham2d.py` performs setup and analysis
- __`analysis/`__ generating the free energy surface
	- `coords.csv` the bond distances
	- `metadata.txt` the constrained bond distances and force constants
	- `wham-output` output from WHAM2D program
	- `plot_pes.ipynb` plots the free energy surface


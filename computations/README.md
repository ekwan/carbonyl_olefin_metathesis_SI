# Computations

This folder contains the key computational files that were used in the paper.  Calculations were performed in Gaussian 16 and ORCA.

### Contents

- __`grids/`__ <br>
	These are structures with constrained C1-C2 and C3-O1 bond distances with single-point energies calculated at the coupled-cluster and DFT levels.  Python notebooks are provided to graph the results.
	- `model_system_gas/` <br>
		DLPNO-CCSD(T1)/aug-cc-pVTZ/NormalPNO and DFT/jul-cc-pVDZ single points in the gas phase for the model system.
	- `model_system_explicit/` <br>
		B3LYP-D3(BJ)/MIDI!/LANL2DZ(Fe,Cl) + GFN-xtb0 free energy surface (trajectories not included) for the model system.
	- `prenyl_gas_or_implicit` <br>
		Single points with various DFTs with jul-cc-pVDZ in the gas phase, implicit DCE, or implicit water for the prenyl substrate.
- __`prenyl/`__ <br>
	These are stationary points along the reaction coordinate for the prenyl substrate calculated at B3LYP-D3(BJ)/jul-cc-pVDZ in the gas phase, implicit DCE, and implicit water.<br>
- __`styrenyl/`__ <br>
	These are stationary points along the reaction coordinate for the styrenyl substrate calculated at B3LYP-D3(BJ)/jul-cc-pVDZ in the gas phase, implicit DCE, and implicit water.
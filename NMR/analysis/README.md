# KIE Analysis

This directory contains spreadsheets to calculate KIEs and error bars from the DEPT integrals and standard deviations.  The calculations are based on this equation:

<img src="../img/analysis1.png", height=150>

where F<sub>1</sub> is the conversion of the light isotope, R<sub>SM</sub> is the isotope ratio in the recovered starting material, and R<sub>0</sub> is the isotope ratio in the unreacted starting material.  In carbon KIEs, the conversion of both isotopes is essentially the same, so we assume F = F<sub>1</sub>.  The isotope ratios R are defined as heavy divided by light.

The spreadsheets here take the tables from the Jupyter Notebooks and compute the KIEs and estimate their uncertainties.  These estimates are consistently lower than the spread between the two independent KIE measurements are thus likely too optimistic.  The most plausible explanation is that sample-dependent errors are more serious than random errors.

### Contents

- `Prenyl KIE Spreadsheet.xlsx` KIEs and errors for prenyl substrate
- `Styrenyl KIE Spreadsheet.xlsx` KIEs and errors for styrenyl substrate
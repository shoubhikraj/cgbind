[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3550545.svg)](https://doi.org/10.5281/zenodo.3550545) [![Build Status](https://travis-ci.org/duartegroup/cgbind.svg?branch=master)](https://travis-ci.org/duartegroup/cgbind)
![alt text](cgbind/common/llogo.png)
### *C*a*g*e*Bind*ing: A tool to for automated metallocage binding affinity calculations
***

**cgbind** automates the process of generating M2L4 metallocage structures
from just SMILES strings of the corresponding linker (_L_). Binding affinity
calculations may also be evaluated via input of both linker and substrate
SMILES, provided an installation of ORCA or XTB is available. A graphical
user interface (GUI) in _alpha_ is currently available at
[cgbind.com](http://cgbind.com).

***

## Requirements
0. Python v. 3.7
1. [rdkit](https://github.com/rdkit/rdkit)
2. [autode](https://github.com/duartegroup/autodE) latest
3. [ORCA](https://sites.google.com/site/orcainputlibrary/home) v. 4.1 (optional)
4. [XTB](https://github.com/grimme-lab/xtb) v. 6.2 (optional)

***

## Installation

For installation instructions see the [docs](https://duartegroup.github.io/cgbind/install.html).
If the requirements are already satisfied
```
python setup.py install
```

***

## Usage

**cgbind** constructs cages from SMILES [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
strings, which can be generated directly from ChemDraw.

![alt text](cgbind/common/SMILES_generation.png)


To load as a module:
```python
import cgbind
```

See _examples/_ and the [docs](https://duartegroup.github.io/cgbind/examples.html)
for how to use **cgbind**.

from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from cgbind.log import logger
from cgbind.input_output import print_output
from cgbind.input_output import xyzs2xyzfile
from cgbind.confomers import extract_xyzs_from_rdkit_mol_object
from cgbind.geom import calc_com
from autode.bond_lengths import get_bond_list_from_rdkit_bonds
from autode.bond_lengths import get_xyz_bond_list
from cgbind import calculations


class Molecule:

    def print_xyzfile(self):
        xyzs2xyzfile(xyzs=self.xyzs, basename=self.name)

    def set_com(self):
        self.com = calc_com(self.xyzs)

    def init_smiles(self, smiles):
        """
        Initialise a Molecule object from a SMILES sting using RDKit
        :param smiles: (str) SMILES string
        :return:
        """
        logger.info('Initialising a Molecule from a SMILES strings ')
        try:
            self.mol_obj = Chem.MolFromSmiles(smiles)
            self.mol_obj = Chem.AddHs(self.mol_obj)
            self.charge = Chem.GetFormalCharge(self.mol_obj)
            self.n_rot_bonds = rdMolDescriptors.CalcNumRotatableBonds(self.mol_obj)
            self.n_h_donors = rdMolDescriptors.CalcNumHBD(self.mol_obj)
            self.n_h_acceptors = rdMolDescriptors.CalcNumHBA(self.mol_obj)

        except:
            logger.error('RDKit failed to generate mol objects')
            return

        print_output('Conformer generation for', self.name, 'Running')
        self.conf_ids = list(AllChem.EmbedMultipleConfs(self.mol_obj, numConfs=self.n_confs, params=AllChem.ETKDG()))
        self.volume = AllChem.ComputeMolVolume(self.mol_obj)
        self.bonds = get_bond_list_from_rdkit_bonds(rdkit_bonds_obj=self.mol_obj.GetBonds())
        print_output('', '', 'Done')

        self.n_atoms = self.mol_obj.GetNumAtoms()
        self.conf_xyzs = extract_xyzs_from_rdkit_mol_object(mol_obj=self.mol_obj, conf_ids=self.conf_ids)
        self.xyzs = self.conf_xyzs[0]

    def singlepoint(self, method, keywords, n_cores=1, max_core_mb=1000):
        return calculations.singlepoint(self, method, keywords, n_cores, max_core_mb)

    def optimise(self, method, keywords, n_cores=1, max_core_mb=1000):
        return calculations.optimise(self, method, keywords, n_cores, max_core_mb)

    def __init__(self, smiles=None, name='molecule', charge=0, mult=1, n_confs=1, xyzs=None, solvent=None):
        logger.info('Initialising a Molecule object for {}'.format(name))

        self.name = name
        self.smiles = smiles
        self.xyzs = xyzs
        self.solvent = solvent
        self.n_confs = n_confs

        self.charge = int(charge)
        self.mult = mult

        self.energy = None
        self.mol_obj = None
        self.n_atoms = None
        self.com = None

        self.n_rot_bonds = None
        self.n_h_donors = None
        self.n_h_acceptors = None
        self.volume = None          # Å^3
        self.bonds = None

        self.conf_ids = None
        self.conf_filenames = None
        self.conf_xyzs = None

        if smiles:
            self.init_smiles(smiles)

        if xyzs:
            self.n_atoms = len(xyzs)
            self.bonds = get_xyz_bond_list(xyzs=self.xyzs)

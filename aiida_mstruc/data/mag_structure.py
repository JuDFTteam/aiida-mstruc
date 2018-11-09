# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c), Forschungszentrum Jülich GmbH, IAS-1/PGI-1, Germany.         #
#                All rights reserved.                                         #
# This file is part of the aiida-mstruc package.                              #
#                                                                             #
# The code is hosted on GitHub at https://github.com/JuDFTteam/aiida-mstruc   #
# For further information on the license, see the LICENSE.txt file            #
###############################################################################
"""
This module contains the magnetic crystal structure data..
"""

# Ideas:
# TODO: look at ase and pymatgen magnetic structure
# TODO: Think about how fleur and other codes use magnetic structures
# Each Site can have its own magnetic and orbital momment pointing in some direction
# These properties can also be set for a Kind
# Also for the whole structure...

# For performance, if you want this also to be able to represent an
# array of 1000x1000x1000 spins, you might want to think about writting this to 
# disk and only keep certain 'global' information in the database
# or make 'spin fields' and extra datatype.

import os
import re

from aiida.orm import DataFactory
from aiida.common.exceptions import InputValidationError, ValidationError
from aiida.work.workfunctions import workfunction as wf
from aiida.orm.structure import StructureData, Kind, Site

bohr_a = 0.52917721092#A, todo: get from somewhereA
#StructureData = DataFactory('structure')

class MagneticstructureData(StructureData):
    """
    """

    
    ###########
    # Functions, properties from StructureData to be overwrite

    def get_pymatgen(self,**kwargs):
        """
        """
        pass

    def get_pymatgen_structure(self,**kwargs):
        """
        """
        pass
 
    
    def _get_object_pymatgen_molecule(self,**kwargs):
        """
        """
        pass
    
    
    def _get_object_pymatgen_structure(self):
        """
        """
        pass

    def _get_object_pymatgen(self):
        """
        """
        pass

    def _get_object_ase(self):
        """
        """
        pass

    def _get_cif(self):
        """
        """
        pass
    
    #################


    @property
    def total_magnetic_moment(self):
        """
        """
        return self.get_attr('total_magnetic_moment', 0.0)

    @property
    def total_orbital_moment(self):
        """
        """
        return self.get_attr('total_orbital_moment', 0.0)

    @property
    def quantization_axes(self):
        """
        global qunatization axes, theta, phi
        """
        return self.get_attr('quantization_axes', (0.0, 0.0))

    def _validate(self):
        """

        """
        #from aiida.common.exceptions import ValidationError

        super(StructureData, self)._validate()

        
    def set_spin_spiral(self, **kwargs):
        """
        """
        pass

    def set_random_mag(self, **kwargs):
        """
        """
        pass

    def set_ferro_mag(self, **kwargs):
        """
        """
        pass        
    
    def get_structuredata_nwf(magstructure):
        """
        """
        
        pass

    @staticmethod
    @wf
    def get_structuredata(magstructure):
        """
        This routine return an AiiDA Structure Data type without magnetic momments
        This is a workfunction and therefore keeps the provenance.

        :return: StructureData node
        """
        return magstructure.get_structuredata_nwf(magstructure)

        
    def get_some_visualisation_file(self):
        """
        for vesta, blender, Pofray or whatever
        """
        pass
        
class MagSite(Site):
    pass

class MagKind(Kind):
    pass
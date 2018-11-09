# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c), Forschungszentrum Jülich GmbH, IAS-1/PGI-1, Germany.         #
#                All rights reserved.                                         #
# This file is part of the AiiDA-mstruc package.                              #
#                                                                             #
# The code is hosted on GitHub at https://github.com/JuDFTteam/aiida-mstruc   #
# For further information on the license, see the LICENSE.txt file            #
###############################################################################

import pytest

@pytest.mark.usefixtures("aiida_env")
class TestAiida_mstruc_entrypoints:
    """
    tests all the entry points of aiida-mstruc. Therefore if it is 
    reconized by AiiDA.
    """
    
    
    # Data
    
    def test_magneticstructuredata_entry_point(aiida_env):
        from aiida.orm import DataFactory
        from aiida_mstruc.data.mag_structure import MagneticstructureData
    
        mstruc = DataFactory('mstruc.mag_structure')
        assert mstruc == MagneticstructureData


# Module to run tests on initializing AbsSurvey

# TEST_UNICODE_LITERALS

import numpy as np
import os, pdb
import pytest
from astropy import units as u
from astropy.coordinates import SkyCoord

from pyigm.abssys.igmsys import IGMSystem
from pyigm.abssys.igmsurvey import GenericIGMSurvey

'''
def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'files')
    return os.path.join(data_dir, filename)
'''

def test_generic():
    # Start
    gensurvey = GenericIGMSurvey()

    # Systems
    coord = SkyCoord(ra=123.1143*u.deg, dec=-12.4321*u.deg)
    gensys1 = IGMSystem('Generic', coord, 1.244, [-300,300.]*u.km/u.s, NHI=16.)
    gensys1.name = 'Sys1'
    #
    coord2 = SkyCoord(ra=223.1143*u.deg, dec=42.4321*u.deg)
    gensys2 = IGMSystem('Generic', coord2, 1.744, [-300,300.]*u.km/u.s, NHI=17.)
    gensys2.name = 'Sys2'
    # Combine
    gensurvey.add_abs_sys(gensys1)
    gensurvey.add_abs_sys(gensys2)
    assert gensurvey.nsys == 2

    # Attribute
    aNHI = gensurvey.NHI
    np.testing.assert_allclose(aNHI, np.array([16.,17.]))

import pytest
import jpcm
import matplotlib.pyplot as plt
import matplotlib.cm.listedcolormap as LCM

def test_jpcm_load():
    """
    Test that the jpcm package can be loaded.
    """
    assert jpcm

def test_jpcm_get():
    """
    Test that the jpcm package can be loaded.
    """
    assert isinstance(jpcm.get("def"),LCM)

def test_jpcm_register():
    """
    Test that the jpcm package can be loaded.
    """
    assert jpcm.register()

import pytest
import jpcm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as LCM


def test_jpcm_load():
    """
    Test that the jpcm package can be loaded.
    """
    assert jpcm


def test_jpcm_get():
    """
    Test that the jpcm package can be loaded.
    """
    assert isinstance(jpcm.get("def"), LCM)


def test_jpcm_register():
    """
    Test that the jpcm package can be loaded.
    """
    jpcm.register()

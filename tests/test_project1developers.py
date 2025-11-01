import pytest
from project1developers import *

def test_read_devs():
    # Implement this!
    pass

def test_compute_similarity():
    # Implement this!
    pass

def test_preprocess():
    # useampia kuin kaksi osaisia nimiä (biggus dickus jr -> biggus, dickus jr)
    # Yksiosainen nimi
    # aksenttimerkkejä
    #
    dev = [" Biggus. Dickus!", "biggus.dickus@monty.com"]
    name, first, last, i_first, i_last, email, prefix = preprocess(dev)
    assert name == "biggus dickus"
    assert first == "biggus"
    assert last == "dickus"
    assert i_first == "b"
    assert i_last == "d"
    assert email == "biggus.dickus@monty.com"
    assert prefix == "biggus.dickus"


def test_save_similarity_data():
    # Implement this!
    pass

def filter_and_save():
    # Implement this!
    pass

 
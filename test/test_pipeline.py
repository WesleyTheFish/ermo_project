import pipeline as pl
import pytest

@pytest.mark.parametrize(
    "input_value,expected_output",
    [
        (0.1, 0),
        (-0.1, 0),
        (0.3, 0.3),
        (-0.3, -0.3),
        (0, 0),
        (0.2, 0),
        (-0.2, 0),
        (1, 1),
        (-1, -1),
    ]
)
def test_deadzone_1(input_value, expected_output):
    dz = pl.make_deadzone_transform(0, 0.2)
    assert dz(input_value) == expected_output


@pytest.mark.parametrize(
    "width,input_value,expected_output",
    [
        (1, 1, 1),
        (1, 0, 0),
        (1, -1, -1),
    ]
)
def test_window_filter_1(width, input_value, expected_output):
    wf = pl.make_window_filter_transform(width)
    assert wf(input_value) == expected_output


def test_window_filter_2():
    width = 3
    wf = pl.make_window_filter_transform(width)
    assert wf(1) == 1
    assert wf(2) == (1 + 2) / 2
    assert wf(3) == (1 + 2 + 3) / 3
    assert wf(4) == (2 + 3 + 4) / 3
    assert wf(5) == (3 + 4 + 5) / 3
    assert wf(6) == (4 + 5 + 6) / 3
    assert wf(7) == (5 + 6 + 7) / 3
    
def test_window_filter_2():
    width = 3
    wf = pl.make_window_filter_transform(width)
    assert wf(1) == 1
    assert wf(2) == (1 + 2) / 2
    assert wf(3) == (1 + 2 + 3) / 3
    assert wf(4) == (2 + 3 + 4) / 3
    assert wf(5) == (3 + 4 + 5) / 3
    assert wf(6) == (4 + 5 + 6) / 3
    assert wf(7) == (5 + 6 + 7) / 3

def test_window_filter_3():
    width = 5
    wf = pl.make_window_filter_transform(width)
    assert wf(1) == 1.
    assert wf(3) == 2
    assert wf(5) == 3
    assert wf(7) == 4
    assert wf(9) == 5
    assert wf(11) == 7

@pytest.mark.skip(reason="Not implemented yet.")
def test_deadzone_2():
    dz = pl.make_deadzone_transform(0, 0.5)
    assert dz(0.1) == 0
    assert dz(-0.1) == 0
    assert dz(0.5) == 0
    assert dz(0.75) == 0.5
    assert dz(1) == 1
    assert dz(-0.5) == 0
    assert dz(-0.75) == -0.5
    assert dz(-1) == -1

def test_class_window():

    """Test the WindowTransform class same as the function based window filter, slightly slower."""
    width = 3
    wxf = pl.WindowTransform(width)  # class based window transform
    assert wxf(1) == 1
    assert wxf(2) == (1 + 2) / 2
    assert wxf(3) == (1 + 2 + 3) / 3
    assert wxf(4) == (2 + 3 + 4) / 3
    assert wxf(5) == (3 + 4 + 5) / 3
    assert wxf(6) == (4 + 5 + 6) / 3
    assert wxf(7) == (5 + 6 + 7) / 3
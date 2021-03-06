from polynomial import Nomial, PolynomialFit, x, y
import numpy.linalg as la
from sympy import Lambda, symbols
import numpy as np
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
np.set_printoptions(precision=4, linewidth=120, suppress=True)

def stable_fit(pts):
    return PolynomialFit(full_rank_tol=1e-9).stable_fit(pts).terms.terms

def test_four_by_three():
    pts = [ \
        (-1, 0), \
        (1, 0), \
        (-3, 0), \
        (-5, 0), \
        (-1, -2), \
        (1, -2), \
        (1, -2), \
        (-3, -2), \
        (-5, -2), \
        (-1, 2), \
        (1, 2), \
        (-3, 2), \
        (-5, 2) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), x**2)), \
        Nomial(Lambda((x, y), y**2)), \
        Nomial(Lambda((x, y), x**2*y)), \
        Nomial(Lambda((x, y), x*y**2)), \
        Nomial(Lambda((x, y), x**3)), \
    ]

    assert stable_fit(pts) == expected

def test_six_points_with_diagonal():
    pts = [ \
        (-1, 0.0330314), \
        (0.907926, -2.64e-14), \
        (-1.13441, 3.05716), \
        (-0.87524, -2.99221), \
        (0.907926, 3.02642), \
        (0.907926, -3.02642) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), y**2)) \
    ]

    print(PolynomialFit(full_rank_tol=1e-9).stable_fit(pts).downwind_weight)
    assert stable_fit(pts) == expected

def test_nine_points_with_diagonal():
    pts = [ \
        (-1, 1.36424e-16), \
        (1, 5.80712e-14), \
        (1, 3.33333), \
        (1, -3.33333), \
        (-1, 3.33333), \
        (-1, -3.33333), \
        (-3.12554, 3.35946), \
        (-3.02091, 0.0282014), \
        (-2.91995, -3.30361) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), x**2)), \
        Nomial(Lambda((x, y), y**2)), \
        Nomial(Lambda((x, y), x**2*y)), \
        Nomial(Lambda((x, y), x*y**2)) \
    ]

    assert stable_fit(pts) == expected
    

def test_three_downwind_two_upwind():
    pts = [ \
        (-0.318132398309, 1), \
        (1.62494112442, -0.0619155571362), \
        (-0.519892365614, 6.24311965797), \
        (1.97959459194, 5.68059436497), \
        (1.6715638405, -5.58574321789), \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), y**2)), \
    ]

    assert stable_fit(pts) == expected

def test_three_downwind_two_upwind2():
    pts = [ \
        (-0.375692991674, 1), \
        (2.04670349731, 0.151415600652), \
        (2.68167823645, -5.90562193016), \
        (1.48171410264, 6.45067028153), \
        (-1.05780329301, 6.2993205546) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), y**2)), \
    ]

    assert stable_fit(pts) == expected

def test_eight_points_with_diagonal():
    pts = [ \
        (-1, 0.0425922049484), \
        (1.05781693914, -0.0369040044104), \
        (-5.10831948925, 0.22706220493), \
        (-3.05606764231, 0.133444521133), \
        (-5.17064352149, 1.10939830377), \
        (-3.1023861129, 1.10939830377), \
        (-1.0341287043, 1.10939830377), \
        (1.0341287043, 1.10939830377) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), x**2)), \
        Nomial(Lambda((x, y), x**2*y)), \
        Nomial(Lambda((x, y), x**3)), \
    ]

    assert stable_fit(pts) == expected

def test_eight_points_with_diagonal2():
    pts = [ \
        (-1, -0.0669388588762), \
        (0.833644437615, 0.0794066407836), \
        (-4.75714056459, -0.217550549489), \
        (-2.8731750957, -0.165967824541), \
        (-4.74883733854, 0.906972333924), \
        (-2.84930240312, 0.906972333924), \
        (-0.949767467708, 0.906972333924), \
        (0.949767467708, 0.906972333924) \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), x**2)), \
        Nomial(Lambda((x, y), x**2*y)), \
        Nomial(Lambda((x, y), x**3)), \
    ]

    assert stable_fit(pts) == expected

def test_two_by_three_very_small_diagonal():
    pts = [ \
        (-1, -0.000810356386742), \
        (1.00145581289, -8.74386005651e-14), \
        (-0.993588838779, 3.33540741754), \
        (-1.00145581289, -1.66909302149), \
        (1.00145581289, -1.66909302149), \
        (1.00145581289, 3.33818604298), \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), y**2)), \
        Nomial(Lambda((x, y), x*y**2)), \
    ]

    assert stable_fit(pts) == expected

def test_two_by_three_diagonal():
    pts = [ \
        (-1, 0.0149698735917), \
        (1.02740059135, -2.24259694664e-14), \
        (-0.907001583868, -3.3816285968), \
        (-1.0162149057, 3.41915929803), \
        (1.02740059135, -3.42466863784), \
        (1.02740059135, 3.42466863784), \
    ]

    expected = [ \
        Nomial(Lambda((x, y), 1.0)), \
        Nomial(Lambda((x, y), x)), \
        Nomial(Lambda((x, y), y)), \
        Nomial(Lambda((x, y), x*y)), \
        Nomial(Lambda((x, y), y**2)), \
        Nomial(Lambda((x, y), x*y**2)), \
    ]

    assert stable_fit(pts) == expected


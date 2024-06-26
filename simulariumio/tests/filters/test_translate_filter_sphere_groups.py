#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from simulariumio import MetaData, UnitData, JsonWriter, DisplayData
from simulariumio.physicell import PhysicellConverter, PhysicellData
from simulariumio.filters import TranslateFilter
from simulariumio.constants import DISPLAY_TYPE


@pytest.mark.parametrize(
    "trajectory, _filter, expected_bundleData_t0",
    [
        # sphere groups for owner cells and subcells
        (
            PhysicellData(
                meta_data=MetaData(
                    box_size=np.array([960.0, 640.0, 300.0]),
                    scale_factor=0.01,
                ),
                timestep=36.0,
                path_to_output_dir="simulariumio/tests/data/physicell/subcell_output/",
                display_data={
                    0: DisplayData(
                        name="Substrate",
                        display_type=DISPLAY_TYPE.SPHERE,
                        color="#d0c5c8",
                    ),
                },
                phase_names={0: {18: "fixed"}},
                max_owner_cells=10000,
                owner_cell_display_name="Stem cell",
                time_units=UnitData("min"),
            ),
            TranslateFilter(
                default_translation=0.01 * (-0.5 * np.array([960.0, 640.0, 300.0])),
            ),
            [
                1000,
                35,
                0,
                -0.4016802,
                -0.4266752,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                36,
                0,
                -0.0983478,
                -0.4266752,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                37,
                0,
                0.2049846,
                -0.4266752,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                38,
                0,
                0.508317,
                -0.4266752,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                39,
                0,
                -0.5533464,
                -0.1558427,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                40,
                0,
                -0.250014,
                -0.1558427,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                41,
                0,
                0.0533184,
                -0.1558427,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                42,
                0,
                0.3566508,
                -0.1558427,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                43,
                0,
                -0.4016802,
                0.1041565,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                44,
                0,
                -0.0983478,
                0.1041565,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                45,
                0,
                0.2049846,
                0.1041565,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                46,
                0,
                0.508317,
                0.1041565,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                47,
                0,
                -0.5533464,
                0.3641557,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                48,
                0,
                -0.250014,
                0.3641557,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                49,
                0,
                0.0533184,
                0.3641557,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                50,
                0,
                0.3566508,
                0.3641557,
                -1.339,
                0,
                0,
                0,
                0.18837494593627718,
                0,
                1000,
                10008,
                1,
                -0.04319645,
                -0.44932665,
                -0.98309091,
                0,
                0,
                0,
                1.0,
                44,
                -0.510149945454546,
                -0.1290147545454552,
                -0.09490909090909089,
                0.18697981,
                -0.20681754545454645,
                -0.1290147545454552,
                -0.09490909090909089,
                0.18697981,
                0.09651485454545394,
                -0.1290147545454552,
                -0.09490909090909089,
                0.18697981,
                0.39984725454545433,
                -0.1290147545454552,
                -0.09490909090909089,
                0.18697981,
                -0.35848374545454575,
                0.14181774545454484,
                -0.09490909090909089,
                0.18697981,
                -0.05515134545454625,
                0.14181774545454484,
                -0.09490909090909089,
                0.18697981,
                0.24818105454545414,
                0.14181774545454484,
                -0.09490909090909089,
                0.18697981,
                -0.35848374545454575,
                0.022651445454545005,
                0.16609090909090918,
                0.18697981,
                -0.05515134545454625,
                0.022651445454545005,
                0.16609090909090918,
                0.18697981,
                0.24818105454545414,
                0.022651445454545005,
                0.16609090909090918,
                0.18697981,
                0.5515134545454536,
                0.022651445454545005,
                0.16609090909090918,
                0.18697981,
                1000,
                10014,
                2,
                -0.02581179,
                0.17198238,
                -0.95317391,
                0,
                0,
                0,
                1.0,
                92,
                -0.5275346086956532,
                -0.21949207826086958,
                -0.1248260869565217,
                0.18697981,
                -0.22420220869565366,
                -0.21949207826086958,
                -0.1248260869565217,
                0.18697981,
                0.07913019130434673,
                -0.21949207826086958,
                -0.1248260869565217,
                0.18697981,
                0.3824625913043471,
                -0.21949207826086958,
                -0.1248260869565217,
                0.18697981,
                -0.37586840869565297,
                0.04050712173913018,
                -0.1248260869565217,
                0.18697981,
                -0.07253600869565346,
                0.04050712173913018,
                -0.1248260869565217,
                0.18697981,
                0.23079639130434693,
                0.04050712173913018,
                -0.1248260869565217,
                0.18697981,
                0.5341287913043464,
                0.04050712173913018,
                -0.1248260869565217,
                0.18697981,
                -0.5275346086956532,
                0.3005063217391304,
                -0.1248260869565217,
                0.18697981,
                -0.22420220869565366,
                0.3005063217391304,
                -0.1248260869565217,
                0.18697981,
                0.07913019130434673,
                0.3005063217391304,
                -0.1248260869565217,
                0.18697981,
                0.3824625913043471,
                0.3005063217391304,
                -0.1248260869565217,
                0.18697981,
                -0.22420220869565366,
                -0.3278250782608696,
                0.13617391304347837,
                0.18697981,
                0.07913019130434673,
                -0.3278250782608696,
                0.13617391304347837,
                0.18697981,
                0.3824625913043471,
                -0.3278250782608696,
                0.13617391304347837,
                0.18697981,
                -0.37586840869565297,
                -0.06782587826086983,
                0.13617391304347837,
                0.18697981,
                -0.07253600869565346,
                -0.06782587826086983,
                0.13617391304347837,
                0.18697981,
                0.23079639130434693,
                -0.06782587826086983,
                0.13617391304347837,
                0.18697981,
                0.5341287913043464,
                -0.06782587826086983,
                0.13617391304347837,
                0.18697981,
                -0.5275346086956532,
                0.19217332173913038,
                0.13617391304347837,
                0.18697981,
                -0.22420220869565366,
                0.19217332173913038,
                0.13617391304347837,
                0.18697981,
                0.07913019130434673,
                0.19217332173913038,
                0.13617391304347837,
                0.18697981,
                0.3824625913043471,
                0.19217332173913038,
                0.13617391304347837,
                0.18697981,
                1000,
                10025,
                3,
                -0.5533464,
                -0.1558427,
                -0.817,
                0,
                0,
                0,
                1.0,
                4,
                0,
                0,
                0,
                0.18697981,
                1000,
                10002,
                4,
                -4.8,
                -3.2,
                -1.5,
                0,
                0,
                0,
                1.0,
                4,
                0,
                0,
                0,
                0,
            ],
        ),
    ],
)
def test_translate_filter(trajectory, _filter, expected_bundleData_t0):
    converter = PhysicellConverter(trajectory)
    filtered_data = converter.filter_data([_filter])
    buffer_data = JsonWriter.format_trajectory_data(filtered_data)
    assert False not in np.isclose(
        np.array(buffer_data["spatialData"]["bundleData"][0]["data"]),
        np.array(expected_bundleData_t0),
    )

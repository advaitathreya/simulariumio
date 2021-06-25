#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simulariumio import FileConverter
from simulariumio.filters import EveryNthAgentFilter


@pytest.mark.parametrize(
    "input_path, _filter, expected_data",
    [
        (
            "simulariumio/tests/data/cytosim/aster_pull3D_couples_actin_solid_3_frames"
            "/aster_pull3D_couples_actin_solid_3_frames.json",
            EveryNthAgentFilter(
                n_per_type={
                    "microtubule": 3,
                    "actin": 1,
                    "vesicle": 2,
                    "dynein": 2,
                    "motor complex": 1,
                },
                default_n=2,
            ),
            {
                "trajectoryInfo": {
                    "version": 2,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 0.05,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "µm",
                    },
                    "size": {"x": 200.0, "y": 200.0, "z": 200.0},
                    "cameraDefault": {
                        "position": {"x": 0, "y": 0, "z": 120},
                        "lookAtPosition": {"x": 0, "y": 0, "z": 0},
                        "upVector": {"x": 0, "y": 1, "z": 0},
                        "fovDegrees": 75.0,
                    },
                    "typeMapping": {
                        "0": {"name": "microtubule"},
                        "1": {"name": "actin"},
                        "2": {"name": "aster"},
                        "3": {"name": "vesicle"},
                        "4": {"name": "kinesin"},
                        "5": {"name": "dynein"},
                        "6": {"name": "motor complex"},
                    },
                },
                "spatialData": {
                    "version": 1,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                36.93,
                                36.8,
                                16.78,
                                30.55,
                                43.87,
                                19.84,
                                24.169999999999998,
                                50.93,
                                22.900000000000002,
                                17.78,
                                57.99999999999999,
                                25.95,
                                11.4,
                                65.07,
                                29.01,
                                1001.0,
                                13.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                12.0,
                                46.08,
                                -104.85,
                                -2.1,
                                45.67,
                                -104.54,
                                -1.9,
                                45.26,
                                -104.23,
                                -1.7000000000000002,
                                44.85,
                                -103.91999999999999,
                                -1.5,
                                1001.0,
                                14.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                9.0,
                                53.690000000000005,
                                79.28,
                                -3.09,
                                53.6,
                                78.83,
                                -3.39,
                                53.5,
                                78.39,
                                -3.6999999999999997,
                                1000.0,
                                4.0,
                                2.0,
                                36.93,
                                36.8,
                                16.78,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                5.0,
                                3.0,
                                78.60000000000001,
                                -28.799999999999997,
                                18.04,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                7.0,
                                4.0,
                                20.61,
                                -39.910000000000004,
                                89.35,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                9.0,
                                4.0,
                                37.56,
                                -80.46,
                                -46.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                101.0,
                                5.0,
                                -74.11999999999999,
                                30.31,
                                -59.89,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                103.0,
                                5.0,
                                -19.37,
                                -9.379999999999999,
                                97.66,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                10.0,
                                6.0,
                                32.629999999999995,
                                38.550000000000004,
                                57.120000000000005,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                11.0,
                                6.0,
                                4.42,
                                20.200000000000003,
                                -62.88,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                12.0,
                                6.0,
                                -73.8,
                                -25.2,
                                -43.89,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.05,
                            "data": [
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                18.0,
                                44.55,
                                33.97,
                                8.86,
                                36.63,
                                38.269999999999996,
                                4.51,
                                28.96,
                                43.28,
                                0.5,
                                21.83,
                                49.61,
                                -2.52,
                                16.0,
                                57.66,
                                -3.58,
                                12.85,
                                66.92,
                                -1.47,
                                1001.0,
                                13.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                51.480000000000004,
                                -85.75,
                                5.3100000000000005,
                                51.0,
                                -85.78,
                                5.59,
                                50.529999999999994,
                                -85.82,
                                5.87,
                                50.06,
                                -85.86,
                                6.15,
                                49.58,
                                -85.9,
                                6.419999999999999,
                                1001.0,
                                14.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                9.0,
                                47.0,
                                81.69999999999999,
                                -9.139999999999999,
                                47.099999999999994,
                                81.22,
                                -9.39,
                                47.21,
                                80.74,
                                -9.64,
                                1000.0,
                                4.0,
                                2.0,
                                44.86,
                                34.239999999999995,
                                9.36,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                5.0,
                                3.0,
                                77.18,
                                -36.65,
                                21.9,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                7.0,
                                4.0,
                                20.61,
                                -39.910000000000004,
                                89.35,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                9.0,
                                4.0,
                                37.56,
                                -80.46,
                                -46.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                101.0,
                                5.0,
                                -74.11999999999999,
                                30.31,
                                -59.89,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                103.0,
                                5.0,
                                -19.37,
                                -9.379999999999999,
                                97.66,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                10.0,
                                6.0,
                                33.96,
                                13.309999999999999,
                                50.29,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                11.0,
                                6.0,
                                19.189999999999998,
                                17.69,
                                -76.94,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                12.0,
                                6.0,
                                -72.52,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 0.1,
                            "data": [
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                44.55,
                                33.97,
                                8.86,
                                36.63,
                                38.269999999999996,
                                4.51,
                                28.96,
                                43.28,
                                0.5,
                                21.83,
                                49.61,
                                -2.52,
                                16.0,
                                57.66,
                                -3.58,
                                1001.0,
                                13.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                51.480000000000004,
                                -85.75,
                                5.3100000000000005,
                                51.0,
                                -85.78,
                                5.59,
                                1001.0,
                                14.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                12.0,
                                47.0,
                                81.69999999999999,
                                -9.139999999999999,
                                47.099999999999994,
                                81.22,
                                -9.39,
                                47.21,
                                80.74,
                                -9.64,
                                47.31,
                                80.25999999999999,
                                -9.89,
                                1000.0,
                                4.0,
                                2.0,
                                44.86,
                                34.239999999999995,
                                9.36,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                5.0,
                                3.0,
                                77.18,
                                -36.65,
                                21.9,
                                0.0,
                                0.0,
                                0.0,
                                10.0,
                                0.0,
                                1000.0,
                                7.0,
                                4.0,
                                20.61,
                                -39.910000000000004,
                                89.35,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                9.0,
                                4.0,
                                37.56,
                                -80.46,
                                -46.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                101.0,
                                5.0,
                                -74.11999999999999,
                                30.31,
                                -59.89,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                103.0,
                                5.0,
                                -19.37,
                                -9.379999999999999,
                                97.66,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                10.0,
                                6.0,
                                33.96,
                                13.309999999999999,
                                50.29,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                11.0,
                                6.0,
                                19.189999999999998,
                                17.69,
                                -76.94,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                12.0,
                                6.0,
                                -72.52,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {"version": 1, "data": []},
            },
        ),
    ],
)
def test_every_nth_agent_filter(input_path, _filter, expected_data):
    converter = FileConverter(input_path)
    filtered_data = converter.filter_data([_filter])
    buffer_data = converter._read_trajectory_data(filtered_data)
    assert expected_data == buffer_data
    assert converter._check_agent_ids_are_unique_per_frame(buffer_data)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simulariumio import FileConverter
from simulariumio.filters import ReorderAgentsFilter


@pytest.mark.parametrize(
    "input_path, _filter, expected_data",
    [
        (
            "simulariumio/tests/data/cytosim/aster_pull3D_couples_actin_solid_3_frames"
            "/aster_pull3D_couples_actin_solid_3_frames_small.json",
            ReorderAgentsFilter(
                type_id_mapping={
                    7: 1,
                    1: 2,
                }
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
                        "1": {"name": "motor complex"},
                        "2": {"name": "microtubule"},
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
                                2.0,
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
                                1000.0,
                                12.0,
                                1.0,
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
                                2.0,
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
                                1000.0,
                                12.0,
                                1.0,
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
                                2.0,
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
                                1000.0,
                                12.0,
                                1.0,
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
                "plotData": {
                    "version": 1,
                    "data": [],
                },
            },
        ),
    ],
)
def test_reorder_agents_filter(input_path, _filter, expected_data):
    converter = FileConverter(input_path)
    filtered_data = converter.filter_data([_filter])
    buffer_data = converter._read_trajectory_data(filtered_data)
    assert expected_data == buffer_data
    assert converter._check_agent_ids_are_unique_per_frame(buffer_data)

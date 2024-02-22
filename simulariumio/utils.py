import numpy as np
from typing import Dict, Any

from .data_objects import DisplayData, AgentData


def unpack_position_vector(
    vector_dict: Dict[str, str], defaults: np.ndarray
) -> np.ndarray:
    """
    Takes a vector dict describing x, y, z coordinates and default values
    and returns a numpy array representing the 3 coordintes

    Parameters
    ----------
    vector_dict : Dict[str, str]
        Dict representing values of X, Y, and/or Z coordinates
        Keys should be {'x','y','z'}
    defaults: np.ndarray
        Numpy array representing default XYZ coordinates. For any coordinates
        not provided in vector_dict, these default values will be used in the
        result vector
    """
    # if no vector information was given, go with the defaults
    if vector_dict is None:
        return defaults

    # use all positions given, but use defaults if any are missing
    return np.array(
        [
            float(vector_dict.get("x", defaults[0])),
            float(vector_dict.get("y", defaults[1])),
            float(vector_dict.get("z", defaults[2])),
        ]
    )


def unpack_display_data(
    data_dict: Dict[str, Any]
) -> Dict[str, DisplayData]:
    """
    Create dict [str, DisplayData] mapping agent names to display data from
    a JSON dict
    """
    display_data = dict()
    for index in data_dict:
        agent_info = data_dict[index]
        for agent_name in agent_info:
            agent_data = agent_info[agent_name]
            display_data[agent_name] = DisplayData.from_dict(agent_data)
    return display_data


def translate_agent_positions(
    data: AgentData,
    default_translation: np.ndarray,
    translation_per_type: Dict[str, np.ndarray] = {}
) -> AgentData:
    """
    Translate all spatial data for each frame of simularium trajectory data

    Parameters
    ----------
    data : AgentData
        Trajectory data, containing the spatial data to be traslated
    default_translation : np.ndarray (shape = [3])
        XYZ translation for all agents not specified in translation_per_type
    translation_per_type : Dict[str, int]
        translation for agents of each type
        Default: {}
    """
    total_steps = data.times.size
    for time_index in range(total_steps):
        for agent_index in range(int(data.n_agents[time_index])):
            if (
                data.types[time_index][agent_index]
                in translation_per_type
            ):
                translation = translation_per_type[
                    data.types[time_index][agent_index]
                ]
            else:
                translation = default_translation
            data.positions[time_index][agent_index] += translation
    return data

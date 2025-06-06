
from seismometer.configuration import ConfigProvider

def gather_prediction_types(config: ConfigProvider) -> dict[str, str]:
    """
    Gathers the defined types from the configuration dictionary.
    
    Parameters
    ----------
    config : ConfigProvider
        The loaded configuration object.

    Returns
    -------
    dict[str, str]
        the type dictionary with the structure dict[column] = type
    """
    return {defn.name: defn.dtype for defn in config.prediction_defs.predictions if defn.dtype is not None}
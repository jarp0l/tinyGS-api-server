from decouple import config

def get_config(config_name: str) -> str | int:
    return config(config_name)
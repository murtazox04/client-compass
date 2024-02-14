from decouple import config

from .base import *

env_type = config("ENV_TYPE", default="local")

if env_type == "local":
    from .local import *
elif env_type == "staging":
    from .staging import *
elif env_type == "production":
    from .production import *
else:
    raise Exception("Invalid ENV_TYPE")

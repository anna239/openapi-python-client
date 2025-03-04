from pathlib import Path
from typing import Dict, Optional

import yaml
from pydantic import BaseModel


class ClassOverride(BaseModel):
    """An override of a single generated class.

    See https://github.com/openapi-generators/openapi-python-client#class_overrides
    """

    class_name: Optional[str] = None
    module_name: Optional[str] = None


class Config(BaseModel):
    """Contains any configurable values passed by the user.

    See https://github.com/openapi-generators/openapi-python-client#configuration
    """

    class_overrides: Dict[str, ClassOverride] = {}
    project_name_override: Optional[str]
    package_name_override: Optional[str]
    package_version_override: Optional[str]
    field_prefix: str = "field_"

    @staticmethod
    def load_from_path(path: Path) -> "Config":
        """Creates a Config from provided JSON or YAML file and sets a bunch of globals from it"""
        config_data = yaml.safe_load(path.read_text())
        config = Config(**config_data)
        return config

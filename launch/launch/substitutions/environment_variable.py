# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for the EnvironmentVariable substitution."""

import os
from typing import List
from typing import Text
from typing import Union
from typing import overload

from ..launch_context import LaunchContext
from ..substitution import Substitution


class EnvironmentVariable(Substitution):
    """
    Substitution that gets an environment variable value as a string.

    If the environment variable is not found, it returns empty string.
    """

    @overload
    def __init__(self, *, name: Text):
        """Construct with just Text (unicode string)."""
        ...

    @overload  # noqa: F811
    def __init__(self, *, name: List[Union[Text, Substitution]]):
        """Construct with list of Text and Substitutions."""
        ...

    def __init__(self, *, name):  # noqa: F811
        """Constructor."""
        super().__init__()

        from ..utilities import normalize_to_list_of_substitutions  # import here to avoid loop
        self.__name = normalize_to_list_of_substitutions(name)

    @property
    def name(self) -> List[Substitution]:
        """Getter for name."""
        return self.__name

    def perform(self, context: LaunchContext) -> Text:
        """Perform the substitution by looking up the environment variable."""
        from ..utilities import perform_substitutions  # import here to avoid loop
        return os.environ.get(perform_substitutions(context, self.name), '')

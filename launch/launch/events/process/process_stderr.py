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

"""Module for ProcessStderr event."""

from typing import Dict
from typing import List
from typing import Optional
from typing import Text

from .process_io import ProcessIO


class ProcessStderr(ProcessIO):
    """Event emitted when a process generates output on stderr."""

    name = 'launch.events.process.ProcessStderr'

    def __init__(
        self,
        *,
        action: 'launch.actions.ExecuteProcess',
        cmd: List[Text],
        cwd: Optional[Text],
        env: Optional[Dict[Text, Text]],
        text: bytes,
    ):
        """
        Constructor.

        :param: action is the ExecuteProcess action associated with the event
        :param: cmd is the final command after substitution expansion
        :param: cwd is the final working directory after substitution expansion
        :param: env is the final environment variables after substitution expansion
        :param: text is the unicode data associated with the event
        """
        super().__init__(action=action, cmd=cmd, cwd=cwd, env=env, text=text, fd=2)
import os

import pytest
from iotedgedev.envvars import EnvVars
from iotedgedev.output import Output
from tests.utility import runner_invoke

pytestmark = pytest.mark.e2e

output = Output()
envvars = EnvVars(output)
test_solution_shared_lib_dir = os.path.join(os.getcwd(), "tests", "assets", "test_solution_shared_lib")


def test_iothub_setup():
    # Arrange
    os.chdir(test_solution_shared_lib_dir)

    # Act
    runner_invoke(['iothub', 'setup'])

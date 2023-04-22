# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Checks that the expected operators are registered."""

from absl.testing import absltest

from temporian.core import operator_lib
from temporian.core.operators import all_operators


class RegisteredOperatorsTest(absltest.TestCase):
    def test_base(self):
        # Note: The operators are stored alphabetically.
        expected_operators = [
            "ADDITION",
            "CALENDAR_DAY_OF_MONTH",
            "CALENDAR_DAY_OF_WEEK",
            "CALENDAR_ISO_WEEK",
            "CALENDAR_YEAR",
            "CALENDAR_MINUTE",
            "CALENDAR_DAY_OF_YEAR",
            "CALENDAR_MONTH",
            "CALENDAR_HOUR",
            "CALENDAR_SECOND",
            "DIVISION",
            "FILTER",
            "FLOORDIV",
            "GLUE",
            "LAG",
            "MOVING_COUNT",
            "MOVING_STANDARD_DEVIATION",
            "MOVING_SUM",
            "MULTIPLICATION",
            "PREFIX",
            "PROPAGATE",
            "SAMPLE",
            "SELECT",
            "SIMPLE_MOVING_AVERAGE",
            "SUBTRACTION",
            "SET_INDEX",
            "DROP_INDEX",
            "UNIQUE_TIMESTAMPS",
        ]

        self.assertSetEqual(
            set(operator_lib.registered_operators().keys()),
            set(expected_operators),
        )


if __name__ == "__main__":
    absltest.main()

#  Copyright (c) 2015-2018 Cisco Systems, Inc.  # noqa: D100
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
from __future__ import annotations

import pytest

from molecule.status import Status


@pytest.fixture()
def _instance():  # type: ignore[no-untyped-def]  # noqa: ANN202
    s = Status(
        instance_name=None,  # type: ignore[arg-type]
        driver_name=None,  # type: ignore[arg-type]
        provisioner_name=None,  # type: ignore[arg-type]
        scenario_name=None,  # type: ignore[arg-type]
        created=None,  # type: ignore[arg-type]
        converged=None,  # type: ignore[arg-type]
    )

    return s  # noqa: RET504


def test__instance_name_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.instance_name is None


def test_status_driver_name_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.driver_name is None


def test_status_provisioner_name_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.provisioner_name is None


def test_status_scenario_name_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.scenario_name is None


def test_status_created_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.created is None


def test_status_converged_attribute(_instance):  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN201, PT019, D103
    assert _instance.converged is None

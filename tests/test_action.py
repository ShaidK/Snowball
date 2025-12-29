#
# File: test_action.py | Note: Following file maintains testing of the Semantic Version validation 
#

#
# MIT License
# 
# Copyright (c) 2025 ShaidK
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from snowball.action import SemanticVersionService
import pytest
import uuid

class TestSemanticVersionService:
    """
    The following class represent the tests associated with the class: TestSemanticVersionService
    """

    @pytest.mark.failure
    @pytest.mark.parametrize(
        "version", [
            1,
            1.0,
            True,
            None,
            {},
            ()
        ]
    )
    def test__GIVEN__Invalid_Semantic_Version_Type__WHEN__Validating_Semantic_Version__THEN__Raise_ValueError(self, version: str) -> None:
        with pytest.raises(expected_exception=ValueError, match=f"Invalid type for parameter 'version': expected str, got {type(version).__name__}"):
            SemanticVersionService.validate(version=version)


    @pytest.mark.failure
    @pytest.mark.parametrize(
        "version", [
            #
            # NOTE: Invalid string args
            #
            str(uuid.uuid4),
            "",
            "+build",
            "-alpha",

            #
            # NOTE: Invalid version string args
            #
            "a1.0.1",
            "Y0.2.1",

            #
            # NOTE: Extra segment args
            #
            "1.0.0.0",

            #
            # NOTE: Missing segment args
            #
            "1",
            "1.0",
            "1.0.",
            ".1.0",
            ".1",
            ".1.0.1",
            "1..1",

            #
            # NOTE: Leading zeroes args
            #
            "01.1.1",
            "1.01.0",
            "1.0.01",
            "1.0.0-01",

            #
            # NOTE: Negative & non-numeric args
            #
            "-1.0.0",
            "1.-1.0",
            "1.0.-1",
            "x.y.z",
            "1.y.0",
            "1.0.z",
            "x.0.0",

            #
            # NOTE: Empty build & pre-release args
            #
            "1.0.0-",
            "1.0.0-alpha.",
            "1.0.0+build.",
            "1.0.0alpha..beta",
            "1.0.0-alpha..x",
            "1.0.0+build..",
            "1.0.0+build..gamma",
            "1.0.0-."

            #
            # NOTE: Invalid spaces & trailing args
            #
            "1.0.0 ",
            " 1.0.0",
            "1.0.0-alpha beta",
            "1.0.0alpha",

            #
            # NOTE: Illegal character args
            #
            "1.0.0-alpha!",
            "1.0.0#hash",
            "1.0.0-?",
            "1.0.0-xyz_xyz",
            "1.0.0+xyz/xyz",
            "1.0.0+build@gamma",
            
            #
            # NOTE: Multiple plus & dashes args
            #
            "1.0.0++build",
            "1.0.0-alpha+beta+gamma",

            #
            # NOTE: Mixed seperators args
            #
            "1-0-0",
            "1_0_0",
            "1+0-0"

            #
            # NOTE: The following arg conditions evaluates True even though it seem invalid.
            #       This has been confirmed by the following Project: 'semver' Github Issue
            #
            #       https://github.com/python-semver/python-semver/issues/468
            #
        ]
    )
    def test__GIVEN__Invalid_Semantic_Version_String__WHEN__Validating_Semantic_Version__THEN__Return_False(self, version: str) -> None:
        try:
            assert SemanticVersionService.validate(version=version) is False
        except Exception as err:
            pytest.fail(f"FATAL: Error raise when testing the class: TestSemanticVersionService \n{err}")

    @pytest.mark.success
    @pytest.mark.parametrize(
        "version", [
            #
            # NOTE: Valid string args
            #
            "v1.0.0",
            "V1.0.0",
            "1.0.0",
            "1.2.5",
            "10.20.30",

            #
            # NOTE: Pre-release args
            #
            "1.0.0-a",
            "1.0.0+a",
            "1.0.0-alpha",
            "1.0.0-alpha.1",
            "1.0.0-rc.1",
            "1.0.0-alpha.beta",
            "1.0.0-x.7.z.78",
            "1.2.3-0.3.7",
            "1.0.0-1",
            "1.0.0-2.2.2",
            "1.0.0-alpha-678",

            #
            # NOTE: Build metadata args
            #
            "1.0.0-alpha-beta",
            "1.0.0-alpha-beta+build-678",
            "1.0.0-20220220202020",
            "1.0.0+exp.sha.2020f20",
            "1.0.0-alpha+001",
            "1.0.0-alpha.1+build.7",
            "1.0.0-rc.1+build.1",
            "1.0.0+build.222.meta",

            #
            # NOTE: Case sensitive args
            #
            "1.0.0-AA-BB-222",

            #
            # NOTE: Large numerics args
            #
            "222222222222222222222.0.0",
            "2.222222222222222222222.2",
            "2.2.222222222222222222222",
            "222222222222222222222.222222222222222222222.222222222222222222222-alpha-beta-gamma-delta+build.epsilon.zeta.omega"

            #
            # NOTE: Additional dot args
            #
            "1.0.0-alpha.beta.gamma.delta",

            #
            # NOTE: Build / pre-release ordering args
            #
            "1.0.0-alpha+build",
            "1.0.0+build-alpha"
        ]
    )
    def test__GIVEN__Valid_Semantic_Version_String__WHEN__Validating_Semantic_Version__THEN__Return_True(self, version: str) -> None:
        try:
            assert SemanticVersionService.validate(version=version) is True
        except Exception as err:
            pytest.fail(f"FATAL: Error raise when testing the class: TestSemanticVersionService \n{err}")

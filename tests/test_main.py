#
# File: test_cli.py | Note: Following file maintains testing of the main function 
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

from snowball.action import SemanticVersionService, cli
from _pytest.capture import CaptureFixture
from pytest_mock import MockerFixture

import pytest

class TestCLI:
    """
    The following class represent the tests associated with the function: cli
    """
    INVALID_SEMANTIC_VERSION="A0.0.0+build+alpha"

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_Type__WHEN__Inputting_Within_System_Arguements__THEN__Exception_Is_Handled(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=type(int))
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_Type_With_Invalid_Args__WHEN__Inputting_Within_System_Arguements__THEN__Exception_Is_Handled(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "--n", type(int) ])
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_Type_With_Valid_Short_Args__WHEN__Inputting_Within_System_Arguements__THEN__Exception_Is_Handled(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "-v", type(int) ])
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_Type_With_Valid_Long_Args__WHEN__Inputting_Within_System_Arguements__THEN__Exception_Is_Handled(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "--version", type(int) ])
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_Type_With_Invalid_Service__WHEN__Inputting_Within_System_Arguements__THEN__Exception_Is_Handled(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "--version", self.INVALID_SEMANTIC_VERSION ], service=None)
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version___WHEN__SemanticVersionService_Raises_Error__THEN__Exception_Is_Handled(self, mocker: MockerFixture, capsys: CaptureFixture[str]) -> None:
        service = mocker.Mock(spec=SemanticVersionService)
        service.validate.side_effect = Exception()
        
        result = cli(args=[ "--version", self.INVALID_SEMANTIC_VERSION ], service=service)
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Unhandled Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version___WHEN__SemanticVersionService_Raises_ValueError__THEN__Exception_Is_Handled(self, mocker: MockerFixture, capsys: CaptureFixture[str]) -> None:
        service = mocker.Mock(spec=SemanticVersionService)
        service.validate.side_effect = ValueError()
        
        result = cli(args=[ "--version", self.INVALID_SEMANTIC_VERSION ], service=service)
        assert result == 1
        std = capsys.readouterr()
        assert "::error title=Validation Error::" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_With_Valid_Long_Arguement___WHEN__Inputting_Within_System_Arguements__THEN__Validation_Failed_Message(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "--version", self.INVALID_SEMANTIC_VERSION ])
        assert result == 1
        std = capsys.readouterr()
        assert f"::notice title=Validation Failure::Following version: {self.INVALID_SEMANTIC_VERSION} fails to conforms to Semantic Versioning" in std.out 

    @pytest.mark.failure
    def test__GIVEN__Invalid_Semantic_Version_With_Valid_Short_Arguement___WHEN__Inputting_Within_System_Arguements__THEN__Validation_Failed_Message(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "-v", self.INVALID_SEMANTIC_VERSION ])
        assert result == 1
        std = capsys.readouterr()
        assert f"::notice title=Validation Failure::Following version: {self.INVALID_SEMANTIC_VERSION} fails to conforms to Semantic Versioning" in std.out 

    @pytest.mark.success
    def test__GIVEN__Valid_Semantic_Version_With_Valid_Long_Arguement___WHEN__Inputting_Within_System_Arguements__THEN__Validation_Success_Message(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "--version", "V0.1.0" ])
        assert result == 0
        std = capsys.readouterr()
        assert "::notice title=Validation Successful::Following version: V0.1.0 conforms to Semantic Versioning" in std.out 


    @pytest.mark.success
    def test__GIVEN__Valid_Semantic_Version_With_Valid_Short_Arguement___WHEN__Inputting_Within_System_Arguements__THEN__Validation_Success_Message(self, capsys: CaptureFixture[str]) -> None:
        result = cli(args=[ "-v", "V0.1.0" ])
        assert result == 0
        std = capsys.readouterr()
        assert "::notice title=Validation Successful::Following version: V0.1.0 conforms to Semantic Versioning" in std.out 

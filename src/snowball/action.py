#
# File: action.py | Note: Following file maintains validation of the Semantic Version 
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

from typing import Optional
from semver import Version
import argparse
import sys

class SemanticVersionService:
    """
    The following class is responsible for validating the semantic version string.
    This ensure that the input conforms to Semantic Versioning specification.
    """

    @staticmethod
    def validate(version: str) -> bool:
        """
        The following static function validates if the provided string conform to 
        Semantic Versioning specification.
        
        :param version: Parameter sematic version string to be validated
        :type version: str

        :return: True if the string is valid semantic version else False
        :rtype: bool
        """
        if not isinstance(version, str):
            raise ValueError(
                f"Invalid type for parameter 'version': expected str, got {type(version).__name__}"
            )
        return Version.is_valid(version=version.lstrip("Vv"))

def cli(args: Optional[list[str]] = None, service: SemanticVersionService = SemanticVersionService) -> int:
    """
    The following function represent the CLI entrypoint to validate the Semantic
    Version string.
    
    Parses '--version/-v' & validates it against a provided service. Suited for 
    Local Usage & CI environments (aka GitHub Actions Workflows annotations).

    :param args: Optional list of CLI arguements 
    :type args: Optional[list[str]]
    :param service: Description
    :type service: SemanticVersionService
    :return: Exit Codes (0 = valid, 1 = invalid & errors) 
    :rtype: int
    """
    try:
        parser = argparse.ArgumentParser(description="Validate the Semantic Version string", prog="semver-service")
        parser.add_argument("-v", "--version", required=True, help="Provided version string to validates if it conforms to Semantic Versioning")
        namespace = parser.parse_args(args=args)

        if service.validate(version=namespace.version):
            print(f"::notice title=Validation Successful::Following version: {namespace.version} conforms to Semantic Versioning")
            return 0
        print(f"::notice title=Validation Failure::Following version: {namespace.version} fails to conforms to Semantic Versioning")
        return 1
    except ValueError as err:
        print(f"::error title=Validation Error::{err}")
        return 1
    except Exception as err:
        print(f"::error title=Unhandled Error::{err}")
        return 1

# pragma: no cover
if __name__ == "__main__":
    sys.exit(cli())
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

from semver import Version

class SemanticVersionValidation:
    """
    The following class is responsible for validating the semantic version string.
    This ensure that the input conforms to Semantic Versioning specification
    """

    @staticmethod
    def validate(version: str) -> bool:
        """
        The following static function validates if the provided string conform to 
        Semantic Versioning specification
        
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

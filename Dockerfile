# syntax=docker/dockerfile:1

#
# File: Dockerfile | Note: Following file represent the Snowball Docker Image
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

#
# NOTE: Docker Multistage Build - Build Stage
#
FROM python:3.14-slim as build

WORKDIR /build

COPY . .
RUN python -m pip install --no-cache-dir --upgrade pip poetry && \
    poetry install --without ci --without test

RUN poetry build --format wheel

#
# NOTE: Docker Multistage Build - Execution Stage
#
FROM python:3.14-slim

COPY --from=build /build/dist/*.whl .
RUN pip install --no-cache-dir *.whl

ENTRYPOINT ["snowball"]

![Snowstorm](img/snowball.png)

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fshaidk%2Fsnowball%2Fbuild%2Fpyproject.toml&style=flat-square&labelColor=2980B9&color=46535E)
![License](https://img.shields.io/github/license/shaidk/snowball?style=flat-square&labelColor=2980B9&color=46535E)
![Build](https://img.shields.io/github/actions/workflow/status/shaidk/snowball/build.yml?style=flat-square&labelColor=2980B9&color=46535E&label=build)
![Docker](https://img.shields.io/github/actions/workflow/status/shaidk/snowball/docker.yml?style=flat-square&labelColor=2980B9&color=46535E&label=docker)

#### INTEGRATION

The "Snowball" Action is a [GitHub Action][1] designed to validate a provided
Semantic Version. The "Snowball" Action is based upon the [GitHub Action for
Docker][2] which uses a Docker Image to execute the GitHub Action.

To integrate the "Snowball" Action within your Github Workflow you need to
add the following steps within your Github Workflow File:

```yml
- name: Validate Semantic Version
  uses: ShaidK/Snowball@v0.12.0
  with:
      version: '<VERSION_TO_VALIDATE>'
```

#### INPUT

The "Snowball" Action requires the Input Parameter: `version`. The Input
Parameter defines the string which need to be validated & confirm if it
conforms to Semantic Versioning.

#### OUTPUT

The "Snowball" Action will output if the Version validates & conforms to
Semantic Versioning or will output an Error if the string does not
conform.

#### USAGE

The following is an example usage of the "Snowball" Action to validate
the Semantic Version string:

```yml
jobs:
    validate_version:
        runs-on: ubuntu-latest
        name: Validate Semantic Version
        steps:
            - uses: actions/checkout@v6
              with:
                  fetch-depth: 0

            - name: Validate Semantic Version
              uses: ShaidK/Snowflake@v0.12.0
              with:
                  version: 'V0.12.0'
```

#### PROJECT STRUCTURE

Following is the structure of the Snowball GitHub Action Project:

```text
.
├── pyproject.toml
├── poetry.lock
├── Dockerfile
├── CHANGELOG
├── LICENSE
├── README.md
├── .gitattributes
├── .gitignore
├── .yamllint
├── .dockerignore
├── .github
│   └── workflows
│       ├── docker.yml
│       └── build.yml
├── img
│   ├── polar_bear.png
│   └── snowball.png
├── src
│   └── snowball
│       ├── action.py
│       └── __init__.py
└── tests
    ├── test_action.py
    └── test_main.py
```

#### DOCKER IMAGE

The "Snowball" Project build a Docker Image which is used for the execution
of the GitHub Action. The Docker Image can be pulled using the following
Command:

```shell
docker pull ghcr.io/shaidk/snowball:<VERSION>
```

The "Snowball" Docker Image can then be executed within a Container using
the following Command:

```shell
docker run ghcr.io/shaidk/snowball:<VERSION> --version V1.0.0
```

#### LICENSE

```text
MIT License

Copyright (c) 2025 ShaidK

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

<p align="center">
    <img src="./img/polar_bear.png" style="width: 100px; padding: 50px;" />
</p>

[1]: https://github.com/features/actions
[2]: https://docs.github.com/en/actions/tutorials/use-containerized-services/create-a-docker-container-action

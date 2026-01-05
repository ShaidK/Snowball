![Snowstorm](img/snowball.png)

![License](https://img.shields.io/github/license/shaidk/snowball?color=00B4D4)

#### INTEGRATION

The "Snowball" Action is a [GitHub Action][1] designed to validate a provided
Semantic Version. The "Snowball" Action is based upon the GitHub Action for
Docker which uses a Docker Image to execute the GitHub Action step.

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

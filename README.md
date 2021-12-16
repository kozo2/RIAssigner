# RIAssigner
[![Python package](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package.yml/badge.svg)](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package.yml)
[![Python Package using Conda](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package-conda.yml/badge.svg?branch=main)](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package-conda.yml)
[![Anaconda Build](https://github.com/RECETOX/RIAssigner/actions/workflows/anaconda.yml/badge.svg?branch=main)](https://github.com/RECETOX/RIAssigner/actions/workflows/anaconda.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=hechth_RIAssigner&metric=alert_status)](https://sonarcloud.io/dashboard?id=hechth_RIAssigner)
[![bioconda package](https://img.shields.io/conda/v/bioconda/riassigner)](https://anaconda.org/bioconda/riassigner)
## Overview
RIAssigner is a python tool for retention index (RI) computation for GC-MS data developed at [RECETOX](https://www.recetox.muni.cz/en).

## Installation
Installation is currently possible by creating the conda environment with `conda env create -f conda/environment-dev.yml` and then installing the package with `python -m pip install -e .`

Install via [bioconda](https://anaconda.org/bioconda/riassigner) using `conda install -c bioconda riassigner`

## Usage
RIAssigner can be used to read data from `.msp`, `.csv` and `.tsv` files using [matchms](https://github.com/matchms/matchms) and [pandas](https://pandas.pydata.org/) and to compute the retention indices for the data.
A reference list of retention indexed compounds (traditionally an Alkane series) with retention times is used to compute the RI for a query dataset of retention time values using the [van Den Dool and Kratz](https://doi.org/10.1016/S0021-9673(01)80947-X) method or by using [cubic spline based interpolation](https://doi.org/10.1021/ac50035a026).
### Example
```python
from RIAssigner.compute import Kovats
from RIAssigner.data import MatchMSData, PandasData

# Load reference & query data
query = PandasData("../tests/data/csv/aplcms_aligned_peaks.csv", "csv", rt_unit="seconds")
reference = MatchMSData("../tests/data/msp/Alkanes_20210325.msp", "msp", rt_unit="min")

# Compute RI and write it back to file
query.retention_indices = Kovats().compute(query, reference)
query.write("peaks_with_rt.csv")
```
For more details check out this [notebook](doc/example_usage.ipynb) or try this tool on [Galaxy](https://umsa.cerit-sc.cz/).

## Developer Documentation
### Setup
Create your development environment using the provided [script](conda/environment-dev.yml) via conda to install all required dependencies, including linter and testing frameworks.

### Contributing
We appreciate contributions - feel free to open an issue on our repository, create your own fork, work on the problem and pose a PR.
Make sure to add your contributions to the [changelog](CHANGELOG.md) and to adhere to the [versioning](https://semver.org/spec/v2.0.0.html).
For more information see [here](CONTRIBUTING.md).
### Architecture
<!-- generated by mermaid compile action - START -->
![~mermaid diagram 1~](/.resources/README-md-1.svg)
<details>
  <summary>Mermaid markup</summary>

```mermaid
classDiagram
    class MatchMSData{
        -List ~Spectra~ data
    }

    class PandasData {
        -DataFrame data
    }

    Data <|-- MatchMSData
    Data <|-- PandasData

    class Data{
        <<abstract>>
        +read(string filename)
        +write(string filename)
        +retention_times() List~float~
        +retention_indices() List~int~
    }


    class ComputationMethod{
        <<interface>>
        +compute(Data query, Data reference) List~int~

    }

    class Kovats {

    }
    class CubicSpline {

    }

    ComputationMethod <|-- Kovats
    ComputationMethod <|-- CubicSpline

```

</details>
<!-- generated by mermaid compile action - END -->

### Testing
All functionality is tested with the [pytest](https://docs.pytest.org/en/6.2.x/contents.html) framework. Make sure to run your IDE in the `riassigner-dev` conda environment (or make sure to use the respective python interpreter when developing) to follow formatting guidelines and to be able to execute the tests.

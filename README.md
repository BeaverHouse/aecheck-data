<p align="center">
  <a href="https://github.com/HU-Lee/aecheck-data">
    <img src="logo.png" alt="Logo">
  </a>

  <p align="center">
    Data & processing code for AE Check
    <br>
    <br>
    <a href="https://github.com/HU-Lee/aecheck-data/issues">Bug Report</a>
    |
    <a href="https://github.com/HU-Lee/aecheck-data/issues">Request to HU-Lee</a>
  </p>

  <p align="center">
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    </a>
    <a href="https://python-poetry.org/">
      <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
    </a>
    <a href="https://pandas.pydata.org/">
      <img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
    </a>
    <a href="https://docs.pytest.org/en/8.0.x/">
      <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
    </a>
    <a href="./LICENSE">
      <img src="https://img.shields.io/github/license/HU-Lee/aecheck-data" alt="License">
    </a>
  </p>
</p>

<!-- Content -->

<br>

## Description

Data & processing code for [AE Check][aecheck].  
It is processed manually and migrated to [frontend repository][aecheck-v3].

**Timeline**

|     **Data**      |         **Description**          |
| :---------------: | :------------------------------: |
| 2022.09 ~ 2023.09 |             v2 code              |
| 2023.09 ~ 2024.02 |  add v3 code, auto-migrate data  |
|     2024.02 ~     | delete v2 code, clean repository |

**Data source**

- Raw app data
- [Seesaa wiki][seesaa]
- [AE wiki][aewiki]
- [altema.jp][altema]

<br>

## Requirements

1. You need to install [Python 3.12][py312] and [Poetry][poetry] to manage the packages.  
   To install Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. You need to set repository secret to run GitHub Actions.

   - `GH_PAT_ORGANIZATION` : Fine-grained access token for organization repositories

<br>

**Install packages**

```
poetry install
```

[poetry]: https://python-poetry.org/
[py312]: https://www.python.org/downloads/release/python-3120/

<br>

## File description

- `step0.py`
  - It imports personality data from [Seesaa wiki][seesaa].
- `step1.py`
  - It adds the missing i18n tags.
- `step2.py`
  - It processes the JSON files & images, then saves to `result` folder.
- `result/updates.tsx`
  - It includes some configs and announcement formats used in frontend.

[python]: https://www.python.org/
[aecheck]: https://aecheck.com/
[aecheck-v3]: https://github.com/BeaverHouse/aecheck-v3
[seesaa]: https://anothereden.game-info.wiki
[aewiki]: https://anothereden.wiki/
[altema]: https://altema.jp/anaden/

<br>

## Contributing

See the [CONTRIBUTING.md][contributing].

[contributing]: ./CONTRIBUTING.md

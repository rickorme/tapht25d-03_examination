# tapht25d-03_examination
This is the final exam project of the course "TAPHT25D: Testautomatisering och testverktyg" by NBI/Handelsakademin yrkeshögskola.

The application being tested, "Läslistan" can be found [here](https://tap-ht25-testverktyg.github.io/exam/).

Answers to theory questions can be found in this file in the root folder:

    ANSWERS.md

# Starting the project

## Clone the GitHub repo
```bash
git clone https://github.com/rickorme/tapht25d-03_examination.git
```
## Setup the virtual environment

This project requires Python 3.x. Please follow the steps below to set up the environment and enable the running of the automated end-to-end tests.

### 1. Create and Activate a Virtual Environment
#### **On Linux / MacOS**
```bash
python -m venv .venv
source .venv/bin/activate
```

#### **On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install dependencies
``` bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers
Linux users: please read the note below first 👇
``` bash
python -m playwright install --with-deps chromium
```
#### 👉**Important note for Linux Users**👈
The `--with-deps` flag uses apt to install system libraries and is designed for Debian/Ubuntu based systems. If you are using a different Linux distribution (such as Arch, Fedora, or openSUSE), this command will fail.

Instead, omit the flag and install the browser directly:
``` bash
python -m playwright install chromium
```
Then, install the required Playwright system dependencies using your native package manager (e.g., `sudo pacman -S playwright` on Arch-based systems).

# What has been tested (and how to run the tests)

## Backend logic developed and tested using TDD (Test Driven Development)

### User stories and acceptance criteria
User stories and acceptance criteria were written to cover the functionality being tested and developed. These can be found in the root folder in file:

    STORIES.md

### Development
Three new classes were developed for the future integration of new backend logic. These were developed using TDD as the development methodology.

The new classes are found here:
 
     src/backend/the_reading_list.py

## Unit and integration tests
Unit and integration tests were written before the functional code was created, according to the TDD methodology. The tests are located here:

    tests/integration
    tests/unit

### Running the tests
The unit and integration tests are writetn using pytest. To run all unit and integration tests:

``` bash
# run from the root folder of the project
pytest
```

Pytest markers were employed so that individual groups of tests could be run independently. Here is a list of the markers which can be used:

| marker      | whichh tests are run      |
| --------    | ----------------------- |
| unit        | all unit tests          |
| integration | all integration tests | 
| katalog_01  | all tests for user story KATALOG-01-US |
| katalog_02  | all tests for user story KATALOG-02-US |
| katalog_03  | all tests for user story KATALOG-03-US |
| addbok_01   | all tests for user story ADDBOK-01-US |
| minbok_01   | all tests for user story MINBOK-01-US |
| stat_01     | all tests for user story STAT-01-US |

Markers can be used to run individual groups of tests as follows:

``` bash
# run from the root folder of the project
pytest -m <marker>
```

## E2E (End to End) tests using BDD framework
The E2E tests were applied to existing functionality, so whilst a BDD (Behaviour Driven Development) framework was implemented, it was used only for testing, not development.

I have attempted to cover all of the existing functionality of the application, writing feature files to describe the expected behaviour of the application (using Gherkin syntax). Feature files are located here:

    src/features/

The testing stack is Python, using Behave and Playwright. Testing logic is defined in step files and page files, located here:

    src/features/steps
    src/features/pages

### Running the E2E tests
To run all E2E tests:

``` bash
# run from the root folder of the project
behave

# Run with debug messages enabled
behave --no-capture
```

Feature tags were employed so that individual groups of tests could be run independently. Here is a list of the tags which can be used:

| marker      | whichh tests are run      |
| --------    | ----------------------- |
| katalog_01  | all tests for user story KATALOG-01-US |
| katalog_02  | all tests for user story KATALOG-02-US |
| katalog_03  | all tests for user story KATALOG-03-US |
| addbok_01   | all tests for user story ADDBOK-01-US |
| minbok_01   | all tests for user story MINBOK-01-US |
| stat_01     | all tests for user story STAT-01-US |
| nav_01      | all tests for user story NAV-01-US |

Markers can be used to run individual groups of tests as follows:

``` bash
# run from the root folder of the project
behave --tags=<tag>
```



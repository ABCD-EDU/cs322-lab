# cs322-lab
This repository contains all the exercises and projects for cs322 midterms

## How to set-up
### Anaconda Setup
1. Install `anaconda` by downloading the installer in https://www.anaconda.com/products/individual
2. After installing anaconda, open your conda terminal `Anaconda Prompt(anaconda3)`
3. (Optional) update your conda by using `conda update conda`

### Creating your environment
1. Create a new environment and install the necessary requirements for the specific project
```
$ cd ./<project-path>
$ conda create --name <name> --file requirements.txt
```

## Pushing changes to the repository
**If you are working alone on a specific task, ignore this.**
1. Create a branch with the naming convention `task--activity-surname` (ex. `lab1--naivebayes-arevalo`. the shorter the better)
2. If you are committing your changes, do it the normal way and ask for a pull request. Make sure there are no conflicts

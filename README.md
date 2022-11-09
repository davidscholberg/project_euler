# Project Euler

These are my solutions to the [Project Euler][project-euler-site] problem set. The solutions are written in [Python][python].

[project-euler-site]: https://projecteuler.net/
[python]: https://www.python.org/

### Setup

```bash
git clone https://github.com/davidscholberg/project_euler.git
cd project_euler
./install_commit_hooks # this will install a hook to run the unit tests on commit
```

### Running Solutions

To run the solution for a particular problem, pass the problem number to the `solve` script:

```bash
./solve 24
```

The `solve` script runs the solution and compares the computed answer against the correct answer, the list of which was obtained from [luckytoilet/projecteuler-solutions][projecteuler-solutions].

[projecteuler-solutions]: https://github.com/luckytoilet/projecteuler-solutions

### Project Directory Structure

* [project_euler/][project-euler] - Main project package. All python source files go in here.
    * [data/][data] - Input data for problems that have non-trivial input.
    * [solutions/][solutions] - Solution files, one per solution. Logic should be kept to a minimum here.
    * [util/][util] - Package where reusable logic resides. All code here should have unit tests.
* [install_commit_hooks][install-commit-hooks] - Script to install unit test commit hook.
* [solve][solve] - Script that runs the project solution for the given problem number.
* [test][test] - Script that runs all unit tests.

[project-euler]: project_euler
[data]: project_euler/data
[solutions]: project_euler/solutions
[util]: project_euler/util
[install-commit-hooks]: install_commit_hooks
[solve]: solve
[test]: test
# Contributing to fconv

Bug reports and code and documentation patches are welcome. 

## 1. Reporting bugs

**It's important that you provide the full command argument list
as well as the output of the failing command.**

Use the `--debug` flag and copy&paste both the command and its output
to your bug report, e.g.:

```bash
$ fconv <COMPLETE ARGUMENT LIST THAT TRIGGERS THE ERROR> --debug
<COMPLETE OUTPUT>
```

## 2. Contributing Code and Docs

Before working on a new feature or a bug, please browse [existing issues](https://github.com/wf001/fconv/issues)
to see whether it has previously been discussed.

If you are fixing an issue, the first step should be to create a test case that
reproduces the incorrect behaviour. That will also help you to build an
understanding of the issue at hand.

### Development Environment

#### Getting the code

Go to <https://github.com/wf001/fconv> and fork the project repository.

```bash
# Clone your fork
git clone git@github.com:<YOU>/fconv.git

# Enter the project directory
cd fconv

# Create a branch for your changes
git checkout -b my_topical_branch
```

#### Setup

The [Makefile](https://github.com/wf001/fconv/blob/master/Makefile) contains a bunch of tasks to get you started.

To get started, run the command below, which:


#### install all of dependencies.
``` bash
make install-dev
```

#### test
``` bash
make check
```

- Before running this command, recommend to create an isolated Python virtual environment inside `./venv`
  (via the standard library [venv](https://docs.python.org/3/library/venv.html) tool);

```bash
source venv/bin/activate
```

#### Making Changes

Please make sure your changes conform to [Style Guide for Python Code](https://python.org/dev/peps/pep-0008/) (PEP8)
and that `make check` passes.

#### Testing & CI

Please add tests for any new features and bug fixes.

When you open a Pull Request, [GitHub Actions](https://github.com/wf001/fconv/actions) will automatically run fconv’s [test suite](https://github.com/wf001/fconv/tree/master/tests) against your code, so please make sure all checks pass.

#### Running tests locally

fconv uses the [pytest](https://pytest.org/) runner.

```bash
# Run tests on the current Python interpreter.
make test

# Run extended tests for code
make check
```


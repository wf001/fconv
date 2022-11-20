import sys
from unittest import mock

import pytest

from former.__main__ import main


@pytest.mark.parametrize(
    "argv",
    [
        ["former", "json", "yaml", "-i", "hoge"],
        ["former", "yaml", "json", "-i", "hoge"],
        ["former", "json", "yaml", "-i", "hoge", "-o", "fuga"],
    ],
)
def test_cli_valid_args(capfd, argv):
    with mock.patch.object(sys, "argv", argv):
        main()
        out, err = capfd.readouterr()
        assert "Namespace" in out


@pytest.mark.parametrize(
    "args",
    [
        ["former", "json"],
        ["former", "json", "yaml"],
        ["former", "json", "-i", "hoge"],
    ],
)
def test_cli_invalid_args1(capfd, args):
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", args):
            main()
    out, err = capfd.readouterr()
    assert "required:" in err
    assert "error:" in err


@pytest.mark.parametrize("args", [["former", "json", "yaml", "-i"]])
def test_cli_invalid_args2(capfd, args):
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", args):
            main()
    out, err = capfd.readouterr()
    assert "expected one argument" in err
    assert "error:" in err


def test_cli_print_version(capfd):
    argv = ["former", "--v"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "version" in out


def test_cli_print_help(capfd):
    argv = ["former", "--h"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "usage:" in out


def test_cli_no_arg(capfd):
    argv = ["former"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "usage:" in err
    assert "error:" in err

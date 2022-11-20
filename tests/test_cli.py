import sys
from unittest import mock

import pytest

from former import __prog__
from former.__main__ import main


@pytest.mark.parametrize(
    "argv",
    [
        [__prog__, "json", "yaml", "-i", "hoge"],
        [__prog__, "yaml", "json", "-i", "hoge"],
        [__prog__, "json", "yaml", "-i", "hoge", "-o", "fuga"],
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
        [__prog__, "json"],
        [__prog__, "json", "yaml"],
        [__prog__, "json", "-i", "hoge"],
    ],
)
def test_cli_invalid_args1(capfd, args):
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", args):
            main()
    out, err = capfd.readouterr()
    assert "required:" in err
    assert "error:" in err


@pytest.mark.parametrize("args", [[__prog__, "json", "yaml", "-i"]])
def test_cli_invalid_args2(capfd, args):
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", args):
            main()
    out, err = capfd.readouterr()
    assert "expected one argument" in err
    assert "error:" in err


def test_cli_print_version(capfd):
    argv = [__prog__, "--v"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "version" in out


def test_cli_print_help(capfd):
    argv = [__prog__, "--h"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "usage:" in out


def test_cli_no_arg(capfd):
    argv = [__prog__]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "usage:" in err
    assert "error:" in err
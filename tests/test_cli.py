import sys
from unittest import mock

import pytest

from fconv import __prog__
from fconv.__main__ import main

from .fixtures import JSON_FILE_PATH, YAML_FILE_PATH


@pytest.mark.parametrize(
    "argv",
    [
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH],
        [__prog__, "yaml", "json", "-i", YAML_FILE_PATH],
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "-o", YAML_FILE_PATH],
    ],
)
def test_cli_valid_args(mocker, capfd, argv):
    m_form = mocker.patch("fconv.core.Former.form")
    with mock.patch.object(sys, "argv", argv):
        mocker.patch("fconv.core.Former._write_file")
        main()
    assert m_form.call_count == 1


@pytest.mark.parametrize(
    "argv",
    [
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH],
        [__prog__, "yaml", "json", "-i", YAML_FILE_PATH],
    ],
)
def test_cli_print_out(mocker, capfd, argv):
    m_form = mocker.patch("fconv.core.Former.form")
    m_form.return_value = "result printed out"
    out = None
    with mock.patch.object(sys, "argv", argv):
        mocker.patch("fconv.core.Former._write_file")
        main()
    out, _ = capfd.readouterr()
    assert "result printed out" in out


@pytest.mark.parametrize(
    "argv",
    [
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "-o", YAML_FILE_PATH],
        [__prog__, "yaml", "json", "-i", YAML_FILE_PATH, "-o", JSON_FILE_PATH],
    ],
)
def test_cli_not_print_out(mocker, capfd, argv):
    m_form = mocker.patch("fconv.core.Former.form")
    m_form.return_value = "result printed out"
    out = None
    with mock.patch.object(sys, "argv", argv):
        mocker.patch("fconv.core.Former._write_file")
        main()
    out, _ = capfd.readouterr()
    assert len(out) == 0


@pytest.mark.parametrize(
    "args",
    [
        [__prog__, "json"],
        [__prog__, "json", "yaml"],
        [__prog__, "json", "-i", "test.json"],
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

import sys
from unittest import mock

import pytest

from fconv import __prog__
from fconv.__main__ import main

from .fixtures import JSON_FILE_PATH, TOML_FILE_PATH, YAML_FILE_PATH


@pytest.mark.parametrize(
    "argv",
    [
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH],
        [__prog__, "yaml", "json", "-i", YAML_FILE_PATH],
        [__prog__, "toml", "json", "-i", TOML_FILE_PATH],
        [__prog__, "yaml", "toml", "-i", YAML_FILE_PATH],
        [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "-o", YAML_FILE_PATH],
    ],
)
def test_cli_valid_args(mocker, capfd, argv):
    mocker.patch("fconv.core.Former._read_file")
    m_parse_to_internal = mocker.patch("fconv.core.Former._parse_to_internal")
    m_parse_from_internal = mocker.patch("fconv.core.Former._parse_from_internal")
    mocker.patch("fconv.core.Former._write_file")
    with mock.patch.object(sys, "argv", argv):
        main()
    assert m_parse_to_internal.call_count == 1
    assert m_parse_from_internal.call_count == 1
    act_parse_to_internal_kwargs, _ = m_parse_to_internal.call_args
    act_parse_from_internal_kwargs, _ = m_parse_from_internal.call_args
    assert act_parse_to_internal_kwargs[1] == {}


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


class TestCLIOpt:
    @pytest.mark.parametrize(
        "argv, expect_opt",
        [
            # input opt
            (
                [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--json-float-as-int"],
                {"parse_float": "__int"},
            ),
            (
                [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--json-float-as-str"],
                {"parse_float": "str"},
            ),
            (
                [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--json-int-as-float"],
                {"parse_int": "float"},
            ),
            (
                [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--json-int-as-str"],
                {"parse_int": "str"},
            ),
        ],
    )
    def test_cli_json_opt_callable(self, mocker, argv, expect_opt):
        mocker.patch("fconv.core.Former._read_file")
        m_parase_to_internal = mocker.patch("fconv.core.Former._parse_to_internal")
        mocker.patch("fconv.core.Former._parse_from_internal")
        mocker.patch("fconv.core.Former._write_file")

        with mock.patch.object(sys, "argv", argv):
            main()

        act_parse_to_internal_kwargs, _ = m_parase_to_internal.call_args
        k, v = list(expect_opt.items())[0]
        assert callable(act_parse_to_internal_kwargs[1][k])
        assert act_parse_to_internal_kwargs[1][k].__name__ == v

    @pytest.mark.parametrize(
        "argv, expect_opt",
        [
            # output opt
            (
                [__prog__, "yaml", "json", "-i", YAML_FILE_PATH, "--json-skip-keys"],
                {"skipkeys": True},
            ),
            (
                [
                    __prog__,
                    "yaml",
                    "json",
                    "-i",
                    YAML_FILE_PATH,
                    "--json-ignore-check-circular",
                ],
                {"check_circular": False},
            ),
            (
                [__prog__, "yaml", "json", "-i", YAML_FILE_PATH, "--json-disallow-nan"],
                {"allow_nan": False},
            ),
            (
                [__prog__, "yaml", "json", "-i", YAML_FILE_PATH, "--json-indent", "1"],
                {"indent": 1},
            ),
            (
                [__prog__, "yaml", "json", "-i", YAML_FILE_PATH, "--json-sort-keys"],
                {"sort_keys": True},
            ),
        ],
    )
    def test_cli_json_opt(self, mocker, argv, expect_opt):
        mocker.patch("fconv.core.Former._read_file")
        mocker.patch("fconv.core.Former._parse_to_internal")
        m_parse_from_internal = mocker.patch("fconv.core.Former._parse_from_internal")
        mocker.patch("fconv.core.Former._write_file")

        with mock.patch.object(sys, "argv", argv):
            main()

        act_parse_to_internal_kwargs, _ = m_parse_from_internal.call_args
        assert act_parse_to_internal_kwargs[1] == expect_opt

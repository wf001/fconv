import sys
from unittest import mock

import pytest

from fconv import __prog__, __version__
from fconv.__main__ import main

# fmt: off
from .fixtures import (JSON_FILE_PATH, TOML_FILE_PATH, XML_FILE_PATH,
                       YAML_FILE_PATH)

# fmt: on


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
def test_cli_valid_basic_args(mocker, capfd, argv):
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
def test_cli_printed_out(mocker, capfd, argv):
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
def test_cli_not_printed_out(mocker, capfd, argv):
    m_form = mocker.patch("fconv.core.Former.form")
    m_form.return_value = "result printed out"
    out = None
    with mock.patch.object(sys, "argv", argv):
        mocker.patch("fconv.core.Former._write_file")
        main()
    out, _ = capfd.readouterr()
    assert len(out) == 0


@pytest.mark.parametrize(
    "args, err_msg",
    [
        ([__prog__], ["required:", "error:"]),
        ([__prog__, "json"], ["required:", "error:"]),
        ([__prog__, "json", "yaml"], ["required:", "error:"]),
        ([__prog__, "json", "-i", "test.json"], ["required:", "error:"]),
        ([__prog__, "json", "yaml", "-i"], ["expected one argument", "error:"]),
    ],
)
def test_cli_invalid_args(capfd, args, err_msg):
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", args):
            main()
    out, err = capfd.readouterr()
    assert err_msg[0] in err
    assert err_msg[1] in err


def test_cli_print_version(capfd):
    argv = [__prog__, "--v"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert __prog__ in out
    assert __version__ in out


def test_cli_print_help(capfd):
    argv = [__prog__, "--h"]
    with pytest.raises(SystemExit):
        with mock.patch.object(sys, "argv", argv):
            main()
    out, err = capfd.readouterr()
    assert "usage:" in out


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
def test_cli_opt_callable(mocker, argv, expect_opt):
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
        # YAML input opt
        (
            [
                __prog__,
                "xml",
                "yaml",
                "-i",
                XML_FILE_PATH,
                "--xml-process-namespaces",
            ],
            {"process_namespaces": True},
        ),
        (
            [
                __prog__,
                "xml",
                "yaml",
                "-i",
                XML_FILE_PATH,
                "--xml-process-comments",
            ],
            {"process_comments": True},
        ),
    ],
)
def test_cli_opt_in(mocker, argv, expect_opt):
    mocker.patch("fconv.core.Former._read_file")
    m_parse_to_internal = mocker.patch("fconv.core.Former._parse_to_internal")
    mocker.patch("fconv.core.Former._parse_from_internal")
    mocker.patch("fconv.core.Former._write_file")

    with mock.patch.object(sys, "argv", argv):
        main()

    act_parse_to_internal_kwargs, _ = m_parse_to_internal.call_args
    assert act_parse_to_internal_kwargs[1] == expect_opt


@pytest.mark.parametrize(
    "argv, expect_opt",
    [
        # JSON output opt
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
        # YAML output opt
        (
            [
                __prog__,
                "json",
                "yaml",
                "-i",
                JSON_FILE_PATH,
                "--yaml-explicit-start",
            ],
            {"explicit_start": True},
        ),
        (
            [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--yaml-explicit-end"],
            {"explicit_end": True},
        ),
        (
            [__prog__, "json", "yaml", "-i", JSON_FILE_PATH, "--yaml-indent", "1"],
            {"indent": 1},
        ),
        # XML input opt
        (
            [
                __prog__,
                "json",
                "xml",
                "-i",
                JSON_FILE_PATH,
                "--xml-particle-document",
            ],
            {"full_document": False},
        ),
        (
            [
                __prog__,
                "json",
                "xml",
                "-i",
                JSON_FILE_PATH,
                "--xml-disable-pretty",
            ],
            {"pretty": False},
        ),
    ],
)
def test_cli_opt_out(mocker, argv, expect_opt):
    mocker.patch("fconv.core.Former._read_file")
    mocker.patch("fconv.core.Former._parse_to_internal")
    m_parse_from_internal = mocker.patch("fconv.core.Former._parse_from_internal")
    mocker.patch("fconv.core.Former._write_file")

    with mock.patch.object(sys, "argv", argv):
        main()

    act_parse_from_internal_kwargs, _ = m_parse_from_internal.call_args
    assert act_parse_from_internal_kwargs[1] == expect_opt


@pytest.mark.parametrize(
    "argv, expect_in_opt, expect_out_opt",
    [
        (
            [
                __prog__,
                "yaml",
                "json",
                "-i",
                YAML_FILE_PATH,
                "--json-ignore-check-circular",
                "--json-indent",
                "3",
            ],
            {},
            {"check_circular": False, "indent": 3},
        ),
        (
            [
                __prog__,
                "xml",
                "yaml",
                "-i",
                XML_FILE_PATH,
                "--xml-process-comments",
                "--yaml-explicit-start",
                "--yaml-explicit-end",
            ],
            {"process_comments": True},
            {"explicit_start": True, "explicit_end": True},
        ),
    ],
)
def test_cli_multi_opt(mocker, argv, expect_in_opt, expect_out_opt):
    mocker.patch("fconv.core.Former._read_file")
    m_parse_to_internal = mocker.patch("fconv.core.Former._parse_to_internal")
    m_parse_from_internal = mocker.patch("fconv.core.Former._parse_from_internal")
    mocker.patch("fconv.core.Former._write_file")

    with mock.patch.object(sys, "argv", argv):
        main()

    act_parse_to_internal_kwargs, _ = m_parse_to_internal.call_args
    act_parse_from_internal_kwargs, _ = m_parse_from_internal.call_args
    print(m_parse_to_internal.call_args)
    assert act_parse_to_internal_kwargs[1] == expect_in_opt
    assert act_parse_from_internal_kwargs[1] == expect_out_opt


@pytest.mark.parametrize(
    "args",
    [
        (
            [
                __prog__,
                "json",
                "yaml",
                "-i",
                JSON_FILE_PATH,
                "--json-float-as-int",
                "--json-float-as-str",
            ]
        ),
        (
            [
                __prog__,
                "json",
                "yaml",
                "-i",
                JSON_FILE_PATH,
                "--json-int-as-float",
                "--json-int-as-str",
            ]
        ),
    ],
)
def test_cli_duplicate_options(capfd, args):
    with pytest.raises(ValueError) as e:
        with mock.patch.object(sys, "argv", args):
            main()
    assert "It can use either" in str(e)

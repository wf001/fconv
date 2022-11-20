from unittest.mock import MagicMock

import pytest

from former.core import Former

from .fixtures import FakeInvalidFormat, FakeValidFormat

MODULE_PATH = ".".join(["former", "core", "Former"])


@pytest.mark.parametrize(
    "Former, get_called, send_called",
    [
        (
            Former(
                src_format=FakeValidFormat,
                target_format=FakeValidFormat,
                src_path="dummy_in.json",
                target_path="dymmy_out.yaml",
            ),
            True,
            True,
        ),
        (
            Former(
                src_format=FakeValidFormat,
                target_format=FakeValidFormat,
                target_path="dymmy_out.yaml",
            ),
            False,
            True,
        ),
        (
            Former(
                src_format=FakeValidFormat,
                target_format=FakeValidFormat,
                src_path="dummy_in.json",
            ),
            True,
            False,
        ),
        (
            Former(src_format=FakeValidFormat, target_format=FakeValidFormat),
            False,
            False,
        ),
    ],
)
def test_form(mocker, Former, get_called, send_called):
    """
    Whether all of the functions inner Former().form() calling works currectly.
    """

    m_read = mocker.patch(f"{MODULE_PATH}._read_file")
    m_to = mocker.patch(f"{MODULE_PATH}._parse_to_internal")
    m_from = mocker.patch(f"{MODULE_PATH}._parse_from_internal")
    m_write = mocker.patch(f"{MODULE_PATH}._write_file")
    Former.form()
    assert m_read.called is get_called
    assert m_to.called is True
    assert m_from.called is True
    assert m_write.called is send_called


@pytest.mark.parametrize(
    "src_format, target_format",
    [
        (FakeInvalidFormat, FakeValidFormat),
        (FakeValidFormat, FakeInvalidFormat),
        (FakeInvalidFormat, FakeInvalidFormat),
    ],
)
def test_init_handle_invalid_format(mocker, src_format, target_format):
    """
    Raise ValueError when source format or/and target format isn't
    concrete class of AbstractFormat
    """

    with pytest.raises(ValueError) as e:
        Former(
            src_format=src_format,
            target_format=target_format,
            src_path="dummy.json",
            target_path="dummy.yaml",
        )
    assert str(e.value).startswith("Invalid format. expect")


def test_parse_to_internal(mocker):
    """Whether _parse_to_internal works currectly"""

    mocker.patch(f"{MODULE_PATH}._read_file")
    mocker.patch(f"{MODULE_PATH}._parse_from_internal")
    mocker.patch(f"{MODULE_PATH}._write_file")

    fake_src_ctx = "{key1:value1,key2:value2}"
    src_opt = {"indent": 1, "parse_int": float}
    fake_get_load_kwargs_ret = {"key1": "value1", "key2": "value2", "key3": "value3"}

    m_get_laod = mocker.patch.object(
        FakeValidFormat,
        "get_load_kwargs",
        MagicMock(return_value=fake_get_load_kwargs_ret),
    )
    m_load = mocker.patch.object(FakeValidFormat, "load", MagicMock())

    Former(
        src_format=FakeValidFormat,
        target_format=FakeValidFormat,
    )._parse_to_internal(ctx=fake_src_ctx, opt=src_opt)

    act_get_load_args, _ = m_get_laod.call_args
    act_load_args, _ = m_load.call_args

    # get_load_kwargs must be called currect argument.
    assert m_get_laod.call_count == 1
    assert act_get_load_args[0] == fake_src_ctx
    assert act_get_load_args[1] == src_opt
    # load must be called currect argument.
    assert m_load.call_count == 1
    assert act_load_args[0] == fake_get_load_kwargs_ret


def test_parse_from_internal(mocker):

    mocker.patch(f"{MODULE_PATH}._read_file")
    mocker.patch(f"{MODULE_PATH}._parse_to_internal")
    mocker.patch(f"{MODULE_PATH}._write_file")

    fake_internal = {"key1": "value1", "key2": "value2", "key3": "value3"}
    target_opt = {"indent": 1, "parse_int": float}
    fake_get_dump_kwargs_ret = "{key1:value1,key2:value2}"

    m_get_dump = mocker.patch.object(
        FakeValidFormat,
        "get_dump_kwargs",
        MagicMock(return_value=fake_get_dump_kwargs_ret),
    )
    m_dump = mocker.patch.object(FakeValidFormat, "dump", MagicMock())

    Former(
        src_format=FakeValidFormat,
        target_format=FakeValidFormat,
    )._parse_from_internal(internal=fake_internal, opt=target_opt)

    act_get_dump_args, _ = m_get_dump.call_args
    act_dump_args, _ = m_dump.call_args

    # get_dump_kwargs must be called currect argument.
    assert m_get_dump.call_count == 1
    assert act_get_dump_args[0] == fake_internal
    assert act_get_dump_args[1] == target_opt
    # load must be called currect argument.
    assert m_dump.call_count == 1
    assert act_dump_args[0] == fake_get_dump_kwargs_ret

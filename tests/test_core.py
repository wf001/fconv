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
    Whether function calling inner Former().form() was current.
    """

    m_read = mocker.patch(f"{MODULE_PATH}._read_file")
    m_to = mocker.patch(f"{MODULE_PATH}._to_internal")
    m_from = mocker.patch(f"{MODULE_PATH}._from_internal")
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
    Raise exception when source format or target format isn't
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


def test_to_internal(mocker):

    mocker.patch(f"{MODULE_PATH}._read_file")
    mocker.patch(f"{MODULE_PATH}._from_internal")
    mocker.patch(f"{MODULE_PATH}._write_file")
    ctx1 = "{key1:value1,key2:value2}"
    opt = {"indent": 1, "parse_int": float}
    ctx2 = {"key1": "value1", "key2": "value2", "key3": "value3"}
    m_gen_in = mocker.patch.object(
        FakeValidFormat, "gen_input_kwargs", MagicMock(return_value=ctx2)
    )
    m_load = mocker.patch.object(FakeValidFormat, "load", MagicMock())

    Former(
        src_format=FakeValidFormat,
        target_format=FakeValidFormat,
    )._to_internal(ctx=ctx1, opt=opt)

    act_called_args1, _ = m_gen_in.call_args
    act_called_args2, _ = m_load.call_args
    assert m_gen_in.call_count == 1
    assert act_called_args1[0] == ctx1
    assert act_called_args1[1] == opt
    assert m_load.call_count == 1
    assert act_called_args2[0] == ctx2


def test_from_internal(mocker):

    mocker.patch(f"{MODULE_PATH}._read_file")
    mocker.patch(f"{MODULE_PATH}._to_internal")
    mocker.patch(f"{MODULE_PATH}._write_file")
    ctx1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
    ctx2 = "{key1:value1,key2:value2}"
    opt = {"indent": 1, "parse_int": float}
    m_gen_out = mocker.patch.object(
        FakeValidFormat, "gen_output_kwargs", MagicMock(return_value=ctx2)
    )
    m_dump = mocker.patch.object(FakeValidFormat, "dump", MagicMock())

    Former(
        src_format=FakeValidFormat,
        target_format=FakeValidFormat,
    )._from_internal(internal=ctx1, opt=opt)

    act_called_args1, _ = m_gen_out.call_args
    act_called_args2, _ = m_dump.call_args
    assert m_gen_out.call_count == 1
    assert act_called_args1[0] == ctx1
    assert act_called_args1[1] == opt
    assert m_dump.call_count == 1
    assert act_called_args2[0] == ctx2

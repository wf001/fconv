from src.former import Former
from unittest.mock import MagicMock
from src.format import AbstractFormat
import pytest
import json


class TestConcreteFormat(AbstractFormat):
    def load(self, str: str) -> dict:
        pass

    def dump(self, internal: dict) -> str:
        pass

    def _gen_input_kwargs(self, ctx, opt, k):
        pass

    def _gen_output_kwargs(self, ctx, opt):
        pass


class TestInvalidFormat:
    pass


class TestFormerUnit:

    @pytest.mark.parametrize('Former, get_called, send_called', [
        (
            Former(
                src_format=TestConcreteFormat,
                target_format=TestConcreteFormat,
                src_path='dummy_in.json',
                target_path='dymmy_out.yaml'
            ),
            True,
            True
        ),
        (
            Former(
                src_format=TestConcreteFormat,
                target_format=TestConcreteFormat,
                target_path='dymmy_out.yaml'
            ),
            False,
            True
        ),
        (
            Former(
                src_format=TestConcreteFormat,
                target_format=TestConcreteFormat,
                src_path='dummy_in.json'
            ),
            True,
            False
        ),
        (
            Former(
                src_format=TestConcreteFormat,
                target_format=TestConcreteFormat
            ),
            False,
            False
        )

    ])
    def test_form(
            self,
            mocker,
            Former,
            get_called,
            send_called
    ):
        """
        Whether function calling inner Former().form() was current.
        """

        m_get = mocker.patch('src.former.Former._read_file')
        m_to = mocker.patch('src.former.Former._to_internal')
        m_from = mocker.patch('src.former.Former._from_internal')
        m_send = mocker.patch('src.former.Former._write_file')
        Former.form()
        assert m_get.called is get_called
        assert m_to.called is True
        assert m_from.called is True
        assert m_send.called is send_called

    @pytest.mark.parametrize('src_format, target_format', [
        (TestInvalidFormat, TestConcreteFormat),
        (TestConcreteFormat, TestInvalidFormat),
        (TestInvalidFormat, TestInvalidFormat),
    ])
    def test_init_handle_invalid_format(
            self,
            mocker,
            src_format,
            target_format
    ):
        """
        Raise exception when source format or target format isn't
        concrete class of AbstractFormat
        """
        in_name = 'dummy.json'
        out_name = 'dummy.yaml'

        with pytest.raises(ValueError) as e:
            Former(
                src_format=src_format,
                target_format=target_format,
                src_path=in_name,
                target_path=out_name
            )
        assert str(e.value).startswith("Invalid format. expect")

    def test_to_internal(self, mocker):
        in_name = 'dummy.json'
        out_name = 'dummy.yaml'

        mocker.patch('src.former.Former._read_file')
        mocker.patch('src.former.Former._from_internal')
        mocker.patch('src.former.Former._write_file')
        ctx1 = '{key1:value1,key2:value2}'
        opt = {'indent': 1, 'parse_int': float}
        ctx2 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        m_gen_in = mocker.patch.object(
            TestConcreteFormat,
            '_gen_input_kwargs',
            MagicMock(return_value=ctx2)
        )
        m_load = mocker.patch.object(
            TestConcreteFormat,
            'load',
            MagicMock()
        )

        Former(
            src_format=TestConcreteFormat,
            target_format=TestConcreteFormat,
        )._to_internal(ctx=ctx1, opt=opt)

        assert m_gen_in.called_once
        assert m_gen_in.call_args[0][0] == ctx1
        assert m_gen_in.call_args[0][1] == opt
        assert m_load.called_once
        assert m_load.call_args[0][0] == ctx2

    def test_from_internal(self, mocker):
        in_name = 'dummy.json'
        out_name = 'dummy.yaml'

        mocker.patch('src.former.Former._read_file')
        mocker.patch('src.former.Former._to_internal')
        mocker.patch('src.former.Former._write_file')
        ctx1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        ctx2 = '{key1:value1,key2:value2}'
        opt = {'indent': 1, 'parse_int': float}
        m_gen_out = mocker.patch.object(
            TestConcreteFormat,
            '_gen_output_kwargs',
            MagicMock(return_value=ctx2)
        )
        m_dump = mocker.patch.object(
            TestConcreteFormat,
            'dump',
            MagicMock()
        )

        Former(
            src_format=TestConcreteFormat,
            target_format=TestConcreteFormat,
        )._from_internal(internal=ctx1, opt=opt)

        assert m_gen_out.called_once
        assert m_gen_out.call_args[0][0] == ctx1
        assert m_gen_out.call_args[0][1] == opt
        assert m_dump.called_once
        assert m_dump.call_args[0][0] == ctx2


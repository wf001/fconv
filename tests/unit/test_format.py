from unittest.mock import MagicMock

import pytest

from former.format import AbstractFormat, Format


class TestFormatUnit:
    class TestJson:
        def test_load(self, mocker):
            m_loads = mocker.patch("json.loads")
            src_ctx = {"a": "b"}
            Format.Json().load(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_handle_load(self, mocker):
            mocker.patch("json.loads").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Format.Json().load(src_ctx)

        def test_dump(self, mocker):
            m_loads = mocker.patch("json.dumps")
            src_ctx = {"a": "b"}
            Format.Json().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_handle_dump(self, mocker):
            mocker.patch("json.dump").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Format.Json().dump(src_ctx)

        def test_gen_input_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                AbstractFormat, "gen_input_kwargs", MagicMock()
            )
            Format.Json()._gen_input_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

        def test_gen_output_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                AbstractFormat, "gen_output_kwargs", MagicMock()
            )
            Format.Json()._gen_output_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

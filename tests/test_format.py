from unittest.mock import MagicMock

import pytest

from former.format import BaseFormat, Json


class TestFormatUnit:
    class TestJson:
        def test_load(self, mocker):
            m_loads = mocker.patch("json.loads")
            src_ctx = {"a": "b"}
            Json().load(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_load_handle_error(self, mocker):
            mocker.patch("json.loads").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Json().load(src_ctx)

        def test_dump(self, mocker):
            m_loads = mocker.patch("json.dumps")
            src_ctx = {"a": "b"}
            Json().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_dump_handle_error(self, mocker):
            mocker.patch("json.dump").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Json().dump(src_ctx)

        def test_gen_input_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseFormat, "gen_input_kwargs", MagicMock()
            )
            Json().gen_input_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

        def test_gen_output_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseFormat, "gen_output_kwargs", MagicMock()
            )
            Json().gen_output_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

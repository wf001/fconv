from unittest.mock import MagicMock

import pytest

from former.formats.base import BaseDictionalizeFormat
from former.formats.json import Json
from former.formats.yaml import Yaml


class TestFormatsUnit:
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

        def test_get_load_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_load_kwargs", MagicMock()
            )
            Json().get_load_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

        def test_get_dump_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_dump_kwargs", MagicMock()
            )
            Json().get_dump_kwargs({}, {})
            assert m_super_gen_input.call_count == 1

    class TestYaml:
        def test_load(self, mocker):
            m_loads = mocker.patch("yaml.safe_load")
            src_ctx = {"a": "b"}
            Yaml().load(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_load_handle_error(self, mocker):
            mocker.patch("yaml.safe_load").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Yaml().load(src_ctx)

        def test_dump(self, mocker):
            m_loads = mocker.patch("yaml.dump")
            src_ctx = {"a": "b"}
            Yaml().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_dump_handle_error(self, mocker):
            mocker.patch("yaml.dump").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Yaml().dump(src_ctx)

        def test_get_load_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_load_kwargs", MagicMock()
            )
            Yaml().get_load_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

        def test_get_dump_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_dump_kwargs", MagicMock()
            )
            Yaml().get_dump_kwargs({}, {})
            assert m_super_gen_input.call_count == 1

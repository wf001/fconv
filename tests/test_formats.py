from unittest.mock import MagicMock

import pytest

from fconv.formats.base import BaseDictionalizeFormat
from fconv.formats.json import Json
from fconv.formats.toml import Toml
from fconv.formats.xml import Xml
from fconv.formats.yaml import Yaml


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

    class TestToml:
        def test_load(self, mocker):
            m_loads = mocker.patch("toml.loads")
            src_ctx = {"a": "b"}
            Toml().load(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_load_handle_error(self, mocker):
            mocker.patch("toml.loads").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Toml().load(src_ctx)

        def test_dump(self, mocker):
            m_loads = mocker.patch("toml.dumps")
            src_ctx = {"a": "b"}
            Toml().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_dump_handle_error(self, mocker):
            mocker.patch("toml.dumps").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Toml().dump(src_ctx)

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
            Toml().get_dump_kwargs({}, {})
            assert m_super_gen_input.call_count == 1

    class TestXml:
        def test_load(self, mocker):
            m_loads = mocker.patch("xmltodict.parse")
            src_ctx = {"a": "b"}
            Xml().load(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"a": "b"}

        def test_load_handle_error(self, mocker):
            mocker.patch("xmltodict.parse").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Xml().load(src_ctx)

        def test_dump(self, mocker):
            m_loads = mocker.patch("xmltodict.unparse")
            src_ctx = {"input_dict": "b"}
            Xml().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"input_dict": {"root": "b"}, "pretty": True}

        def test_dump_with_disable_pretty(self, mocker):
            m_loads = mocker.patch("xmltodict.unparse")
            src_ctx = {"input_dict": "b", "pretty": False}
            Xml().dump(src_ctx)

            _, act_called_kwargs = m_loads.call_args
            assert m_loads.called
            assert act_called_kwargs == {"input_dict": {"root": "b"}, "pretty": False}

        def test_dump_handle_error(self, mocker):
            mocker.patch("xmltodict.unparse").side_effect = Exception()
            src_ctx = {"a": "b"}

            with pytest.raises(Exception):
                Xml().dump(src_ctx)

        def test_get_load_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_load_kwargs", MagicMock()
            )
            Xml().get_load_kwargs("ctx", {})
            assert m_super_gen_input.call_count == 1

        def test_get_dump_kwargs(self, mocker):
            m_super_gen_input = mocker.patch.object(
                BaseDictionalizeFormat, "get_dump_kwargs", MagicMock()
            )
            Xml().get_dump_kwargs({}, {})
            assert m_super_gen_input.call_count == 1

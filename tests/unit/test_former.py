from src.former import Former, Format, AbstractFormat
import pytest


class TestConcreteFormat(AbstractFormat):
    def load(self, str: str) -> dict:
        pass

    def dump(self, internal: dict) -> str:
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

        m_get = mocker.patch('src.former.Former._get_input')
        m_to = mocker.patch('src.former.Former._to_internal')
        m_from = mocker.patch('src.former.Former._from_internal')
        m_send = mocker.patch('src.former.Former._send_output')
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
        assert str(e.value) == "Invalid format. expect: [JSON, YAML]"

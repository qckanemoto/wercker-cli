import mock

from werckercli.commands import clearsettings

from werckercli.tests import TempHomeSettingsCase


class ClearClearSettingsTests(TempHomeSettingsCase):

    template_name = "home-with-netrc"

    @mock.patch("clint.textui.puts", mock.Mock())
    @mock.patch("werckercli.config.get_value",
                mock.Mock(return_value="data"))
    @mock.patch("clint.textui.puts",
                mock.Mock())
    @mock.patch("werckercli.prompt.yn",
                mock.Mock(return_value=True))
    def test_clear(self):
        my_clearsettings = reload(clearsettings)
        with mock.patch(
            "werckercli.config.set_value",
            mock.Mock()
        ) as set_value:
            from werckercli.config import VALUE_USER_TOKEN

            my_clearsettings.clear_settings()
            set_value.assert_called_once_with(VALUE_USER_TOKEN, None)


class NoClearClearSettingsTests(TempHomeSettingsCase):
    @mock.patch("clint.textui.puts", mock.Mock())
    @mock.patch("werckercli.config.get_value",
                mock.Mock(return_value="data"))
    @mock.patch("clint.textui.puts",
                mock.Mock())
    @mock.patch("werckercli.prompt.yn",
                mock.Mock(return_value=False))
    def test_NO_clear(self):
        with mock.patch(
            "werckercli.config.set_value",
            mock.Mock()
        ) as set_value:

            # my_clearsettings = reload(clearsettings)
            my_clearsettings = clearsettings

            my_clearsettings.clear_settings()
            self.assertEqual(0, set_value.call_count)

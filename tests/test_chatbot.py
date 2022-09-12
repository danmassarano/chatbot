"""test_cahtbot runs integration tests on chatbot."""
import io
import os
import sys
import unittest

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "chatbot")
sys.path.append(SOURCE_PATH)

from chatbot.chatbot import main  # noqa: E402


class TestChatbot(unittest.TestCase):
    """
    Runs tests on the chatbot package.

    Methods
    -------
    test_main():
        Test that run_chatbot is running and returning results.

    """

    @unittest.skipUnless(
        os.getenv("TWITTER_BEARER_TOKEN") is not None,
        "Requires twitter API key",
    )
    def test_main(self):
        """Test that chatbot is running and returning results."""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main(["--username", "edthewlis"])
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue().split("\n")

        self.assertIsNotNone(output[-4])
        self.assertIsNotNone(output[-3])
        self.assertIsNotNone(output[-2])

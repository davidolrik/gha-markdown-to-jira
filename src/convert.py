from io import StringIO

import mistletoe
from jira_renderer import JIRARenderer
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_prefix = "INPUT_"

    MARKDOWN: str


settings = Settings()

with StringIO(settings.MARKDOWN) as in_file:
    jira_formatted_text: str = mistletoe.markdown(in_file, JIRARenderer)

    jira_formatted_text = jira_formatted_text.replace("%", "%25")
    jira_formatted_text = jira_formatted_text.replace("\n", "%0A")
    jira_formatted_text = jira_formatted_text.replace("\r", "%0D")

    print(f"::set-output name=jira-text::{jira_formatted_text}")

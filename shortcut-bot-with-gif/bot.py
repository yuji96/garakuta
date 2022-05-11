from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os
import twitter

load_dotenv()

api = twitter.Api(consumer_key=os.environ["consumer_key"],
                  consumer_secret=os.environ["consumer_secret"],
                  access_token_key=os.environ["access_token_key"],
                  access_token_secret=os.environ["access_token_secret"])

template = Environment(loader=FileSystemLoader(".")).get_template("template.j2")

data, *_ = pd.read_csv("database.csv").sample().T.to_dict().values()

api.PostUpdate(
    template.render(**data),
    media=f"screenrecord/{path}.gif" if (path := data.get("path")) else None,
)

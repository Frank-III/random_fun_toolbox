import os
import sys
from pprint import pprint
import json
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")

while NOTION_TOKEN == "":
    print("NOTION_TOKEN not found.")
    NOTION_TOKEN = input("Enter your integration token: ").strip()

notion = Client(auth=NOTION_TOKEN)

"""
ToDo:
when try to determine which page to append blocks:
1. query database using `notion.databases.query` with params:
    **{"database_id": database_id
    "filter":{
        "property":"Name",
        "title":{
            "equals": page_name
        }
    }
    }
2. do some extraction to extract the page name

3. using `notion.blocks.children.list` to get the children of page's blocks with param: page_id

4. using recursion to get the children of `Problem to focus on page`

5. add new focus problem using template 
"""
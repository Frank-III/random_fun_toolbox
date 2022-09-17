from ast import Str
import os
import sys
from pprint import pprint
import json
from typing import Dict
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")

while NOTION_TOKEN == "":
    print("NOTION_TOKEN not found.")
    NOTION_TOKEN = input("Enter your integration token: ").strip()

"""
ToDo:
1. TheGitNotion Client interface
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

2. The ContentParser interface
    1. when title content include inline code, should parse into inline code format.
    
    2. when adding heading format or other format parse according corresponding dict template respectively.
    


3. other generic call to notion api should just use self.notion.xxx 
"""

class MyGitNotion:
    def __init__(self, contentparser= NotionContentParser(), **kwargs) -> None:
        self.notion = Client(auth=NOTION_TOKEN)
        self.database_id = os.getenv("database_id", "")
        self.database_pages = {}
        self.contentparser = contentparser
        # self.blocks = None

    def get_page(self, name: str) -> Dict:
        self.database_pages["name"] = self.notion.databases.query(
        **{
            "database_id": self.database_id,
            "filter": {
                "property": "Name",
                "title":{
                    "equals": name,
                    },
            },
        }) 
        return self.database_pages["name"]

    def get_page_id(self, name: str) -> str:
        if name in self.database_pages.keys():
            return (self.database_pages[name]["results"][0]["url"]).split("-")[-1]
        else:
            return (self.get_page(name)["results"][0]["url"]).split("-")[-1]

    def get_page_children(self, name):
        return self.notion.blocks.children(self.get_page_id(name))

    def append_page_block(self, name, content, code=None):
        parsed_res = self.contentparser.parse(content, code=code)
        self.notion.blocks.append(self.get_page_id(name), children=parsed_res)


class NotionContentParser:
    pass






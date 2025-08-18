#!/usr/bin/env python3
"""
Bootstrap Notion workspace with Tracks and Tasks databases and import CSV data.

Usage:
  python notion-bootstrap.py --parent <PARENT_PAGE_ID> \
    --tracks_csv "/absolute/path/to/notion-import-tracks.csv" \
    --tasks_csv "/absolute/path/to/notion-import-tasks.csv"

Requires env var NOTION_TOKEN to be set to a Notion Internal Integration Token.
"""

import os
import sys
import csv
import time
import json
import argparse
from typing import Dict, Any, List, Optional

import requests


NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


class NotionClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("NOTION_TOKEN")
        if not self.token:
            print("Error: NOTION_TOKEN environment variable not set")
            sys.exit(1)
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def create_database(self, parent_page_id: str, title: str, properties: Dict[str, Any]) -> str:
        payload = {
            "parent": {"type": "page_id", "page_id": parent_page_id},
            "title": [
                {
                    "type": "text",
                    "text": {"content": title},
                }
            ],
            "properties": properties,
        }
        resp = requests.post(f"{BASE_URL}/databases", headers=self.headers, data=json.dumps(payload))
        if resp.status_code >= 400:
            print(f"Failed to create database '{title}': {resp.status_code} {resp.text}")
            sys.exit(1)
        data = resp.json()
        return data["id"]

    def create_page(self, database_id: str, properties: Dict[str, Any]):
        payload = {"parent": {"database_id": database_id}, "properties": properties}
        resp = requests.post(f"{BASE_URL}/pages", headers=self.headers, data=json.dumps(payload))
        if resp.status_code >= 400:
            print(f"Failed to create page: {resp.status_code} {resp.text}")
            sys.exit(1)
        return resp.json()

    def query_database_by_title(self, parent_page_id: str, title: str) -> Optional[str]:
        # Notion API doesn't support list databases by parent easily; use search as fallback
        payload = {"query": title, "filter": {"value": "database", "property": "object"}}
        resp = requests.post(f"{BASE_URL}/search", headers=self.headers, data=json.dumps(payload))
        if resp.status_code >= 400:
            return None
        for res in resp.json().get("results", []):
            if res.get("object") == "database":
                # Database titles are rich text array
                title_rt = res.get("title", [])
                db_title = "".join([t.get("plain_text", "") for t in title_rt])
                if db_title.strip() == title.strip():
                    return res.get("id")
        return None


def tracks_properties() -> Dict[str, Any]:
    return {
        "Track Name": {"title": {}},
        "Type": {
            "select": {
                "options": [
                    {"name": "Strategic", "color": "red"},
                    {"name": "Operational", "color": "blue"},
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "Planning", "color": "gray"},
                    {"name": "Active", "color": "green"},
                    {"name": "On Hold", "color": "yellow"},
                    {"name": "Completed", "color": "green"},
                ]
            }
        },
        "Priority": {
            "select": {
                "options": [
                    {"name": "High", "color": "red"},
                    {"name": "Medium", "color": "yellow"},
                    {"name": "Low", "color": "green"},
                ]
            }
        },
        "Owner": {"multi_select": {}},
        "Start Date": {"date": {}},
        "End Date": {"date": {}},
        "Description": {"rich_text": {}},
    }


def tasks_properties(tracks_db_id: str) -> Dict[str, Any]:
    return {
        "Task Name": {"title": {}},
        "Related Track": {
            "relation": {
                "database_id": tracks_db_id,
                "type": "single_property",
                "single_property": {}
            }
        },
        "Type": {
            "select": {
                "options": [
                    {"name": "Strategic", "color": "red"},
                    {"name": "Operational", "color": "blue"},
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "Backlog", "color": "gray"},
                    {"name": "In Progress", "color": "blue"},
                    {"name": "Review", "color": "yellow"},
                    {"name": "Done", "color": "green"},
                ]
            }
        },
        "Priority": {
            "select": {
                "options": [
                    {"name": "High", "color": "red"},
                    {"name": "Medium", "color": "yellow"},
                    {"name": "Low", "color": "green"},
                ]
            }
        },
        "Assignee": {"multi_select": {}},
        "Due Date": {"date": {}},
        "Sprint Week": {"rich_text": {}},
        "Tags": {"multi_select": {}},
        "Effort": {"number": {"format": "number"}},
        "Description": {"rich_text": {}},
        "Notes": {"rich_text": {}},
    }


def split_multiselect(value: str) -> List[str]:
    if not value:
        return []
    # Split by common separators and clean
    separators = ["+", "/", ",", "&", " and "]
    tmp = [value]
    for sep in separators:
        nxt: List[str] = []
        for part in tmp:
            nxt.extend(part.split(sep))
        tmp = nxt
    return [p.strip() for p in tmp if p.strip()]


def num_from_effort(value: str) -> Optional[float]:
    if not value:
        return None
    # Extract leading number
    digits = ""
    for ch in value:
        if ch.isdigit() or ch == ".":
            digits += ch
        elif digits:
            break
    try:
        return float(digits) if digits else None
    except ValueError:
        return None


def import_tracks(notion: NotionClient, db_id: str, csv_path: str) -> Dict[str, str]:
    name_to_page: Dict[str, str] = {}
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("Track Name", "").strip()
            if not name:
                continue
            props: Dict[str, Any] = {
                "Track Name": {"title": [{"type": "text", "text": {"content": name}}]},
            }
            if row.get("Type"):
                props["Type"] = {"select": {"name": row["Type"].strip()}}
            if row.get("Status"):
                props["Status"] = {"select": {"name": row["Status"].strip()}}
            if row.get("Priority"):
                props["Priority"] = {"select": {"name": row["Priority"].strip()}}
            owners = split_multiselect(row.get("Owner", ""))
            if owners:
                props["Owner"] = {"multi_select": [{"name": o} for o in owners]}
            if row.get("Description"):
                props["Description"] = {"rich_text": [{"type": "text", "text": {"content": row["Description"]}}]}
            if row.get("Start Date"):
                props["Start Date"] = {"date": {"start": row["Start Date"].strip()}}
            if row.get("End Date"):
                props["End Date"] = {"date": {"start": row["End Date"].strip()}}

            page = notion.create_page(db_id, props)
            name_to_page[name] = page.get("id")
            # Be gentle on API
            time.sleep(0.2)
    return name_to_page


def import_tasks(notion: NotionClient, db_id: str, track_name_to_page: Dict[str, str], csv_path: str):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("Task Name", "").strip()
            if not name:
                continue
            props: Dict[str, Any] = {
                "Task Name": {"title": [{"type": "text", "text": {"content": name}}]},
            }

            # Relation to Track
            rel_track_name = row.get("Related Track", "").strip()
            if rel_track_name and rel_track_name in track_name_to_page:
                props["Related Track"] = {"relation": [{"id": track_name_to_page[rel_track_name]}]}

            # Selects
            if row.get("Type"):
                props["Type"] = {"select": {"name": row["Type"].strip()}}
            if row.get("Status"):
                props["Status"] = {"select": {"name": row["Status"].strip()}}
            if row.get("Priority"):
                props["Priority"] = {"select": {"name": row["Priority"].strip()}}

            # Multi-selects
            assignees = split_multiselect(row.get("Assignee", ""))
            if assignees:
                props["Assignee"] = {"multi_select": [{"name": a} for a in assignees]}
            tags = split_multiselect(row.get("Tags", ""))
            if tags:
                props["Tags"] = {"multi_select": [{"name": t} for t in tags]}

            # Dates & numbers
            if row.get("Due Date"):
                props["Due Date"] = {"date": {"start": row["Due Date"].strip()}}
            if row.get("Sprint Week"):
                props["Sprint Week"] = {"rich_text": [{"type": "text", "text": {"content": row["Sprint Week"].strip()}}]}
            effort_val = num_from_effort(row.get("Effort", ""))
            if effort_val is not None:
                props["Effort"] = {"number": effort_val}

            # Texts
            if row.get("Description"):
                props["Description"] = {"rich_text": [{"type": "text", "text": {"content": row["Description"]}}]}

            notion.create_page(db_id, props)
            time.sleep(0.2)


def main():
    parser = argparse.ArgumentParser(description="Bootstrap Notion DBs and import CSV data")
    parser.add_argument("--parent", required=True, help="Parent Notion page ID (32-char without dashes)")
    parser.add_argument("--tracks_csv", required=True, help="Absolute path to tracks CSV")
    parser.add_argument("--tasks_csv", required=True, help="Absolute path to tasks CSV")
    args = parser.parse_args()

    notion = NotionClient()

    # Create or reuse databases
    tracks_title = "📋 Task Tracks"
    tasks_title = "✅ Task Management"

    existing_tracks_db_id = notion.query_database_by_title(args.parent, tracks_title)
    if existing_tracks_db_id:
        tracks_db_id = existing_tracks_db_id
        print(f"Found existing Tracks DB: {tracks_db_id}")
    else:
        print("Creating Tracks database...")
        tracks_db_id = notion.create_database(args.parent, tracks_title, tracks_properties())
        print(f"Tracks DB created: {tracks_db_id}")

    existing_tasks_db_id = notion.query_database_by_title(args.parent, tasks_title)
    if existing_tasks_db_id:
        tasks_db_id = existing_tasks_db_id
        print(f"Found existing Tasks DB: {tasks_db_id}")
    else:
        print("Creating Tasks database...")
        tasks_db_id = notion.create_database(args.parent, tasks_title, tasks_properties(tracks_db_id))
        print(f"Tasks DB created: {tasks_db_id}")

    # Import data
    print("Importing Tracks from CSV...")
    track_name_to_page = import_tracks(notion, tracks_db_id, args.tracks_csv)
    print(f"Imported {len(track_name_to_page)} tracks")

    print("Importing Tasks from CSV...")
    import_tasks(notion, tasks_db_id, track_name_to_page, args.tasks_csv)
    print("Tasks import completed")


if __name__ == "__main__":
    main()


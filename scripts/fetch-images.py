#!/usr/bin/env python3
"""Download project images listed in content/projects.json into assets/images/.

Run this once network access to images.squarespace-cdn.com is available
(e.g. from a session whose environment network policy allows it):

    python3 scripts/fetch-images.py
"""
import json
import os
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS_FILE = os.path.join(ROOT, "content", "projects.json")


def main():
    with open(PROJECTS_FILE) as f:
        projects = json.load(f)

    for project in projects:
        for image in project.get("images", []):
            dest = os.path.join(ROOT, image["local_path"])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.exists(dest):
                print(f"skip (exists): {image['local_path']}")
                continue
            print(f"downloading: {image['source_url']} -> {image['local_path']}")
            urllib.request.urlretrieve(image["source_url"], dest)


if __name__ == "__main__":
    main()

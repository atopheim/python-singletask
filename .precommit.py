#!/usr/bin/env python3
import tomli
import subprocess
import sys

with open("pyproject.toml", "rb") as f:
    data = tomli.load(f)

version = data["project"]["version"]
tag_name = f"v{version}"

# 1. Check if tag already exists
check_cmd = subprocess.run(["git", "rev-parse", tag_name],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)

if check_cmd.returncode == 0:
    print(f"Tag {tag_name} already exists. Doing nothing.")
    sys.exit(0)

# 2. Create and push the tag
print(f"Creating and pushing tag {tag_name}...")
subprocess.run(["git", "tag", tag_name], check=True)
subprocess.run(["git", "push", "origin", tag_name], check=True)

print(f"Tag {tag_name} successfully pushed!")

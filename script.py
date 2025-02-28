import re
import os
import json
import shutil

acceptable_tags = [
    "USA",
    "Japan",
    "World",
    "Europe",
]

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"


def get_rom_title(rom_name):
    title = re.split(r"\s*\(.*?\)", rom_name, maxsplit=1)[0].strip()
    return title


def get_rom_tags(rom_name):
    tag_pattern = re.compile(r"\(([^)]+)\)")
    matches = tag_pattern.findall(rom_name)

    tags = [tag.strip() for match in matches
            for tag in match.split(",")
            if len(tag.strip()) != 2]
    return tags


for file in os.listdir("."):
    if not os.path.isfile(file):
        continue

    base_name = os.path.basename(file)

    rom_title = get_rom_title(base_name)
    rom_tags = get_rom_tags(base_name)

    reasons = []

    if "USA" not in rom_tags:
        reasons.append("needs USA tag")

    for tag in rom_tags:
        if tag not in acceptable_tags:
            reasons.append("unknown tag: " + tag)

    info = {
        "base_name": base_name,
        "rom_title": rom_title,
        "rom_tags": rom_tags,
        "reasons": reasons,
    }

    if reasons:
        current_folder = os.path.basename(os.getcwd())
        parent_folder = os.path.dirname(os.getcwd())
        pruned_folder = os.path.join(
            parent_folder, f"{current_folder} (Pruned)")

        print(json.dumps(info, indent=4))

        if DRY_RUN:
            print(f"[DRY_RUN] Moving: {base_name} -> {pruned_folder}")
        else:
            print(f"Moving: {base_name} -> {pruned_folder}")

            os.makedirs(pruned_folder, exist_ok=True)

            shutil.move(base_name, os.path.join(pruned_folder, base_name))

print("success!")

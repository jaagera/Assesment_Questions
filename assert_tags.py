original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]

changed["tags"].append("another_tag")
assert original["tags"] == ["python"]
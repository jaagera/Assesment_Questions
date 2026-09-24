def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"].copy()
    updated["tags"].append(tag)
    return updated
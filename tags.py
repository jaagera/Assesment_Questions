def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"] + [tag]
    return updated
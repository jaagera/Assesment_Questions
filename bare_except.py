def summarise_amounts(raw_values):
    total = 0
    for raw in raw_values:
        try:
            total += int(raw)
        except:
            pass
    return {"total": total, "rejected": 0}
print(return)
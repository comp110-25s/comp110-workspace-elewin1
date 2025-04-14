def count_regs(county: str, list_all: list[str]) -> int:
    count: int = 0
    i: int = 0
    while i < (len(list_all)):
        if list_all[i] == county:
            count += 1
        i += 1
    return count


print(count_regs("lee", ["wake", "orange", "lee", "lee"]))
print(words)

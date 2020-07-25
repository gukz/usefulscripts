from collections import defaultdict


def show_foods(orders):
    "返回每个桌子的菜品销量情况"
    table_foods = dict()
    all_foods = set()
    for order in orders:
        table, food = order[1], order[2]
        if table not in table_foods:
            table_foods[table] = defaultdict(int)
        table_foods[table][food] += 1
        all_foods.add(food)
    res = []
    all_foods = sorted(list(all_foods))
    for table in sorted(table_foods.keys(), key=lambda a: int(a)):
        line = [table]
        for food in all_foods:
            line.append(str(table_foods[table][food]))
        res.append(line)
    head = ["Table"]
    for food in all_foods:
        head.append(food)
    res.insert(0, head)
    return res


if __name__ == "__main__":
    inp = [
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Rous", "3", "Ceviche"],
        ["Carla", "5", "Ceviche"],
        ["Carla", "5", "Water ever"],
    ]
    res = [
        ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water ever"],
        ["3", "0", "2", "1", "0"],
        ["5", "0", "1", "0", "1"],
        ["10", "1", "0", "0", "0"],
    ]
    assert res == show_foods(inp)

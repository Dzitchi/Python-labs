def find_common_participants(group1, group2, div=','):
    group1_split = set(group1.split(div))
    group2_split = group2.split(div)
    com_part = list(group1_split.intersection(group2_split))

    return com_part


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

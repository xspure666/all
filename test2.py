names_list = ["Washington", "Trump", "Obama", "bush", "Clinton", "Reagan"]
l1 = [name for name in names_list if name.startswith('W')]
l2 = [name for name in names_list if name.startswith('W') or len(name) < 5]
l3 = [name for name in names_list if len(name) < 5 and name.islower()]
print(l1, l2, l3)

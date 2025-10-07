dict_1 = {'ID': '5', 'Task': 'After reviewing the original question and the thoughts of previous agents, what is the final answer to the question?', 'Difficulty': '5', 'Token': '50', 'Rely': '4', 'Result': None}

Rely = [i.strip() for i in dict_1['Rely'].split(',')] if 'Rely' in dict_1 else []
for i in Rely:
    if int(i) >= int(dict_1['ID']):
        Rely = [j for j in range(1, int(dict_1['ID']))]
    if str(int(dict_1['ID']) - 1) in Rely:
        Rely = [j for j in range(1, int(dict_1['ID']))]
Rely = ','.join(str(i) for i in Rely)
print(Rely)
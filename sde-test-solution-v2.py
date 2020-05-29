import json

output_dic = dict()


with open("./sample_input.json") as file:
    load_dict = json.load(file)

    # # create c or g bond dic
    # c_bond_list = []
    # g_bond_list = []
    for bond_type in load_dict['data']:
        if bond_type['id'].startswith('c'):
            # check if there's any null value
            if None not in bond_type.values():



# print(c_bond_list)
# print(g_bond_list)

output_dic = dict()

for c_bond in c_bond_list:
    tenor_str = c_bond['tenor']
    tenor = ''.join((ch if ch in '0123456789.' else ' ') for ch in tenor_str)
    for g_bond in g_bond_list:
        #create a gid - tenor_diff dic:
        
        

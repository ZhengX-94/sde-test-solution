import json


output = {'data':[]}  
with open("./sample_input_2.json") as file:
    load_dict = json.load(file)

    # create c or g bond dic
    c_bond_list = []
    g_bond_list = []
    for bond_type in load_dict['data']:
        if bond_type['id'].startswith('c'):
            # check if there's any null value
            if None not in bond_type.values():
                c_bond_list.append(bond_type)
        else:
            g_bond_list.append(bond_type)





def str_to_num(tenor_str):
    num_str = ''.join((ch if ch in '0123456789.' else ' ') for ch in tenor_str)
    return float(num_str)


def yield_converter(yield_str):
    num_str = ''.join((ch if ch in '0123456789.' else ' ') for ch in yield_str)
    num_wo_space = num_str.replace(" ", "")
    return int(num_wo_space)


for c_bond in c_bond_list:
    # compare tenor_diff or amount_outstanding for each g_bond
    tenor_diff_min = 100
    output_dic = dict()
    for g_bond in g_bond_list:
        tenor_diff = abs(str_to_num(
            c_bond['tenor']) - str_to_num(g_bond['tenor']))
        if tenor_diff < tenor_diff_min:
            best_g_bond = g_bond
            best_amount = g_bond['amount_outstanding']
            tenor_diff_min = tenor_diff
        # compare amount outstanding if there's tie for tenor_diff
        if tenor_diff == tenor_diff_min:
            if g_bond['amount_outstanding'] > best_amount:
                best_g_bond = g_bond

    # ouput best_g_bond for current c_bond
    output_dic['corporate_bond_id'] = c_bond['id']
    output_dic['government_bond_id'] = best_g_bond['id']
    spread = int(abs(str_to_num(c_bond['yield']) * 100
                     - str_to_num(best_g_bond['yield']) * 100))
    output_dic['spread_to_benchmark'] = str(spread) + ' bps'
    output['data'].append(output_dic)
  


with open("./sample_output_dev.json", "w") as f:
    json.dump(output, f)



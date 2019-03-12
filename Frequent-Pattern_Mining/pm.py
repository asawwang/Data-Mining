import sys
import itertools
import functools

def string_sort(first_pattern, second_pattern):
    if first_pattern[1] == second_pattern[1]:
        first = ''.join(first_pattern[0])
        second = ''.join(second_pattern[0])
        if first == second:
            return 0
        elif first < second:
            return -1
        else:
            return 1
    elif first_pattern[1] < second_pattern[1]:
        return 1
    else:
        return -1

inputs = []
for input_line in sys.stdin:
    inputs.append(input_line.strip())
min_support = 1
min_support = int(inputs[0])
if min_support == 0:
    min_support = 1

transaction_table = {}
transactions = inputs[1:]
for curr_transaction in transactions:
    pattern_list = curr_transaction.split(' ')
    curr_flag = 0
    for p in pattern_list:
        p = (p,)
        curr_flag = 1
        if p not in transaction_table:
            if curr_flag == 1:
                transaction_table[p] = 1
        else:
            transaction_table[p] = transaction_table[p] + 1
frequent_itemsets = {}

frequent_itemsets = {item : support for item, support in transaction_table.items() if support >= min_support}
num_lines = len(frequent_itemsets)
input_range = range(2, num_lines)
frequent_itemsets_ret = frequent_itemsets
for input_idx in input_range:
    sorted_itemsets = sorted(list(frequent_itemsets.keys()))

    candidate_list = []
    curr_length = len(sorted_itemsets[0])
    if curr_length == 1:
        one_item_list = [i[0] for i in sorted_itemsets]
        candidate_list = list(itertools.combinations(one_item_list, 2))
    else:
        s_length = len(sorted_itemsets)
        for i in range(0, s_length - 1):
            j = i + 1
            next_sets = sorted_itemsets[j:]
            curr_set = sorted_itemsets[i]
            for curr_next in next_sets:
                set_range = range(curr_length - 1)
                append_flag = None
                for kk in set_range:
                    if curr_set[kk] != curr_next[kk]:
                        append_flag = None
                    else:
                        append_flag = True
                if append_flag == True:
                    sss = list(curr_set)
                    sss.append(curr_next[curr_length-1])
                    ifreq_flag = False
                    inflen = len(sorted_itemsets[0])
                    for item_in_combin in itertools.combinations(sss, inflen):
                        if item_in_combin not in sorted_itemsets:
                            ifreq_flag = True
                            break
                    if ifreq_flag == True:
                        continue
                    else:
                        candidate_list.append(tuple(sss))
    transaction_table = {}
    for curr_transaction in transactions:
        pattern_list = curr_transaction.split(' ')
        alphabet_order_list = sorted([*pattern_list])
        valid_set = set(itertools.combinations(alphabet_order_list, input_idx))
        candidate_set = set(candidate_list)
        valid_cadidate_list = list(set(candidate_list) & valid_set)
        for vc in valid_cadidate_list:
            if vc not in transaction_table:
                transaction_table[vc] = 1
            else:
                transaction_table[vc] = transaction_table[vc] + 1
        frequent_itemsets = {item : support for item, support in transaction_table.items() if support >= min_support}
        frequent_itemsets_ret.update(frequent_itemsets)

frequent_itemsets_to_print = sorted(frequent_itemsets_ret.items(), key = functools.cmp_to_key(string_sort))

for pattern in frequent_itemsets_to_print:
    formatted = "%s [%s]" % (pattern[1], " ".join(pattern[0]))
    print(formatted)
count = 1
freqent_patterns = frequent_itemsets_ret
temp_set = [t for t in freqent_patterns.keys() if len(t) == 1]
closed_patterns = list(temp_set)
while temp_set:
    count = count + 1
    set_t = [t for t in freqent_patterns.keys() if len(t) == count]
    for pattern in temp_set:
        for curr_pattern in set_t:
            pset = set(pattern)
            currset = set(curr_pattern)
            if pset.issubset(currset) and freqent_patterns[pattern] == freqent_patterns[curr_pattern]:
                    closed_patterns.remove(pattern)
                    break
    temp_set = [t for t in freqent_patterns.keys() if len(t) == count]
    closed_patterns.extend(temp_set)
close_patterns_with_count = {closeitem:freqent_patterns[closeitem] for closeitem in closed_patterns if closeitem in freqent_patterns}
close_to_print = sorted(close_patterns_with_count.items(), key = functools.cmp_to_key(string_sort))
print()
for pattern in close_to_print:
    formatted = "%s [%s]" % (pattern[1], " ".join(pattern[0]))
    print(formatted)

count = 1
freqent_patterns = frequent_itemsets_ret
temp_set = [t for t in freqent_patterns.keys() if len(t) == 1]
max_pattern = list(temp_set)
while temp_set:
    count = count + 1
    set_t = [t for t in freqent_patterns.keys() if len(t) == count]
    for pattern in temp_set:
        for curr_pattern in set_t:
            pset = set(pattern)
            currset = set(curr_pattern)
            if pset.issubset(currset):
                    max_pattern.remove(pattern)
                    break
    temp_set = [t for t in freqent_patterns.keys() if len(t) == count]
    max_pattern.extend(temp_set)
max_patterns_with_count = {maxitem:freqent_patterns[maxitem] for maxitem in max_pattern if maxitem in freqent_patterns}
max_to_print = sorted(max_patterns_with_count.items(), key = functools.cmp_to_key(string_sort))
print()
for pattern in max_to_print:
    formatted = "%s [%s]" % (pattern[1], " ".join(pattern[0]))
    print(formatted)

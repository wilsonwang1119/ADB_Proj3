__author__ = 'youhanwang'

import sys
import csv

def generate_itemsets(input_file, min_sup, min_conf, output_file):
    reader = csv.reader(input_file)
    transactions = []
    for line in reader:
        tran = set(line)
        transactions.append(tran)

    result = [] # list of l1, l2....
    items = set()
    visited = set()
    for transaction in transactions:
        for item in transaction:
            if item not in visited:
                visited.add(item)
                if support(transactions, set([item])) >= min_sup * len(transactions):
                    items.add(frozenset([item]))

    result.append(items)

    while items:
        candidates = apriori_gen(items)
        items = set()
        for candidate in candidates:
            # print candidate , support(transactions, candidate)
            if support(transactions, candidate) >= min_sup * len(transactions):
                items.add(frozenset(candidate))
        result.append(items)

    out_result = []
    for itemsets in result:
        for itemset in itemsets:
            sup = float(support(transactions, itemset)) / len(transactions)
            out_result.append((itemset, sup))

    out_result.sort(key = lambda x : x[1], reverse = True)

    print >> output_file, "==Frequent itemsets(min_sup= %s%%)" % (min_sup * 100)


    for line in out_result:
        print >> output_file, "%s, %s%%" % (list(line[0]), line[1] * 100)
    generate_rules(transactions, result, min_conf, output_file)




def generate_rules(transactions, itemsets, min_conf, output_file):
    result = []
    for itemset in itemsets[1:]:
        for items in itemset:
            for rhs in items:
                lhs = items - set([rhs])
                count_lhs, count_rule = confidence(transactions, lhs, items)
                conf = float(count_rule) / float(count_lhs)
                if conf > min_conf:
                    sup = float(count_rule) / len(transactions)
                    result.append((lhs, rhs, conf, sup))


    result.sort(key = lambda x : x[3], reverse = True)

    print >> output_file, "==High-confidence association rules (min_conf= %s%%)" % (min_conf * 100)
    for line in result:
        print >> output_file, "%s => %s (Conf: %s%%, Supp: %s%%)" % (list(line[0]), [line[1]], line[2] * 100, line[3] * 100)


def confidence(transactions, lhs, rule):
    count1 = 0
    count2 = 0
    for transaction in transactions:
        if lhs <= transaction:
            count1 += 1
            if rule <= transaction:
                count2 += 1

    return count1, count2


def apriori_gen(items):
    new_items = set()
    for item1 in items:
        for item2 in items:
            new_item = item1 ^ item2
            if len(new_item) == 2:
                new_items.add(item1 | item2)

    return new_items




def support(transactions, item):
    count = 0
    for transaction in transactions:
        if item <= transaction:
            count = count + 1

    return count


def usage():
    print """
    Usage:
    python <CSV-Input> <min_sum> <min_conf> <Output>
    <CSV-Input> is the Integrated dataset
    <min_sup>   is the minimum support requirement, range from 0 to 1.0
    <min_conf>  is the minimum confidence requirement, range from 0 to 1.0
    <Output>    is the output file

    Example:
    python input.csv 0.2 0.5 output.txt
    """

if __name__ == "__main__":
    if len(sys.argv) != 5: #Expecting 5 arguments.
        usage()
        exit(2)

    try:
        input = file(sys.argv[1], "r")
    except IOError:
        sys.stderr.write("ERROR: Can't read input file.")

    if float(sys.argv[2]) < 0 or float(sys.argv[2]) > 1 or float(sys.argv[3]) < 0 or float(sys.argv[3]) > 1:
        sys.stderr.write("ERROR: Invalid parameter input.")

    try:
        output = file(sys.argv[4], "w")
    except IOError:
        sys.stderr.write("ERROR: Can't write to output file.")

    generate_itemsets(input, float(sys.argv[2]), float(sys.argv[3]), output)




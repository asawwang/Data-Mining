import sys

"""
Disclaimer: The following decision tree algorithm (class Question, Leaf, Deinision node)
are referenced from https://www.youtube.com/watch?v=LDRbO9a6XPU presented by Google Developers
and https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb, a Jupyter file
created by Google Developers Machine learning totorial
"""

class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        return val == self.value

class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:
    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        values = set([row[col] for row in rows])  # unique values in the column
        for val in values:  # for each value

            question = Question(col, val)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

def build_tree(rows):
    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
    gain, question = find_best_split(rows)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0:
        return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
    true_rows, false_rows = partition(rows, question)

    # Recursively build the true branch.
    true_branch = build_tree(true_rows)

    # Recursively build the false branch.
    false_branch = build_tree(false_rows)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)

def classify(row, node):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def process_traning_data(training_file):
    # print('asdasdasdasds')
    rows = []
    class_table = []
    with open(training_file, 'r') as tf:
        for line in tf:
            single_row = []
            curr_data_line = line.strip().split(' ')
            label = curr_data_line[0]
            for single_attr in curr_data_line[1:]:
                attr = single_attr.split(':')
                attr_val = attr[1]
                single_row.append(attr_val)
            single_row.append(label)
            if label not in class_table:
                class_table.append(label)
            rows.append(single_row)
    return rows, class_table

def majority_voting(prediction_dic):
    best = 0
    result = ''
    for i in prediction_dic:
        single_prediction = prediction_dic[i]
        if single_prediction > best:
            best = single_prediction
            result = i
    return result

def init_confusion_matrix(size):
    confusion_matrix = []
    for i in range(0, size):
        col = []
        for j in range(0, size):
            col.append(0)
        confusion_matrix.append(col)
    return confusion_matrix

def print_matrix(confusion_matrix):
    for i in range(0, len(confusion_matrix)):
        for j in range(0, len(confusion_matrix)):
            if j < (len(confusion_matrix) - 1):
                print(confusion_matrix[i][j], end = ' ')
            else:
                print(confusion_matrix[i][j])


training_file = sys.argv[1]
test_file = sys.argv[2]
rows, class_table = process_traning_data(training_file)
# print(class_table)
# print(len(class_table))
my_tree = build_tree(rows)
confusion_matrix = init_confusion_matrix(len(class_table))
# print(confusion_matrix)
test_rows, temp = process_traning_data(test_file)
count = 0
true = 0
for test_row in test_rows:
    count += 1
    # print(classify(test_row, my_tree), majority_voting(classify(test_row, my_tree)))
    real_class = test_row[-1]
    real_idx = class_table.index(real_class)
    classified_class = majority_voting(classify(test_row, my_tree))
    classified_idx = class_table.index(classified_class)
    confusion_matrix[real_idx][classified_idx] += 1
    if(real_class == classified_class):
        true += 1
# print(true/float(count))
# print(confusion_matrix)
print_matrix(confusion_matrix)

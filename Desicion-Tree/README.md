# Classification Framework
## Big Picture
This framework contains two classification methods: a basic method and an ensemble method. More specifically, decision tree and random forest. Given certain training dataset following a specific data format, the classification framework should be able to generate a classifier and use this classifier to assign labels to unseen test data instances.
## Steps
Step 1: Read in training dataset and test dataset, and store them in memory.
Step 2: Implement a basic classification method, which includes both training process and test process. Given a training dataset, the classification method should be able to construct a classifier correctly and efficiently. Given a test dataset, the classification method should be able to predict the label of the unseen test instances with the aforementioned classifier.
Step 3: Implement an ensemble method using the basic classification method in Step 2. The ensemble classification method should also be able to train a classifier and predict labels for unseen data instances.
Step 4: Test both the basic classification method and the ensemble method with different datasets. Evaluate their performances and write a report.

# Frequent Pattern Mining

## Input Format

The input dataset is a transaction dataset.

The first line of the input corresponds to the minimum support.

Each following line of the input corresponds to one transaction. Items in each transaction are seperated by a space.

Please refer to the sample input below. In sample input 0, the minimum support is 2. The dataset contains 3 transactions and 5 item types (A, B, C, D and E).

## Output Format
The output are the frequent patterns you mined from the input dataset.

Each line of the output should be in the format:

```
Support [frequent pattern]
Support [frequent pattern]
......
```

The frequent patterns should be ordered according to their support from largest to smallest. Ties should be resolved by ordering the frequent patterns according to the alphabetical order.

First print all the frequent patterns for part 1, then the closed frequent patterns for part 2 and last the maximal frequent patterns for part 3. Each part should be separated by an empty line.

Please refer to the sample output below. In sample output 0, the first 9 patterns are the frequent patterns for part 1, the following 3 patterns are the closed frequent patterns for part 2 and the last 2 patterns are the maximal frequent patterns for part 3.

## Sample Input
```
2
B A C E D
A C
C B D
```

## Sample Output
```
3 [C]
2 [A]
2 [A C]
2 [B]
2 [B C]
2 [B C D]
2 [B D]
2 [C D]
2 [D]

3 [C]
2 [A C]
2 [B C D]

2 [A C]
2 [B C D]
```

# 8 - Diffie-Hellman

## 8.1 Groups, Cyclic and subgroups 
Understanding the functionality of groups, cyclic groups and subgroups is important for the use of public-key cryptosystems based on the discrete logarithm
problem. That’s why we are going to practice some arithmetic in such structures
in this set of problems.
Let’s start with an easy one. Determine the order of all elements of the multi-
plicative groups of:

1. Z∗5
- 1 4 4 1
2. Z∗7
- 1 4 2 2 4 1
3. Z∗13
- 1 4 9 3 12 10 10 12 3 9 4 1

## 8.2 Elements

We consider the group Z∗53 . What are the possible element orders? How many
elements exist for each order?

- 53 Elementos, 52 Ordenes

## 8.3 From the subgroups

We now study the groups from Problem 8.2.
1. How many elements does each of the multiplicative groups have?
- Z * 5= 4
- Z * 7=6
- Z * 13=12

2. Do all orders from above divide the number of elements in the corresponding multiplicative group?
- Sí

3. Which of the elements from Problem 8.1 are primitive elements?
- Z * 5: [2, 3]
- Z * 7: [3, 5]
- Z * 13: [2, 6, 7, 11]

4. Verify for the groups that the number of primitive elements is given by φ (|Z∗p|)
- φ (4) = 2
- φ (6) = 2
- φ (12)= 4

## 8.4 Generators

 In this exercise we want to identify primitive elements (generators) of a multi-plicative group since they play a big role in the DHKE and and many other public-key schemes based on the DL problem. You are given a prime p = 4969 and the
corresponding multiplicative group Z∗4969 .
1. Determine how many generators exist in Z∗4969.
- 1584

2. What is the probability of a randomly chosen element a ∈ Z∗4969 being a genera-tor?
- 31.87%

3. Determine the smallest generator a ∈ Z∗4969 with a > 1000.
Hint: The identification can be done na¨ıvely through testing all possible factors of the group cardinality p − 1, or more efficiently by checking the premise that a(p−1)/q i = 1 mod p for all prime factors qi with p − 1 = ∏ qe
ii . You can simply start with a = 1001 and repeat these steps until you find a respective generator of Z∗4969 .
- 11

4. What measures can be taken in order to simplify the search for generators for arbitrary groups Z∗p?
- Se puede hacer una lista de los generadores de los grupos y buscar en esa lista

## 8.5 
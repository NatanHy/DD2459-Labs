## 1

## 2
### (i)
Assume in-place sorting.
```java
//@requires True
//@ensures \old(A).length() == A.length()
//@ensures \forall int i; 1 <= i <= A.length();
//          (\num_of int j;  1 <= j <= A.length(); A[j]==A[i]) ==
//          (\num_of int k;  1 <= k <= A.length(); \old(A)[k]==A[i]) 
//@ensures \forall i; 1 <= i < A.length(); A[i] <= A[i+1]
```

### (ii)
```java
//@requires Trye
//@ensures (\exits i; 1 <= i <= A.length() ; A[i] == key) ? \result = i : \result = -1
```

### (iii)
```java
//@requires True
//@ensures \exists i; 1 <= i <= A.length(); key == A[i]
```

### (iv)
```java
//@requires \forall i; 1 <= i < A.length(); A[i] <= A[i+1]
//@ensures (\exits i; 1 <= i <= A.length() ; A[i] == key) ? \result = i : \result = -1
```

## 4

### (i)

Mutation | Random | Pairwise
--- | --- | ---
1 | Timeout | Timeout
2 | 8 | 4
3 | 9 | 25
4 | 2 | 1
5 | 2 | 1
6 | Timeout | Timeout

### (iv)

N=100 gives a much larger test suite for pairwise testing. Both generating and reading the test case file takes significantly longer. In terms of effectiveness the tests are around the same as before. 

Mutation | Random | Pairwise
--- | --- | ---
1 | Timeout | Timeout
2 | 10 | 4
3 | 6 | 4
4 | 3 | 1
5 | 3 | 1
6 | Timeout | Timeout
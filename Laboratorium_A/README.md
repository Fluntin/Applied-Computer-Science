# Taping Papers Together

## Task Description

### Summary
Björn likes the square root of two, √2 = 1.41421356..., very much. He wants to write down the first 10000 digits of it on a single paper. Björn started this on an A4 paper but ran out of space after writing down only 1250 digits. He realized that he needs an A1 paper to fit all the digits. However, he doesn't have an A1 paper, but he has smaller papers that he can tape together.

To make an A1 paper, Björn can tape together two A2 papers along their long side, or two A3 papers to get an A2 paper, and so on. Given the number of papers of different sizes that Björn has, your task is to calculate how much tape he needs to make an A1 paper. The length of tape needed to join two sheets of paper is equal to their long side.

Each paper size (A2, A3, A4, ...) has the same shape, but each consecutive paper size has half the area of the previous one. An A2 paper measures 2^(-5/4) meters by 2^(-3/4) meters.

The first line of input contains a single integer n (2 ≤ n ≤ 30), which represents the A-size of the smallest papers Björn has. The second line contains n-1 integers, separated by spaces, representing the number of sheets he has of each paper size starting with A2 and ending with A n. It is guaranteed that Björn doesn't have more than 10^9 sheets of any paper size.

### Output
If Björn has enough paper to make an A1 paper, output a single floating-point number representing the smallest total length of tape needed in meters. If it is not possible to make an A1 paper, output "impossible". The output number should have an absolute error of at most 10^(-5).

# Matrix generator
With this generator you can generate 3x3 and 4x4 matrices and their code for LaTeX.  

You can choose the range of coefficients in matrices in _generate_matrix_ function.  

```
 x = random.randint(-5, 7)
```


## Determinant
Script find value of determinant for each matrix and decide whether is singular/regular.  


## Example of input/output

```
Enter dimension of matrix: 3 for 3x3, 4 for 4x4: 4
Entrer number of generated matrices: 1

[-5, -2, 7, -4]
[4, 1, 2, -4]
[2, -5, -2, 2]
[-2, 4, -3, -4]
Matrix is regular, its determinant is |A|=1530

\[
\begin{bmatrix}
-5 & -2 & 7 & -4 \\
4 & 1 & 2 & -4 \\
2 & -5 & -2 & 2 \\
-2 & 4 & -3 & -4
\end{bmatrix}
\]
```


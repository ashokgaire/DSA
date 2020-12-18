### Asymptotic analysis

We can have three cases to analyze an algorithm: 
1) The Worst Case 
2) Average Case 
3) Best Case


## Worst Case Analysis (Usually Done) 
In the worst case analysis, we calculate upper bound on running time of an algorithm. 
We must know the case that causes maximum number of operations to be executed. 
For Linear Search, the worst case happens when the element to be searched (x in the above code) is not present in the array. 
When x is not present, the search() functions compares it with all the elements of arr[] one by one. 
Therefore, the worst case time complexity of linear search would be Θ(n).

## Average Case Analysis (Sometimes done) 
In average case analysis, we take all possible inputs and calculate computing time for all of the inputs. 
Sum all the calculated values and divide the sum by total number of inputs. 
We must know (or predict) distribution of cases. For the linear search problem, 
let us assume that all cases are uniformly distributed (including the case of x not being present in array). 
So we sum all the cases and divide the sum by (n+1). Following is the value of average case time complexity. 
 

Average Case Time =  
analysis1
= analysis2
= Θ(n) 

## Best Case Analysis (Bogus) 
In the best case analysis, we calculate lower bound on running time of an algorithm. We must know the case that causes minimum number of operations to be executed. In the linear search problem, the best case occurs when x is present at the first location. The number of operations in the best case is constant (not dependent on n). So time complexity in the best case would be Θ(1) 
Most of the times, we do worst case analysis to analyze algorithms. In the worst analysis, we guarantee an upper bound on the running time of an algorithm which is good information. 
The average case analysis is not easy to do in most of the practical cases and it is rarely done. In the average case analysis, we must know (or predict) the mathematical distribution of all possible inputs.
The Best Case analysis is bogus. Guaranteeing a lower bound on an algorithm doesn’t provide any information as in the worst case, an algorithm may take years to run.


1) Θ Notation: The theta notation bounds a functions from above and below, so it defines exact asymptotic behavior.
A simple way to get Theta notation of an expression is to drop low order terms and ignore leading constants. For example, consider the following expression.
3n3 + 6n2 + 6000 = Θ(n3)
Dropping lower order terms is always fine because there will always be a n0 after which Θ(n3) has higher values than Θn2) irrespective of the constants involved.
For a given function g(n), we denote Θ(g(n)) is following set of functions.

Θ(g(n)) = {f(n): there exist positive constants c1, c2 and n0 such 
                 that 0 <= c1*g(n) <= f(n) <= c2*g(n) for all n >= n0}

The above definition means, if f(n) is theta of g(n), then the value f(n) is always between c1*g(n) and c2*g(n) for large values of n (n >= n0). The definition of theta also requires that f(n) must be non-negative for values of n greater than n0.

2) Big O Notation: The Big O notation defines an upper bound of an algorithm, it bounds a function only from above. For example, consider the case of Insertion Sort. It takes linear time in best case and quadratic time in worst case. We can safely say that the time complexity of Insertion sort is O(n^2). Note that O(n^2) also covers linear time.
If we use Θ notation to represent time complexity of Insertion sort, we have to use two statements for best and worst cases:
1. The worst case time complexity of Insertion Sort is Θ(n^2).
2. The best case time complexity of Insertion Sort is Θ(n).

The Big O notation is useful when we only have upper bound on time complexity of an algorithm. Many times we easily find an upper bound by simply looking at the algorithm.

3) Ω Notation: Just as Big O notation provides an asymptotic upper bound on a function, Ω notation provides an asymptotic lower bound.

Ω Notation can be useful when we have lower bound on time complexity of an algorithm. As discussed in the previous post, the best case performance of an algorithm is generally not useful, the Omega notation is the least used notation among all three.

For a given function g(n), we denote by Ω(g(n)) the set of functions.

Ω (g(n)) = {f(n): there exist positive constants c and
                  n0 such that 0 <= c*g(n) <= f(n) for
                  all n >= n0}.


### Properties of Asymptotic Notations :
As we have gone through the definition of this three notations let’s now discuss some important properties of those notations.

    General Properties :

    If f(n) is O(g(n)) then a*f(n) is also O(g(n)) ; where a is a constant.

    Example: f(n) = 2n²+5 is O(n²)
    then 7*f(n) = 7(2n²+5)
    = 14n²+35 is also O(n²)

    Similarly this property satisfies for both Θ and Ω notation.
    We can say
    If f(n) is Θ(g(n)) then a*f(n) is also Θ(g(n)) ; where a is a constant.
    If f(n) is Ω (g(n)) then a*f(n) is also Ω (g(n)) ; where a is a constant.
    Reflexive Properties :

    If f(n) is given then f(n) is O(f(n)).

    Example: f(n) = n² ; O(n²) i.e O(f(n))


    Similarly this property satisfies for both Θ and Ω notation.
    We can say
    If f(n) is given then f(n) is Θ(f(n)).
    If f(n) is given then f(n) is Ω (f(n)).
    Transitive Properties :

    If f(n) is O(g(n)) and g(n) is O(h(n)) then f(n) = O(h(n)) .

    Example: if f(n) = n , g(n) = n² and h(n)=n³
    n is O(n²) and n² is O(n³)
    then n is O(n³)

    Similarly this property satisfies for both Θ and Ω notation.
    We can say
    If f(n) is Θ(g(n)) and g(n) is Θ(h(n)) then f(n) = Θ(h(n)) .
    If f(n) is Ω (g(n)) and g(n) is Ω (h(n)) then f(n) = Ω (h(n))
    Symmetric Properties :

    If f(n) is Θ(g(n)) then g(n) is Θ(f(n)) .

    Example: f(n) = n² and g(n) = n²
    then f(n) = Θ(n²) and g(n) = Θ(n²)

    This property only satisfies for Θ notation.
    Transpose Symmetric Properties :

    If f(n) is O(g(n)) then g(n) is Ω (f(n)).

    Example: f(n) = n , g(n) = n²
    then n is O(n²) and n² is Ω (n)

    This property only satisfies for O and Ω notations.
    Some More Properties :
        If f(n) = O(g(n)) and f(n) = Ω(g(n)) then f(n) = Θ(g(n))
        If f(n) = O(g(n)) and d(n)=O(e(n))
        then f(n) + d(n) = O( max( g(n), e(n) ))
        Example: f(n) = n i.e O(n)
        d(n) = n² i.e O(n²)
        then f(n) + d(n) = n + n² i.e O(n²)
        If f(n)=O(g(n)) and d(n)=O(e(n))
        then f(n) * d(n) = O( g(n) * e(n) )
        Example: f(n) = n i.e O(n)
        d(n) = n² i.e O(n²)
        then f(n) * d(n) = n * n² = n³ i.e O(n³)


1) O(1): Time complexity of a function (or set of statements) is considered as O(1) if it doesn’t contain loop, recursion and call to any other non-constant time function.

   // set of non-recursive and non-loop statements

For example swap() function has O(1) time complexity.
A loop or recursion that runs a constant number of times is also considered as O(1). For example the following loop is O(1).

   // Here c is a constant   
   for (int i = 1; i <= c; i++) {  
        // some O(1) expressions
   }

2) O(n): Time Complexity of a loop is considered as O(n) if the loop variables is incremented / decremented by a constant amount. For example following functions have O(n) time complexity.

   // Here c is a positive integer constant   
   for (int i = 1; i <= n; i += c) {  
        // some O(1) expressions
   }

   for (int i = n; i > 0; i -= c) {
        // some O(1) expressions
   }

3) O(nc): Time complexity of nested loops is equal to the number of times the innermost statement is executed. For example the following sample loops have O(n2) time complexity


  
   for (int i = 1; i <=n; i += c) {
       for (int j = 1; j <=n; j += c) {
          // some O(1) expressions
       }
   }

   for (int i = n; i > 0; i -= c) {
       for (int j = i+1; j <=n; j += c) {
          // some O(1) expressions
   }

For example Selection sort and Insertion Sort have O(n2) time complexity.
4) O(Logn) Time Complexity of a loop is considered as O(Logn) if the loop variables is divided / multiplied by a constant amount.

   for (int i = 1; i <=n; i *= c) {
       // some O(1) expressions
   }
   for (int i = n; i > 0; i /= c) {
       // some O(1) expressions
   }

For example Binary Search(refer iterative implementation) has O(Logn) time complexity. Let us see mathematically how it is O(Log n). The series that we get in first loop is 1, c, c2, c3, … ck. If we put k equals to Logcn, we get cLogcn which is n.
5) O(LogLogn) Time Complexity of a loop is considered as O(LogLogn) if the loop variables is reduced / increased exponentially by a constant amount.

   // Here c is a constant greater than 1   
   for (int i = 2; i <=n; i = pow(i, c)) { 
       // some O(1) expressions
   }
   //Here fun is sqrt or cuberoot or any other constant root
   for (int i = n; i > 1; i = fun(i)) { 
       // some O(1) expressions
   }
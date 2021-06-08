# python-functions
This repository will have the python function concepts and programs to implement those concepts as example.
## In this section we will learn about following:
#### 1. Arguments vs Parameters
#### 2. Positional vs keyword-only arguments
#### 3. Optional Arguments
#### 4. Unpacking iterables and Function Arguments.
#### 5. Extended unpacking
#### 6. Varialbe number of positional and keyword-only arguments

## 1. Arguments and Parameters
**Parameters** are the **local variables in a function** which are **written inside the paranthesis** while defining any function.

**Arguments** are the **values which are passed to the functions** when it is called.

In python, arguments are **passed by reference**. Technically the **memory address** of arguments are passed. 

## 2. Positional and Keyword-only arguments
This is the most **common way of assigning arguments to parameters**: **via order** in which they are passed i.e. **their position**.

**Example:** 

Let us consider a function my_func as below:

```python
def my_func(a,b):
  #code
```

Now let's **call my_func in two ways** as mentioned below:

1. my_func(10,20) **#In this way, parameter a is assigned 10 and parameter b is assigned 20. Here 10 and 20 are the arguments.**
2. my_func(20,10) **#In this way, parameter a is assigned 20 and parameter b is assigned 10. Here 20 and 10 are the arguments.**

**Hence these are the positional arguments, where with the change in the position of the arguments the value of the parameters changes.**





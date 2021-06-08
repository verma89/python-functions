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

****Positional Arguments:****

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

****Default Values:****

A positional argument can be made **optional** by specifying a **default value for corresponding parameter**.

```python
def my_func(a, b=100):
  #code
```

The above function **my_func(a, b=100)** can be called by passing only one argument also, as shown below:

1. my_func(50) **#argument 50 will be assigned to parameter a and b will be assigned with default value 100. **
2. my_func(50,150) **#argument 50 will be assigned to parameter a and argument 150 will be assigned to parameter b. **
3. my_func() **#This way of calling will throw exception as the function is having one possitional parameter for which passing one argument is mandatory. Hence this is wrong way of calling above function**

**Making one positional argument optional out of three:**

Let us consider below function:

```python
def my_func(a, b=10, c):
  #code
```

How to call function **my_func(a, b=10, c)** without specifying value for the second parameter?
1. my_func(5,2) # If called in this way, **argument 5** will be **passed to parameter a** and **argument 2** will be **passed to parameter b** and not to parameter c which will result in exception.

Hence defining function in this way in the present example is not right neither the calling is right. 

**Rules for defining a default value for positional arguments:**

If a Positional Parameter is defined with a defult value, then every positional parameter after it must be given a default value.

Therefore the valid function definition for the above case or scenario will be:


```python
def my_func(a, b=10, c=20):
  #code
```

Now function **my_func(a, b=10, c=20)** can be called in follwing ways:
1. my_func(5) **#argument 5 will be assigned to parameter a. Parameters b and c will be assigned with their respective default values i.e. 10, 20**
2. my_func(5, 3) **#argument 5 and 3 will be assigned to parameters a, b respectively. Parameter c will be assigned with default value 20**
3. my_func(5, 3, 2) **#argument 5, 3, 2 will be assigned to parameters a, b, c respectively.**
4. my_func() **#This way of calling will throw exception as parameter a expects one positional argument to be passed.**

****Keyword argument:****

Now **another case** if i want to **specify the 1st and 3rd arguments but ommit the second argument**. i.e. i want to specify values for parameters a and c but let b take on it default value.

This case can be** achieved using keyword argument**. Using keyword argument positional argument can, optionally, be specified by using the parameter name, whether or not the parameter have default value.

**Let us consider a function having defaut values to its parameters:**

```python
def my_func(a, b=10, c=30):
  #code
```

The above function can be called in following ways using keyword arguments
1. my_func(a=1, c=3)
2. my_func(c=3, a=1)
3. my_func(1, c=3)


**Let us consider a function having all positional parameters:**

```python
def my_func(a, b, c):
  #code
```

The above function can be called in following ways using keyword arguments
1. my_func(1, 2, 3)
2. my_func(1, 2, c = 3)
3. my_func(a = 1, b = 2, c = 3)
4. my_func(a = 1, c = 3, b = 2)

NOTE: Once you use a named argument, all the arguments thereafter should be named too.

**Example:**

1. my_func(c = 3, 1, 2) #looking into this call value 3 can be assigned to parameter c, after that there will be confusion if values 1 and 2 should be assigned to parameters  b or c, c or b. hence causing exception. Thus not a valid syntax.
2. my_func(3, b = 1, 2) 

In both the above case we tried to put possitional argument after keyword arguemnt, which is inavlid syntax. Hence exception will be thrown.

3. my_func(3, b = 1, c = 2) # this is a valid call. Keyword argument followed by keyword arguments.
4. my_func(3, c = 2, b = 1) #As the position doesnot matter for keyword argument thus it will work equally in the same way.

## 4. Unpacking Iterables:
****Prior to this lets revisit the basics of tuple.****

1. In python tuple is defined by **,** and not **()**. **()** is used to make tuple clearer.

**Example: **

1,2,3 and (1,2,3) both are a valid tuple. **() is optional in (1,2,3)**

2. To create a tuple with single element use **,** with element.

**Example:**

1, or (1, ) is a valid syntax to create tuple with single element. However (1) will not create a tuple with single element rather it will create an integer data.

3. To create an empty tupel you can use **()** (it's exception) or you may use **tuple()**

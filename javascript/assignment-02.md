# Assignment : Introduction to Variables and Datatypes
---
## Part I : Variables (let, var, const)

### Part a — 4 Questions

**1. Personal Information**
Declare variables for `name`, `age`, and `city` using appropriate variable keywords. Assign values and print all three variables.

**2. Change the Score**
Create a variable `score` with the value `50`. Change its value to `80` and print the final value. Use the appropriate keyword for a value that can change.

**3. Constant Value**
Create a constant variable `PI` with the value `3.14`. Print its value. Do not try to change the value.

**4. Uninitialized Variables**
Declare one variable having name `num1` using `var` and one having name `num2` using `let` without assigning values. Print both variables. Then assign values to them and print the values again.

---

### Part b — 4 Questions

**5. Choose the Correct Keyword**
Create the following variables using the most appropriate keyword:

* `studentName` — the value will not change
* `marks` — the value may change
* `schoolName` — the value will not change

Assign values to all three variables. Change `marks` and print all variables.

**6. Understand Scope**
Write a program where `var`, `let`, and `const` variables are declared inside an `if` block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.

**7. Test Re-declaration**
Declare a variable named `user` using `var` and declare it again with a different value. Then perform the same experiment using `let`. Observe what happens and identify which declaration allows re-declaration.

**8. Test Re-assignment**
Create three variables using `var`, `let`, and `const`. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.

---

### Part c — 2 Questions

**9. Predict and Explain**
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```

**10. Fix the Program**
The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for **initialization, re-declaration, re-assignment, and scope**.

```javascript
const name;

let age = 20;
let age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
}

console.log(country);

const score = 50;
score = 80;
```

#### Part d — 2 Question 

**11. Predict the Hoisting Behavior**  
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of hoisting for `var`, `let`, and `const`.

```javascript
console.log(a);
console.log(b);
console.log(c);

var a = 10;
let b = 20;
const c = 30;
```

**12. Fix the Hoisting Errors**  
The following program contains errors related to hoisting. Fix the code so that it runs correctly without any errors. Make sure your solution follows the rules of hoisting for `var`, `let`, and `const` (you may reorder declarations/assignments or change keywords only where necessary to make it work properly).

```javascript
console.log(x);
console.log(y);
console.log(z);

var x = "Hello";
let y = "World";
const z = "!";

console.log(x + " " + y + z);
```


**Questions on Primitive vs Non-Primitive Data Types**

---

### Part e — Basic Identification (4 Questions)

**1. Classify the Types**  
Declare one variable of each of the following types and print both the value and its type using `typeof`:
- A whole number  
- A decimal number  
- A piece of text  
- A true/false value  

**2. Undefined vs Null**  
Declare two variables:
- `a` using `let` without assigning any value  
- `b` and intentionally assign `null` to it  

Print both variables and their `typeof` results. Explain the difference between `undefined` and `null`.

**3. Number Special Values**  
Create variables for the following and print each value along with its type:
- Positive Infinity  
- Negative Infinity  
- Not-a-Number (`NaN`)  
- A large number written with scientific notation (e.g., `2.5e3`)  
- A number written with underscores for readability (e.g., `1_000_000`)

**4. String Styles**  
Create three string variables using:
- Single quotes  
- Double quotes  
- Template literals (backticks) that include another variable  

Print all three strings.

---

### Part f — Advanced Primitive Types (3 Questions)

**5. Symbol Uniqueness**  
Create two Symbols with the same description (`'id'`).  
Compare them using `===` and print the result.  
Then use both Symbols as keys in an object and retrieve the values.  
Explain why the comparison returns `false`.

**6. BigInt Precision**  
Create a regular `number` with the value `9007199254740991` (Number.MAX_SAFE_INTEGER).  
Add `1`, `2`, and `3` to it and print the results.  
Now create the same value as a `BigInt` and perform the same additions.  
Print the results and explain the difference.

**7. Choose the Correct Type**  
For each description below, write the most appropriate primitive data type and give an example declaration:
- A unique identifier that is never equal to another value with the same description  
- A very large integer that must keep exact precision  
- A variable that has been declared but not yet given a value  
- An intentional empty value  

---

### Part g — Prediction & Fixing (3 Questions)

**8. Predict the Output**  
Without running the code, predict what each `console.log` will print (value + type). Explain your reasoning.

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);
console.log(typeof b, b);
console.log(typeof c, c);
console.log(typeof d, d);
console.log(typeof e, e);
console.log(typeof f, f);
console.log(typeof g, g);
```

**9. Fix the Code**  
The following program has mistakes related to primitive types. Fix it so that it runs correctly and prints meaningful values.

```javascript
let num = 10;
let text = Hello;
let flag = True;
let empty;
let nothing = Null;
let unique = symbol("id");
let big = 9007199254740991;

console.log(num, text, flag, empty, nothing, unique, big);
```

**10. Primitive vs Non-Primitive**  
Answer the following questions in your own words and give one example for each:

a) What is the main difference between Primitive and Non-Primitive data types?  
b) Why are Numbers, Strings, Booleans, Undefined, Null, Symbol, and BigInt called Primitive?  
c) Give one example of a Non-Primitive data type and explain why it is considered Non-Primitive.



<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/fbe44b69-2625-43fb-af37-22bd1bfa1a48" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/b42b49ba-a78a-41d1-b386-6bfa0d525a23" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/8287912a-99e5-48f8-b9a7-f94e8b04cd74" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/fdd502e0-24cb-45ae-bbcf-146ed3f36780" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/e89aa3ec-7a37-44e5-9fa2-eacca6d77ac4" />





# Part D — Hoisting

## 11. Predict the Hoisting Behavior

```javascript
console.log(a); // undefined
console.log(b); // ReferenceError
console.log(c); // ReferenceError

var a = 10;
let b = 20;
const c = 30;
```

### Explanation:

* `var` is hoisted and gets the value `undefined`.
* `let` and `const` are hoisted but cannot be accessed before their declaration.
* Therefore, `b` and `c` cause `ReferenceError`.

---

## 12. Fix the Hoisting Errors

```javascript
var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z);
```

### Explanation:

The variables are declared before they are used, so there are no hoisting errors.

---

# Part E — Basic Identification

## 1. Classify the Types

```javascript
let whole = 10;
let decimal = 10.5;
let text = "Hello";
let value = true;

console.log(whole, typeof whole);
console.log(decimal, typeof decimal);
console.log(text, typeof text);
console.log(value, typeof value);
```

### Explanation:

* `10` → number
* `10.5` → number
* `"Hello"` → string
* `true` → boolean

---

## 2. Undefined vs Null

```javascript
let a;
let b = null;

console.log(a, typeof a);
console.log(b, typeof b);
```

### Explanation:

* `a` is `undefined` because no value was assigned.
* `b` is `null` because we intentionally assigned an empty value.
* Note: `typeof null` returns `"object"` in JavaScript.

---

## 3. Number Special Values

```javascript
let positiveInfinity = Infinity;
let negativeInfinity = -Infinity;
let notANumber = NaN;
let scientific = 2.5e3;
let largeNumber = 1_000_000;

console.log(positiveInfinity, typeof positiveInfinity);
console.log(negativeInfinity, typeof negativeInfinity);
console.log(notANumber, typeof notANumber);
console.log(scientific, typeof scientific);
console.log(largeNumber, typeof largeNumber);
```

### Explanation:

All of these are JavaScript `number` values.

* `Infinity` → positive infinity
* `-Infinity` → negative infinity
* `NaN` → Not-a-Number
* `2.5e3` → 2500
* `1_000_000` → 1000000

---

## 4. String Styles

```javascript
let single = 'Hello';
let double = "World";

let name = "John";
let template = `Hello ${name}`;

console.log(single);
console.log(double);
console.log(template);
```

### Explanation:

JavaScript supports single quotes, double quotes, and backticks. Template literals can include variables using `${}`.

---

# Part F — Advanced Primitive Types

## 5. Symbol Uniqueness

```javascript
let first = Symbol("id");
let second = Symbol("id");

console.log(first === second); // false

let object = {};

object[first] = "First Value";
object[second] = "Second Value";

console.log(object[first]);
console.log(object[second]);
```

### Explanation:

Both Symbols have the same description, but every Symbol is unique. Therefore, `first === second` is `false`.

---

## 6. BigInt Precision

```javascript
let num = 9007199254740991;

console.log(num + 1);
console.log(num + 2);
console.log(num + 3);

let big = 9007199254740991n;

console.log(big + 1n);
console.log(big + 2n);
console.log(big + 3n);
```

### Explanation:

`Number` has a maximum safe integer of `9007199254740991`. Beyond this, exact precision cannot always be guaranteed.

`BigInt` is used for very large integers and keeps exact precision.

---

## 7. Choose the Correct Type

### A unique identifier

```javascript
let id = Symbol("id");
```

**Type:** `Symbol`

### A very large exact integer

```javascript
let bigNumber = 12345678901234567890n;
```

**Type:** `BigInt`

### A declared variable without a value

```javascript
let value;
```

**Value:** `undefined`

### An intentional empty value

```javascript
let empty = null;
```

**Value:** `null`

---

# Part G — Prediction & Fixing

## 8. Predict the Output

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a); // undefined undefined
console.log(typeof b, b); // object null
console.log(typeof c, c); // number 42
console.log(typeof d, d); // string Hello
console.log(typeof e, e); // boolean true
console.log(typeof f, f); // symbol Symbol(key)
console.log(typeof g, g); // bigint 123n
```

### Explanation:

`typeof` tells us the data type of each value.

* `a` → undefined
* `b` → object (special behavior of `null`)
* `c` → number
* `d` → string
* `e` → boolean
* `f` → symbol
* `g` → bigint

---

## 9. Fix the Code

```javascript
let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = null;
let unique = Symbol("id");
let big = 9007199254740991n;

console.log(num, text, flag, empty, nothing, unique, big);
```

### Explanation:

The original code had several errors:

* `Hello` needed quotes because it is a string.
* `True` should be lowercase `true`.
* `Null` should be lowercase `null`.
* `symbol()` should be `Symbol()`.
* `9007199254740991n` is written as BigInt using `n`.

---

## 10. Primitive vs Non-Primitive

### a) Main difference

**Primitive data types** store a single basic value.

**Non-primitive data types** can store collections of values or more complex data.

Example:

```javascript
let number = 10;        // Primitive

let numbers = [1, 2, 3]; // Non-Primitive
```

---

### b) Why are they called Primitive?

Numbers, Strings, Booleans, Undefined, Null, Symbols, and BigInts are called primitive because they represent basic, single values and are not objects.

Example:

```javascript
let age = 18;
let name = "John";
let passed = true;
```

---

### c) Example of a Non-Primitive Type

```javascript
let person = {
    name: "John",
    age: 20
};
```

**Explanation:**
`person` is an object, which is non-primitive because it can contain multiple related values.





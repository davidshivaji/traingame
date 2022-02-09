# traingame solver

Given a four-digit number, using each digit only once and any 3 operators (+-/*), try to make an equation that results in a desired result integer. (10 by default).

## Usage
```
$ python main.py DIGITS OPTIONAL_RESULT
```

## Example

```
$ python main.py 6550
6*0+5+5 = 10
found 29 other solutions resulting in 10
```

## Example 2
Pass an optional desired result as the second argument.

```
$ python main.py 6283 21
6/2*8-3 = 21
found 5 other solutions resulting in 21
```

/**
 * Operators
 * 
 */

console.log(10 + 10);
console.log(10 - 10);
console.log(10 * 10);
console.log(10 / 10);
console.log(10 % 7); // mod ~ residual "lefter"

console.log(10**3);


console.log('--------------------')

let number = 1;
number ++;
console.log(number);
number --;
console.log(number);

console.log('--------------------')

let result = 1;

result = number ++;
console.log(result, number); //= first and then ++

result = --number;
console.log(result, number); //-- first and then =
// but do not use usually

console.log('--------------------')

let sample = '99';

console.log(+sample);
console.log(-sample);// this temporary transform into number but not change itself
console.log(typeof +sample);
console.log(typeof sample);

sample = true;

console.log(typeof +sample);
console.log(+sample);
console.log(-sample);
console.log(typeof sample);

sample = false;

console.log(typeof +sample);
console.log(+sample);
console.log(typeof sample);

sample = 'define';

console.log(typeof +sample); //Not a Number (NaN)
console.log(+sample);
console.log(typeof sample);

console.log('--------------------')

num01 = 100;

console.log(num01);

num01 += 20;
console.log(num01);

num01 *= 5;
console.log(num01);


console.log('--------------------')

console.log(5 == 5); //excluding type
console.log(5 == '5');
console.log(0 == '');
console.log(true == 1);
console.log(true == '1');

console.log('--------------------')

console.log(5 === 5); //including type
console.log(5 === '5');

console.log(5 != 5); // ! indicates the opposite
console.log(5 != '5');
console.log(5 !== '5');

console.log('--------------------')

console.log(100>1);
console.log(100<1);
console.log(100 <= 1);
console.log(100 >= 1);

console.log('--------------------')

//Ternaty operator
console.log(10 > 0 ? "10 is bigger than 0" : "haha");  //if it is true run left and if false run right
//condition ? <true> <false>

console.log('--------------------')

console.log(true && true); //AND condition
console.log(true && false); // give false

console.log(true || false); // OR condition ~ ||


console.log(10 > 1 && 20 < 2);
console.log(1.1 + 0.1 == 1.2); //RAM issue on the float case.

console.log('--------------------')

//short circuit evaluation

//&& => if left is true then give right
//&& => if left is false then give left
//|| => if left is true then give left
//|| => if left is false then give right

console.log(true && "apple");
console.log(false && "apple");

console.log(true || "apple");
console.log(false || "apple");

console.log(true && true && 'apple');

console.log(true && true && false && 'banana');

console.log('--------------------')


let name02;
console.log(name02);

name02 = name02 ?? 'cake'; // if name02 is null then give right one.
console.log(name02)

name02 = name02 ?? 'bacon'; // if not nothing happens.
console.log(name02)

let name03;
name03 ??= 'bacon' // same with = XXX ?? XXX
console.log(name03)


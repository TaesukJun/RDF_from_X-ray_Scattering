/**
 * Data Types
 * - 6 Primitive Type (smallest unit) + 1 Object Type
 * List of 6 Primitive Type
 * 1) number
 * 2) String
 * 3) Boolean (true or false)
 * 4) undefined
 * 5) null
 * 6) Symbol
 * +
 * 7) Object
 *  -Function
 *  -Array
 *  -Object
 * 
 * 
 */

// Number Types
const AGE = 32;
const TEMPERATURE = -10;
const PI = 3.14;
console.log(typeof AGE);
console.log(typeof TEMPERATURE);
console.log(typeof PI);
console.log('-------------');

const INF = Infinity;
const N_INF = -Infinity;
console.log(typeof INF);
console.log(typeof N_INF);
console.log('-------------');

// String Types
const codeFind = '"C"ode Find'; //to print string of ""
console.log(codeFind);
console.log(typeof codeFind);
const ive = "'ive' love" //to print string of ''
console.log(ive);

    /** Template Literal
     * 
     * Escaping Character
     * 1) new line => \n
     * 2) tab => \t
     * 3) backslash =? \\
     * 4) small qutoation = \'
     *  */ 

const APPLE1 = 'apple\nbanana';
console.log(APPLE1);
const APPLE2 = 'apple\tbanana';
console.log(APPLE2);
const APPLE3 = 'apple\\banana';
console.log(APPLE3);
const APPLE4 = 'apple\'banana';
console.log(APPLE4);
const APPLE5 = `'apple/'ban
ana'`;
console.log(APPLE5);
console.log(typeof APPLE5);

const GroupName = 'TJ';
console.log(GroupName + ' desk');
console.log(`${GroupName} / line`)

console.log('-------------');

// Boolean Types
let isTrue = true;
let isFalse = false;
console.log(typeof isTrue);
console.log(typeof isFalse);


console.log('-------------');
/**
 * Undefined Type
 * : The value assigned when users don't set any value.
 * do not decalre the value with undefined.
 */

let kate;
console.log(kate);
console.log(typeof kate);

console.log('-------------');

/**
 * Null Type
 * : The value assigned when users directly set as null.
 * uses when users reset the values.
 */
kate = null;
console.log(kate);
console.log(typeof kate); //but this reads object due to legacy codes.

console.log('-------------');
/**
 * Symbol Types
 * : for generation of unique value.
 * used by calling Symbol Functions
 */

const TEST1 = '1';
const TEST2 = '1';

console.log(TEST1 === TEST2);

const SYMBOL1 = Symbol('1');
const SYMBOL2 = Symbol('1');

console.log(SYMBOL1 === SYMBOL2);
console.log(typeof SYMBOL1);

console.log('-------------');
/** 
 * Object Types
 * -similar to Map Type
 * -coupled with key: value 
 * 
 */

const Dictionary = {
    red: '1red',
    orange: '2orange',
    yellow: '3yellow',
};

console.log(Dictionary);
console.log(Dictionary['red']);
console.log(Dictionary['orange']);
console.log(typeof Dictionary);
console.log(typeof Dictionary['red']);
/**
 * Array Tupes
 * value -> lists
 * 
 */

let fruitArray = [
    'cake',
    'fish',
    'island',
    'kiss',

]
console.log(fruitArray)
console.log(fruitArray[0])
console.log(typeof fruitArray);
console.log(typeof fruitArray[0]);

fruitArray[0] = 'this';
console.log(fruitArray);



/** 
 * Static typing
 * -declaring what type you want to use.
 * 
 * Dynamic typing
 * -fetch the type from the values that you input.
 * JS -> dynamic typing
 * 
 */

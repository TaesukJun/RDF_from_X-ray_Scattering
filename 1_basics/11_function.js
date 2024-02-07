/** function */

console.log(((2*10/2)%3).toString());

function calc(value = 2, value02 = 1) {
    console.log(((value*value02*10/2)%7).toString());
    
}

for (let i = 0; i < 10; i++) {
    calc(i,i);
}
console.log('-----------------------');
function multi(x=1,y=1) {
    return x * y;
}
// same with
const samemulti = function(x=1, y =1){
    return x * y;
}


console.log(multi(2,4));

/** arrow function */
// case01
const multi02 = (x=1,y=1) => {
    return x * y
}
console.log(multi02(2,3));

// case02
const multi03 = (x=1,y=1) => x * y

console.log(multi03(4,4));

// case03
const multi04 = x  => x * 16

console.log(multi04(4));

// case04
const multi05 = x  => y => z => `x: ${x} y: ${y} z: ${z}`;

console.log(multi05(2)(5)(7));
// console.log(multi05(2)(5)); // error

console.log('-------------------------');

const multiThree = function(x=1, y =1, z=1){
    console.log(arguments); // confirm what values are input into this funciton
    return x * y * z;
}
console.log('-------------------------');
console.log(multiThree(4,5,6))

console.log('-------------------------');

const multiAll = function(...arguments){
    return Object.values(arguments).reduce((a,b) => a * b,1);
}
console.log(multiAll(2,3,4,5,6,7,8));

console.log('-------------------------');

// immediately invoked function -use function immediately right away without declaring
(function (x=1, y=1) {
    console.log(x * y);
})(4,5)

console.log('-------------------------');

console.log(typeof multi);
console.log(multi instanceof Object); // is equal to type? - true => function is Object


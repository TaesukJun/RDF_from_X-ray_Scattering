// https://www.youtube.com/watch?v=ZOVG7_41kJE&t=10333s
/**
 * Array Functions
 */
let iveMembers = [
    '안유진',
    '가을',
    '레이',
    '장원영',
    '리즈',
    '이서',
];

console.log(iveMembers);

// push('xx') - put element at the last of array and save it on that variable

console.log(iveMembers.push('codeFactory')); //if this is read, it gives the number of elements after code
console.log(iveMembers);

console.log('---------------------');


// pop() - delete the last element from array

console.log(iveMembers.pop()); //if this is read, it gives the last element that will be deleted.
console.log(iveMembers);

console.log('---------------------');


// shift() - delete the first element from array

console.log(iveMembers.shift()); //if this is read, it gives the first element that will be deleted.
console.log(iveMembers);

console.log('---------------------');


// unshift('xx") - put element at the first of array and save it on that variable

console.log(iveMembers.unshift('안유진')); //if this is read, it gives the number of elements after code
console.log(iveMembers);

console.log('---------------------');


// splice(start index, number of element) - delete element from start index with number of element

console.log(iveMembers.splice(0, 3)); ////if this is read, it returns the elements that will be deleted.
console.log(iveMembers);

console.log('---------------------');
console.log('---------------------');



// Not changing the array type

let iveMembers2 = [
    '안유진',
    '가을',
    '레이',
    '장원영',
    '리즈',
    '이서',
];

console.log(iveMembers2);

// concat() - this acts like push but it does not change the array after all

console.log(iveMembers2.concat('codeFactory')); //if this is read, it gives array after concat
console.log(iveMembers2);

console.log('---------------------');


// slice(start index, end index) - show element from (start index) to (end index - 1), BUT does not change the array itself

console.log(iveMembers2.slice(0, 3)); ////if this is read, it returns the elements that will be deleted.
console.log(iveMembers2);

console.log('---------------------');
console.log('---------------------');


// spread operator
let iveMembers3 =[
    ...iveMembers2,
];

console.log(iveMembers3);
console.log('---------------------');

let iveMembers4 =[
    iveMembers2,
];
console.log(iveMembers4);
console.log('---------------------');

let iveMembers5 =iveMembers2;
console.log(iveMembers5);
console.log(iveMembers5 === iveMembers2);
console.log(iveMembers3 === iveMembers2); //due to memory storage difference
console.log('---------------------');
console.log('---------------------');

// Frequently used


// join()
console.log(iveMembers2.join());
console.log(typeof iveMembers2.join());
console.log(iveMembers2.join('/'));
console.log(iveMembers2.join(', ')); // in ( XXX ) show how to divide each element

// sort() - ascending // revers() - decending
console.log(iveMembers2.sort());
console.log(iveMembers2);
console.log(iveMembers2.reverse());


let numbers = [
    1,
    9,
    7,
    5,
    3
];
console.log(numbers);
console.log(numbers.sort((a, b)=>{
    return a > b ? 1 : -1;
})); 
/** sort((a, b)=>{})
 * compared a and b
 * if a goes back b when number larger than 0
 * if a comes first than b when number smaller than 0
 * if sequence is same when 0
 */

console.log(numbers.sort((a, b)=>{
    return a > b ? -1 : 1;
})); 


// map() - do not change the array after code.
console.log('---------------------');
console.log('---------------------');

console.log(iveMembers2.map((x) => x));
console.log(iveMembers2.map((x) => `아이브: ${x}`));
console.log(iveMembers2.map((x) => {
    if(x == '안유진') {
        return `아이브: ${x}`;
    }else{
        return x

    }
    
}
));
console.log(iveMembers2);
console.log('---------------------');
console.log('---------------------');

// filter() - return array with satisfying elements

numbers = [1,8,7,6,3];
console.log(numbers.filter(
    (x) => true
));
console.log(numbers.filter(
    (x) => false
));
console.log(numbers.filter(
    (x) => x % 2 == 0
));
console.log('---------------------');
console.log('---------------------');

// find() - return the only first element that satisfy the condtion
console.log(numbers.find(
    (x) => x % 2 == 0
));

// findIndex() - return the index of the first element that satisfy the condtion
console.log(numbers.findIndex(
    (x) => x % 2 == 0
));

// reduce()
console.log(numbers.reduce(
    (p,n) => p + n  , 0 //callback funtion, initial value (in here is p)
));



/**
 * property attribute
 * 1) data property - key and value that has actual value
 * 2) accessor propery - no value but bring other value and call function ex) get, set
 * 
 */

// const yuJin = {
//     name: 'an',
//     year: 2003,
// };
// console.log(Object.getOwnPropertyDescriptor(yuJin,'name'));
// console.log(Object.getOwnPropertyDescriptor(yuJin,'year'));
//{ value: 'an', writable: true, enumerable: true, configurable: true }

/**
 * 1) value - actual property value
 * 2) writable - can be changed?
 * 3) enumerable - can be used as list (e.g. for in)
 * 4) configuralbe - can property attribute be reclaimed / if false then, delete and attribute change cannot be possible.
 */

// console.log(Object.getOwnPropertyDescriptors(yuJin));
console.log(`..............................`);

const yuJin = {
    name: 'an',
    year: 2003,
    get age(){
        return new Date().getFullYear() - this.year;
    },
    set age(age){
        this.year = new Date().getFullYear() - age;
    },
};
console.log(yuJin)
console.log(yuJin.age)
console.log(Object.getOwnPropertyDescriptors(yuJin));


console.log(Object.getOwnPropertyDescriptor(yuJin,'age'));

// yuJin.height = 172;
// yuJin['height'] = 172;
// console.log(Object.getOwnPropertyDescriptors(yuJin,'height'));

Object.defineProperty(yuJin, 'height', {
    value: 172,
    // writable: true,
    // enumerable: true,
    // configurable: true,
})

console.log(yuJin)
console.log(Object.getOwnPropertyDescriptor(yuJin,'height'));

// writable 

yuJin.height = 180;

console.log(yuJin)

// enumerable

console.log(Object.keys(yuJin));
for(let key in yuJin){
    console.log(key);
}

Object.defineProperty(yuJin, 'name', {
    enumerable:false,
});

console.log(Object.getOwnPropertyDescriptor(yuJin, 'name'));

console.log('-------------');
console.log(Object.keys(yuJin));
for(let key in yuJin){
    console.log(key);
}
console.log(yuJin);
console.log(yuJin.name);


Object.defineProperty(yuJin, 'height', {
    value: 172,
});
console.log(Object.getOwnPropertyDescriptor(yuJin, 'height'));

Object.defineProperty(yuJin, 'height',{
    writable: true,
});
// if configurable is false, only writable true -> false can be made without cases are forbidden.

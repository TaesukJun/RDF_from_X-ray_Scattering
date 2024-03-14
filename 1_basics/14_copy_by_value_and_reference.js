/**
 * copy by value
 * copy by reference
 * 1) default - every primitive value is copy by value
 * 2) object is copy by reference
 */

let original = 'hello';
let clone = original;
console.log(original);
console.log(clone);
console.log(original === clone);

console.log('-------------------');
clone += ' is ahn';
console.log(original);
console.log(clone);


console.log('-------------------');
console.log('-------------------');
let originalObj ={
    name: 'ahn',
    group: 'ive',
}
let cloneObj = originalObj;

console.log(originalObj);
console.log(cloneObj);

console.log('-------------------');
originalObj['group'] = 'codeJun'
console.log(originalObj);
console.log(cloneObj);

console.log(originalObj === cloneObj);

let originalObj2 ={
    name: 'ahn',
    group: 'codeJun',
}

console.log(originalObj === originalObj2);

const YuJin1 = {
    name: 'ahn',
    group: 'ive',
};

const YuJin2 = YuJin1;

const YuJin3 = {
    name: 'ahn',
    group: 'ive',
};
console.log('-------------------');
console.log(YuJin1 === YuJin2);
console.log(YuJin1 === YuJin3); //reading only reference address >> false
console.log(YuJin2 === YuJin3);

/**
 * Spread Operator
 */

const YuJin4 = {
    ...YuJin3,

}
//spread Operator -> copy by value

console.log(YuJin4);
console.log(YuJin1 == YuJin3);

console.log('-------------------');
const YuJin5 = {
    year: 2003,
    ...YuJin3,

}
console.log(YuJin5);

console.log('-------------------');
const YuJin6 = {
    name: 2003,
    ...YuJin3,

}
console.log(YuJin6);

console.log('-------------------');
const YuJin7 = {
    
    ...YuJin3,
    name: 2003,
}
console.log(YuJin7);
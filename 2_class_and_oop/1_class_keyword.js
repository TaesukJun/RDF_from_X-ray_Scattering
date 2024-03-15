/**
 * class keyword
 * Ex) Class <- name and birth year [Frame]
 * Object (Instance)
 * 
 */

class IdolModel{
    // name;
    // year;
    constructor(name,year){
        this.name = name;
        this.year = year;


    }

    sayName(){
        return `hello I am ${this.name}`;




    }



};

// constructor - making instance for class


const yuJin = new IdolModel('an',2003);
console.log(yuJin);
const gaEul = new IdolModel('GE',2002);
console.log(gaEul);
const ray = new IdolModel('ray',2004);
console.log(ray);
const wonYoung = new IdolModel('WY',2004);
console.log(wonYoung);
const liz = new IdolModel('liz',2004);
console.log(liz);
const eSeo = new IdolModel('ES',2004);
console.log(eSeo);

console.log(yuJin.name);


console.log(yuJin.sayName());
console.log(eSeo.sayName());

console.log(typeof IdolModel);
console.log(typeof yuJin);
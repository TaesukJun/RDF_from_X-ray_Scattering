/**
 * all about object
 * 
 * methods - declaring teh obejct
 * 1) create object - {}
 * 2) class instancification - class and OOP
 * 3) using function to create object
 */

const yuJin = {
    name: 'an',
    year: 2003,
}

console.log(yuJin);
class IdolModel{
    name;
    year;
    constructor(name,year){
        this.name = name;
        this.year = year;
    }
}
console.log(new IdolModel('an',2003));

// constructor function
function IdolFunction(name, year){
    this.name = name;
    this.year = year;
}
const gaEul = new IdolFunction('gaeul',2002);
console.log(gaEul);
console.log(yuJin == new IdolModel('an',2003));
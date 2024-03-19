/**
 * Inheritance
 * c.f.) class - object (instance) + method
 * inheritance - want to share same class properties
 *  ~ same properties (parent/super class) + other properties (child class)
 */

class IdModel{
    name;
    year;
    constructor(name,year){
        this.name = name;
        this.year = year;

    }
}

class FeIdModel extends IdModel{
    dance(){
        return `${this.name} is dancing`
    }
}

class MaIdModel extends IdModel{
    sing(){
        return `${this.name} is singing`
    }
}
const yuJin = new FeIdModel('an',2003);

console.log(yuJin);
const jiMin = new MaIdModel('jimin',1995);
console.log(jiMin);

console.log(`--------------`);
console.log(yuJin.dance());
console.log(yuJin.name);
console.log(jiMin.sing());


const cf = new IdModel('cdf',1992);
console.log(cf);

console.log(yuJin instanceof IdModel);
console.log(yuJin instanceof FeIdModel);
console.log(yuJin instanceof MaIdModel);
console.log(`--------------`);
console.log(cf instanceof IdModel);
console.log(cf instanceof FeIdModel);
console.log(cf instanceof MaIdModel);

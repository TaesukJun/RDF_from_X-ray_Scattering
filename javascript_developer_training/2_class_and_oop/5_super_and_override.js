/**
 * Super and OVerride
 * 
 */
class IdolModel{
    name;
    year;
    constructor(name, year){
        this.name = name;
        this.year = year;
    }
    sayHello(){
        return `hello, I am ${this.name}.`;
    }
}
class FemaleIdolModel extends IdolModel{
    // song / dance
    part;
    constructor(name, year, part){
        // this.name = name;
        // this.year = year;
        super(name, year);
        this.part = part;
    }
    sayHello(){
        // return `hello, I am ${this.name} with ${this.part} part`; //not super(name)
        return `${super.sayHello()} My part is ${this.part}.`; //not super(name)
    }
}

const yuJin = new FemaleIdolModel('an', 2003, 'vocal');
console.log(yuJin);
const wonYoung = new IdolModel('jang', 2002);
console.log(wonYoung.sayHello());
console.log(yuJin.sayHello());
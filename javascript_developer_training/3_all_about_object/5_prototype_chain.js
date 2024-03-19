/**
 * prototype
 * 
 */
const testObj ={};

// __proto__ exist in every object
// belong to parent class

console.log(testObj.__proto__);

function IdolModel(name, year){
    this.name = name;
    this.year = year;
}
console.log(IdolModel.prototype);

console.dir(IdolModel.prototype,{
    showHidden: true,
});

// circular reference
console.log(IdolModel.prototype.constructor === IdolModel);
console.log(IdolModel.prototype.constructor.prototype === IdolModel.prototype);


console.log(`-------------------------`);

const yuJin = new IdolModel('an', 2003);
console.log(yuJin.__proto__);
console.log(yuJin.__proto__ === IdolModel.prototype);
console.log(testObj.__proto__ === Object.prototype);

console.log(`-------------------------`);

console.log(IdolModel.__proto__ === Function.prototype);
console.log(Function.prototype.__proto__ === Object.prototype);
console.log(IdolModel.prototype.__proto__ === Object.prototype);

console.log(yuJin.toString());
console.log(Object.prototype.toString());

function IdolModel2(name,year){
    this.name = name;
    this.year = year;
    this.sayHello = function(){
        return `${this.name} is saying hello`;
    };
}
console.log(`-------------------------`);
const yuJin2 = new IdolModel2('an',2003);
const wy2 = new IdolModel2('jwy',2004);

console.log(yuJin2.sayHello());
console.log(wy2.sayHello());
console.log(yuJin2.sayHello === wy2.sayHello);

console.log(yuJin2.hasOwnProperty('sayHello'));

function IdolModel3(name,year){
    this.name = name;
    this.year = year;

}

IdolModel3.prototype.sayHello = function(){
    return `${this.name} is saying hello`;
}
const yuJin3 = new IdolModel3('an',2003);
const wy3 = new IdolModel3('jwy',2004);
console.log(`-------------------------`);
console.log(yuJin3.sayHello());
console.log(wy3.sayHello());
console.log(yuJin3.sayHello === wy3.sayHello);
console.log(yuJin3.hasOwnProperty('sayHello'));

console.log(`-------------------------`);

IdolModel3.sayStaticHello = function(){
    return `I am static method`;
}

console.log(IdolModel3.sayStaticHello());

/**
 * Overriding
 */

function IdolModel4(name,year){
    this.name = name;
    this.year = year;
    this.sayHello = function(){
        return `I am instant method`;
    };
}


IdolModel4.prototype.sayHello = function(){
    return `${this.name} is saying hello - prototype method`;
}

const yuJin4 = new IdolModel4('an',2003);

// prototype shadowing - class override
console.log(yuJin4.sayHello());

/**
 * getPrototypeOf, setPrototypeOf
 * 
 * changing instance __proto__ vs changing function prototype
 */
function IdolModel(name, year){
    this.name = name;
    this.year = year;
};

IdolModel.prototype.sayHello = function(){
    return `${this.name} is greeting.`;
};

function FemaleIdolModel(name, year){
    this.name = name;
    this.year = year;

    this.dance = function(){
        return `${this.name} is dancing.`;
    };
};

const gaEul = new IdolModel('gE',2004);
const ray = new FemaleIdolModel('ray',2004);

console.log(gaEul.__proto__);
console.log(gaEul.__proto__===IdolModel.prototype);
console.log(Object.getPrototypeOf(gaEul) === IdolModel.prototype);

console.log(gaEul.sayHello());
console.log(ray.dance());
console.log(Object.getPrototypeOf(ray)=== FemaleIdolModel.prototype);
// console.log(ray.sayHello());

Object.setPrototypeOf(ray,IdolModel.prototype);
console.log(ray.sayHello());
console.log(ray.constructor === FemaleIdolModel);
console.log(ray.constructor === IdolModel);
console.log(Object.getPrototypeOf(ray)=== FemaleIdolModel.prototype);
console.log(FemaleIdolModel.prototype === IdolModel.prototype);



console.log(`-------------------------`);

FemaleIdolModel.prototype = IdolModel.prototype;

const eSeo = new FemaleIdolModel('eSeo',2007);
console.log(Object.getPrototypeOf(eSeo)=== FemaleIdolModel.prototype);












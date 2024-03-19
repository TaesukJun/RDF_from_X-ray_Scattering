/**
 * Getter and Setter
 */
class IdolModel{
    name;
    year;

    constructor(name,year){
        this.name = name;
        this.year = year;


    }
    /**
     * 1) modify data nad return data
     * 2) return private value
     */
    get nameAndYear(){
        return `${this.name}-${this.year}`;



    }

    set setName(name){
        this.name = name;

    }




}

const yuJin = new IdolModel('an', 2003);
console.log(yuJin.nameAndYear);

yuJin.name = 'JWY';
console.log(yuJin);



class IdolModel2{
    #name;
    year;

    constructor(name,year){
        this.#name = name;
        this.year = year;
    }

    get name(){
        return this.#name;
    }

    set name(name){
        this.#name = name;
    }


}

const yuJin2 = new IdolModel2('an',2003);
console.log(yuJin2);

console.log(yuJin2.name);

yuJin2.name = 'cdf';
console.log(yuJin2.name);





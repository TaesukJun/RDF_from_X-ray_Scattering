/**
 * static keyword
 * 
 * 
 */

// class IdolModel{
//     name;
//     year;
//     static groupName = 'ive';
    

//     constructor(name,year){
//         this.name = name;
//         this.year = year;

        
//     }
//     static returnGroupName(){
//         return 'ive';
//     }


// }

// const yuJin = new IdolModel('an',2003);
// console.log(yuJin);
// console.log(IdolModel.groupName);
// console.log(IdolModel.returnGroupName());

/**
 * facory constructor
 */

class IdolModel{
    name;
    year;
    

    constructor(name,year){
        this.name = name;
        this.year = year;

    }
    static fromObject(object){
        return new IdolModel(
            object.name,
            object.year,
        );
    }

    static fromList(list){
        return new IdolModel(
            list[0],
            list[1],
        )
    }

}

const yuJin2 = IdolModel.fromObject({
    name: 'an',
    year: 2003,


});
console.log(yuJin2);

const wonYoung = IdolModel.fromList(
    [
        'JWY',
        2003,
    ]
)
console.log(wonYoung);
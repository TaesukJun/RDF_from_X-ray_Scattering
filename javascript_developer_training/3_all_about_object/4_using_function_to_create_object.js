/**
 * using function to create object
 */
function IdModel(name,year){
    if(!new.target){
        return new IdModel(name,year);
    }
    this.name=name;
    this.year=year;
    this.dance = function(){
        return `${this.name} is dancing`
    }
};
const yuJin = new IdModel('an',2003);
console.log(yuJin);
console.log(yuJin.dance());
console.log(`-----------------------------`);
const yuJin2 = IdModel('an2',2003);
console.log(yuJin2);
console.log(global.name); //global -> this
//if not using new keyword then it returns this => undefined which is false



// cannnot be used in arrow function

// const IdModelArrow = (name,year)=>{
//     if(!new.target){
//         return this ={};
//     }
//     this.name=name;
//     this.year=year;
// };
// const yuJin3 = IdModelArrow('an',2003);
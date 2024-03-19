/**
 * Objects
 */
// key : value
let yuJin ={
    name: "ahn",
    group: "ive",
    dance: function(){
        return `${this.name} is dancing.`;
    }

};

console.log(yuJin);
console.log(yuJin.name);
console.log(yuJin['name']);

const KEY = 'name';

console.log(yuJin[KEY]);

console.log(yuJin.dance());

const NameKey = 'name';
const NameValue = 'ahn';
const GroupKey = 'group';
const GroupValue = 'ive';

const YuJin2 = {
    [NameKey]: NameValue,
    [GroupKey]: GroupValue,
    dance: function(){
        return `${this.name} is dancing.`;
    }
};
console.log(YuJin2);

YuJin2['group'] = 'Jun';
console.log(YuJin2);

YuJin2['english']="AhnYuJun";
console.log(YuJin2);

delete YuJin2['english'];
console.log(YuJin2);

/**
 * Object Characteristics
 * 1) const => non-changable
 * 2) propety or method in object cannot be changed.
 */

const won = {
    name: 'won',
    group: 'ive',

};
console.log(won);

// won = {};

/**
 * get all key value
 */
console.log(Object.keys(won));

/**
 * get all value
 */

console.log(Object.values(won));


const name = 'ahn';
const YuJin3 = {
    name,
    name: name,
};
console.log(YuJin3);







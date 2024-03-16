/**
 * Exercise for class
 * 1) Country class <- country name and its idol group lnfo (name, idolGroup)
 * 2) IdolGroup class <- idol group name and member list (name,members)
 * 3) Idol class <- idol name and birth year (name, year)
 * 4) MaleIdol class <- same with Idol class + sing() function that returns string ${name} is singing.
 * 5) FemaleIdol class <= same with Idol class + dance() function that returns string ${name} is dancing.
 * 
 * use map() function
 */

// ive is korean girl (female) idol group)
const iveMembers = [
    {
        name: '안유진',
        year: 2003,
    },
    {
        name: '가을',
        year: 2002,
    },
    {
        name: '레이',
        year: 2004,
    },
    {
        name: '장원영',
        year: 2004,
    },
    {
        name: '리즈',
        year: 2004,
    },
    {
        name: '이서',
        year: 2007,
    },
]

// BTS is korean idol
// boy (male) group name is bts
const btsMembers = [
    {
        name: '진',
        year: 1992,
    },
    {
        name: '슈가',
        year: 1993,
    },
    {
        name: '제이홉',
        year: 1994,
    },
    {
        name: 'RM',
        year: 1994,
    },
    {
        name: '지민',
        year: 1995,
    },
    {
        name: '뷔',
        year: 1995,
    },
    {
        name: '정국',
        year: 1997,
    },
]

class Country{
    name;
    idolGroups;

    constructor(name, idolGroups){
        this.name = name;
        this.idolGroups = idolGroups;
    }
}

class IdolGroup{
    name;
    members;

    constructor(name, members){
        this.name = name;
        this.members = members;
    }
}

class Idol{
    name;
    year;

    constructor(name, year){
        this.name = name;
        this.year = year;
    }
}

class FemaleIdol extends Idol{
    sing(){
        return `${this.name} is singing.`;
    }
}

class MaleIdol extends Idol{
    dance(){
        return `${this.name}is dancing.`;
    }
}



const cIveMembers = iveMembers.map(
    (x) => new FemaleIdol(x['name'], x['year']),
);
console.log(cIveMembers);

// map function

const cBtsMembers = btsMembers.map(
    (x) => new MaleIdol(x['name'], x['year']),
);
console.log(cBtsMembers);



const iveGroup = new IdolGroup(
    'ive',
    cIveMembers,
)
console.log(iveGroup);



const btsGroup = new IdolGroup(
    'BTS',
    cBtsMembers,
);
console.log(btsGroup);



const korea = new Country(
    'korea',
    [
        iveGroup,
        btsGroup,
    ],
);
console.log(korea);




const allTogether = new Country(
    'korea',
    [
        new IdolGroup(
            'ive',
            iveMembers.map(
                (x) => new FemaleIdol(x['name'], x['year']),
            ),
        ),
        new IdolGroup(
            'bts',
            btsMembers.map(
                (x) => new MaleIdol(x['name'], x['year']),
            ),
        ),
    ],
);
console.log(allTogether);


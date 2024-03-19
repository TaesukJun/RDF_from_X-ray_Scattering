// for loop

for (let i = 0; i < 12; i++) {
    console.log(i);
    
}
console.log('---------------------')

for (let i = 10; i > 0; i--) {
    console.log(i);
    
}
console.log('---------------------')

for (let i = 0; i < 10; i++) {
    for (let j = 10-i; j > 0; j--) {
        console.log(i,j);
        
    }
    
}

squareLength = 6;
let squareShape;

for (let i = 0; i < squareLength; i++) {
    squareShape = ''
    for (let j = 0; j < squareLength; j++) {
        if (i == 0 || i == squareLength-1 || (j == 0) || (j == squareLength-1)) {
            squareShape = squareShape + '*';
        }else {
            squareShape = squareShape + ' ';
        }
        
    }
    console.log(squareShape)
}

console.log('---------------------')


const appKey = {
    name: 'hi',
    year: 2003,
    group: "gigantic"
}

for (const key in appKey) {
    console.log(key)
}

console.log('---------------------')

const junArray = ['a','b','c','d','e']

for (const key in junArray) {
    console.log(key);
    console.log(`${key} is ${junArray[key]}`);
}

console.log('---------------------')

for (const value of junArray) {
    console.log(value);
    
}

//While loop

let number = 0;

while (number < 10) {
    number ++;
    console.log(number)
    
}
console.log('---------------------')
//do while loop


number =0;

do {
    number ++;
    console.log(number)
} while (number < 10);
console.log('---------------------')

//break

for (let t = 0; t < 12; t++) {
    console.log(t+'before');
    if (t ==5) {
        break;
        
    }
    console.log(t+'after');
}
console.log('---------------------')
//continue

for (let t = 0; t < 5; t++) {
    console.log(t+'before');
    if (t ==3) {
        continue;
        
    }
    console.log(t+'after');
}
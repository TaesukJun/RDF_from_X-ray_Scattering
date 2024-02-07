/**type conversion 
 * 1) explict
 * 2) implict
 * 
*/
let age = 32;

// explict
let stringAge = age.toString();
console.log(typeof stringAge, stringAge);
let kate01 = true.toString();
console.log(typeof kate01, kate01);
let kate02 = (Infinity).toString();
console.log(typeof kate02, kate02);

let kate03 = parseInt('12.22');
console.log(typeof kate03, kate03);
let kate04 = parseFloat('12.22');
console.log(typeof kate04, kate04);
let kate05 = +'1';
console.log(typeof kate05, kate05);

console.log('------------------------');

kate05 = !'x'
console.log(typeof kate05, kate05);
kate05 = !!'x'
console.log(typeof kate05, kate05);
kate05 = !!''
console.log(typeof kate05, kate05);
kate05 = !!0
console.log(typeof kate05, kate05);
kate05 = !!'0'
console.log(typeof kate05, kate05);
kate05 = !!'false'
console.log(typeof kate05, kate05);
kate05 = !!false
console.log(typeof kate05, kate05);
kate05 = !!undefined
console.log(typeof kate05, kate05);
kate05 = !!null
console.log(typeof kate05, kate05);
// Array and Object are always true evenif they are empty
kate05 = !!{}
console.log(typeof kate05, kate05); 
kate05 = !![]
console.log(typeof kate05, kate05); 

console.log('------------------------');

// implict - automatically change the type
// not recommended because it may cause bug or hard to understand the code
let test = age + ' ';
console.log(typeof test, test);
console.log('98'+2); // in this case 2 become string
console.log('98'*2); // in this case 98 become int
console.log('98'-2); // in this case 98 become int




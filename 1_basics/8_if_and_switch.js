/**
 * If and Switch
 * 
 */
let number = 5;

if (number % 2 === 0){
    console.log('hihi')

}else {
    console.log('hill')
}

if (number % 2 === 0){
    console.log('hihi')
}else if (number % 3 === 0) {
    console.log('hill')
}else if (number % 5 === 0) {
    console.log('hill02')
}else {
    console.log('what are you doing?')
}
console.log('-----------------------')
const englishDay = 'monday2';
let keyCard;

switch (englishDay) {
    case 'monday':
        keyCard = 'J';
        break;
    case 'tuesday':
        keyCard = 'J02';
        break;
    case 'wednesday':
        keyCard = 'J03';
        break;
    case 'thursday':
        keyCard = 'J04';
        break;

    default:
        keyCard = 'J0448';
        break;
}

console.log(keyCard)
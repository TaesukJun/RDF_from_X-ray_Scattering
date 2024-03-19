/**
 * try... catch
 * 1) error occur -> throw
 * 2) recognize erro -> catch
 */

function runner(){

    try{
        console.log('hello');
    
        throw new Error('BigBigBig');
    
        console.log('jun');





    } catch(e){
        console.log("---catch---");
        console.log(e);

    } finally {//run anyway anycase
        console.log('---finally----');



    }




}

runner();
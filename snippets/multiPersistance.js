//given a number(integer) calculate the multiplicative persistance
function multiPersistance(num) {
    if(num/10 < 1)
        return 0;

    //calculate the product of all digits
    let multDigits = 1;
    for(let i = 0; i < num.toString().length; i++) {
        multDigits*=new Number(num.toString()[i]);
    }

    return multiPersistance(multDigits) + 1
}

//should be 3
console.log(multiPersistance(39)); 

//should be 10
console.log(multiPersistance(3778888999));  

//should be 11
console.log(multiPersistance(277777788888899)); 

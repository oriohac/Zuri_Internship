

// function return_values(n) {
//     let result = "";
//     //let is_countable_object;
//     //check  that the parameter is countable
//     //is_countable_object = check_countable_true(array)
//     if(is_multiple_parameter(array)) return "only one parameter allowed";
//     if(!check_countable_true(array)) return "invalid parameter supplied";
//     if (!check_size_correct(array)) return "parameter is too large"

//     //do for loop
//     array.forEach(element => {
        
//     });

//     for (let i = 0; i < array.length; i++) {
//         result += "array position" + i +"- is" + array[i];
        
//     }
//     console.log(final_result? final_result: "error");
//     //display value
//     //return string
// }

function return_values(array) {


    let result = "";
    //let is_countable_object;
    //check  that the parameter is countable
    //is_countable_object = check_countable_true(array)
    if(arguments.length > 1) return "only one parameter allowed";
    if(!check_countable_true(array)) return "invalid parameter supplied";
    if (!check_size_correct(array)) return "parameter is too large"

    //do for loop
    // array.forEach(element => {
        
    // });

    for (let i = 0; i < array.length; i++) {
        result += "array position " + i +" - is " + array[i]+"\n";
        
    }
    //display value
    return result
    //display value
    //return string
}

function check_countable_true(array) {
    return true;

}

// function is_multiple_parameter(array) {
//     return true;
// }

function check_size_correct(array) {
    return true;
}

//console.log(return_values(["mike","seyi",4]))
console.log(return_values(["a","b",["1","2","3"]]))
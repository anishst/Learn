// RTN Generator Function
function random_number(min, max) {
    var random_num = Math.floor(Math.random() * (+max - +min)) + +min;
    return random_num
}

function validate_rtn(cRTN) {
    cRTN = cRTN.toString();
    // Run through each digit and calculate the total.
    n = 0;
    for (i = 0; i < cRTN.length; i += 3) {
        n += parseInt(cRTN.charAt(i), 10) * 3
            + parseInt(cRTN.charAt(i + 1), 10) * 7
            + parseInt(cRTN.charAt(i + 2), 10);
    }
    // If the resulting sum is an even multiple of ten (but not zero),
    // the aba routing number is good.
    if (n != 0 && n % 10 == 0)
        return true;
    else
        return false;
} // end ValidateRTN funciton;


function create_rtn() {
    /* The first two digits of the nine digit RTN must be in the ranges 00 through 12, 
    21 through 32, 61 through 72, or 80.
    https://en.wikipedia.org/wiki/ABA_routing_transit_number */
    d1 = 1
    d2 = 2
    d3 = random_number(1, 9)
    d4 = random_number(1, 9)
    d5 = random_number(1, 9)
    d6 = random_number(1, 9)
    d7 = random_number(1, 9)
    d8 = random_number(1, 9)
    d9 = random_number(1, 9)

    validateRTN = (3 * (d1 + d4 + d7) + 7 * (d2 + d5 + d8) + d3 + d6 + d9)
    
    while (validateRTN % 10 != 0) {
        d3 = Math.floor((9 * Math.random()) + 1)
        d4 = Math.floor((9 * Math.random()) + 1)
        d5 = Math.floor((9 * Math.random()) + 1)
        d6 = Math.floor((9 * Math.random()) + 1)
        d7 = Math.floor((9 * Math.random()) + 1)
        d8 = Math.floor((9 * Math.random()) + 1)
        d9 = Math.floor((9 * Math.random()) + 1)
        validateRTN = (3 * (d1 + d4 + d7) + 7 * (d2 + d5 + d8) + d3 + d6 + d9)
    }
    // console.log(d1, d2, d3, d4, d5, d6, d7, d8, d9)

    rtn = "" + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    console.log("RTN generated is: " + rtn)
    return rtn



}

create_rtn()
console.log(validate_rtn(create_rtn()))

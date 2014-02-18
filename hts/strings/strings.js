

var primes_dict = [2,3,5,7];
var string = $("input").first().val();
var primes = [];
var comps = [];
var alpha = [];

for( var i = 0; i < string.length; i++ ){
    var c = string[i];
    if(parseInt(c)){
	c = parseInt(c)
	if( c != 0 && c != 1 ){
	    if( primes_dict.indexOf(c) != -1 ){
		primes.push(c);
	    }
	    else{
		comps.push(c);
	    }
	}
    }
    else{
	if( alpha.length < 25 ){
	    alpha.push(String.fromCharCode(c.charCodeAt(0) +1 ));
	}
    }
}
var p = 0;
var c = 0;
for(var i = 0; i < primes.length; i++){
    p += primes[i];
}

for(var i = 0; i < comps.length; i++){
    c += comps[i];
}

var numerics = p*c;
$("input[name=solution]").val(alpha.join('') + numerics);
$("input:last").click();
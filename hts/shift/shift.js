

function doshift( data ){
    var currentnum = "";
    var currentchar = "";
    var complete = "";
    for( var j = 0; j < data.length; j++ ){
	var c = data[j];
	if( parseInt(c) >= 0 ){
	    currentnum += c;
	}
	else{
	    complete += String.fromCharCode(parseInt(currentnum) - shift);
	    //complete += String.fromCharCode(c.charCodeAt(0)+shift);
	    currentnum = "";
	}
    }
    return complete;
}


var text = $("td.sitebuffer").children("table").children("tbody").children("tr:last").prev().children("td:last").prev().text();
var data = "";
var i = 186;
for( i; text[i] != 'S'; i++ ){
    data += text[i];
}
i += 7;

var shift = "";
while( text[i] != 'D' ){
    shift += text[i];
    i += 1;
}
shift = parseInt(shift);


$("input[name=solution]").val(doshift(data));
$("input[name=submitbutton]").click();
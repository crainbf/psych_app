var COLORS = new Array(
	"red",
	"blue",
	"green"
);

var TEXT = new Array(
	"RED",
	"BLUE",
	"GREEN"
);

$(document).ready(function(){
	$('#start').click(start);
});

function start() {
	stimColor = Math.floor(3*Math.random());
	$('#stimulus').css('color', COLORS[stimColor]);
	$('#stimulus').html('Hello');

	// $('#red').click(response);
	// $('#blue').click(response);
}

function response() {
	if ('red' === COLORS[stimColor]) {
		$('#response').html('The answer is correct.');
	} else {
		$('#response').html('The answer is NOT correct.');
	}

}
// $(document).ready(function(){
// 	//$('input[type="button"][value="red"]').click(function(){ 
// 	$('div').mouseenter(function(){
// 		$('div').hide();
// 	});



// 	//alert('hello');
// 	//$('#stimulus').fadeOut(1000);
// });


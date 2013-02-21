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


var num_correct = 0;
var num_trials = 0;
var trials = new Array();


$(document).ready(function(){
	$('#start').click(start);
});

function start() {
	//hide start button
	$('#start').hide();

	//write hello in random color
	stimColor = Math.floor(3*Math.random());
	$('#stimulus').css('color', COLORS[stimColor]);
	$('#stimulus').html('Hello');

	//increment trial by 1 and write to counter
	num_trials++;
	$('#num_trials').html(num_trials);

	//record start time
	var d = new Date();
	start_time = d.getTime();
}

function response(clicked_id) {
	if (clicked_id === COLORS[stimColor]) {
		//create trial object
		var trial ={
			duration: get_duration(),
			stimulus_color: COLORS[stimColor],
			correct: true
		};

		$('body').data('duration', get_duration())

		//Save the duration to an array
		trials[num_trials-1] = trial;

		$('#response').html('The answer is correct.');
		num_correct++;

		$('#score').html(num_correct+' out of '+num_trials);
		start();

	} else {
		//create trial object
		var trial ={
			duration: get_duration(),
			stimulus_color: COLORS[stimColor],
			correct: false
		};
		//Save the duration to an array
		trials[num_trials-1] = get_duration();
		
		$('#response').html('The answer is NOT correct.');

		$('#score').html(num_correct+' out of '+num_trials);
		start();
	}

}

function get_duration(){
	//gets trial duration
	var d = new Date();
	var end_time = d.getTime();
	trial_duration =  end_time - start_time;

	//prints duration to screen
	$('#trial_duration').html(trial_duration);
	return trial_duration
}



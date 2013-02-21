/*global $, document*/

var COLORS = ["red", "blue", "green"];

var TEXT = ["RED", "BLUE", "GREEN"];

var num_correct = 0;
var num_trials = 0;
var trials = [];
var stimColor, start_time;

function start() {
	"use strict";
	//hide start button
	$('#start').hide();

	//write hello in random color
	stimColor = Math.floor(3 * Math.random());
	$('#stimulus').css('color', COLORS[stimColor]);
	$('#stimulus').html('Hello');

	//increment trial by 1 and write to counter
	num_trials += 1;
	$('#num_trials').html(num_trials);

	//record start time
	start_time = Date.now();
}

$(document).ready(function () {
	"use strict";
	$('#start').click(start);
});

function get_duration() {
	"use strict";
	//gets trial duration
	var trial_duration =  Date.now() - start_time;

	//prints duration to screen
	$('#trial_duration').html(trial_duration);
	return trial_duration;
}


function response(clicked_id) {
	"use strict";
	var trial = {
		duration: get_duration(),
		stimulus_color: COLORS[stimColor]
	};

	if (clicked_id === COLORS[stimColor]) {
		trial.correct = true;
		num_correct += 1;

		//Save the trial to the trials array
		trials[num_trials - 1] = trial;

		$('#response').html('The answer is correct.');
		$('#score').html(num_correct + ' out of ' + num_trials);

		start();

	} else {
		trial.correct = false;
		//Save the trial to the trials array
		trials[num_trials - 1] = trial;

		$('#response').html('The answer is NOT correct.');
		$('#score').html(num_correct + ' out of ' + num_trials);

		start();
	}

}

//Not actually using this function yet. 
function interrupt() {
	"use strict";

	$('#stimulus').html('');
}




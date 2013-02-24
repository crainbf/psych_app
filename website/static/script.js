/*global $, document, setTimeout, console*/

//http://rohanradio.com/blog/2011/02/22/posting-json-with-jquery/
jQuery.extend({
	postJSON: function(params) {
		return jQuery.ajax(jQuery.extend(params, {
			type: "POST",
			data: JSON.stringify(params.data),
			dataType: "json",
			contentType: "application/json",
			processData: false
		}));
	}
});

//https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax
function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	crossDomain: false,
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type)) {
			xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
		}
	}
});

var COLORS = ["red", "blue", "green"];

var TEXT = ["RED", "BLUE", "GREEN"];

var num_correct = 0;
var num_trials = 0;
var trials = [];
var stimColor, start_time;
var max_trials = 3;

function start() {
	"use strict";

	//write hello in random color
	stimColor = Math.floor(3 * Math.random());
	$('#stimulus').css('color', COLORS[stimColor]);
	$('#stimulus').html(TEXT[stimColor]);

	//increment trial by 1 and write to counter
	num_trials += 1;
	$('#num_trials').html(num_trials);

	//record start time
	start_time = Date.now();
}

function hide_start() {
	"use strict";
	$('#start').hide();
	start();

}

$(document).ready(function () {
	"use strict";
	$('#start').click(hide_start);
});

function get_duration() {
	"use strict";
	//gets trial duration
	var trial_duration =  Date.now() - start_time;

	//prints duration to screen
	$('#trial_duration').html(trial_duration);
	return trial_duration;
}

function submit_answers() {
	$.postJSON({
		url: '/trial/',
		data: trials,
	});
}


function response(clicked_id) {
	"use strict";
	var trial = {
		duration: get_duration(),
		stimulus_color: COLORS[stimColor],
		response_color: clicked_id
	};
	trials[num_trials - 1] = trial;

	$('#score').html(num_correct + ' out of ' + num_trials);
	
	if (clicked_id === COLORS[stimColor]) {
		num_correct += 1;
		
		$('#response').html('The answer is correct.');
		//Clear stimulus
		$('#stimulus').empty();

	} else {

		$('#response').html('The answer is NOT correct.');
		//clear stimulus
		$('#stimulus').empty();
	}

	if (num_trials == max_trials)
		submit_answers();
	setTimeout(start, 1500);
}

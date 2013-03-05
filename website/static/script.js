/*global $, document, setTimeout, console*/

function ajaxSetup() {
    function ajaxSetupCsrf() {
        //http://rohanradio.com/blog/2011/02/22/posting-json-with-jquery/
        $.extend({
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
    }

    if ($.cookie('csrftoken') == null) {
        $.ajax({
            type: 'GET',
            url: '/csrf/',
            tryCount: 0,
            retryLimit: 3,
            success: ajaxSetupCsrf,
            error: function() {
                this.tryCount++;
                if (this.tryCount <= this.retryLimit) {
                    $.ajax(this);
                }
            }
        });
    } else {
        ajaxSetupCsrf();
    }
}

var COLORS = ["red", "blue", "green"];

var TEXT = ["RED", "BLUE", "GREEN"];

var num_correct = 0;
var num_trials = 0;
var trials = [];
var stimColor, stimWord, start_time;
var max_trials = 3;

function start() {
    "use strict";

    //reenable stimulus buttons
    $('#red, #blue, #green').removeAttr("disabled");

    //write hello in random color
    stimColor = Math.floor(3 * Math.random());
    stimWord = Math.floor(3 * Math.random());

    $('#stimulus').css('color', COLORS[stimColor]);
    $('#stimulus').html(TEXT[stimWord]);

    //increment trial by 1 and write to counter
    num_trials += 1;
    $('#num_trials').html(num_trials);

    //record start time
    start_time = Date.now();
}

function hide_start() {
    "use strict";
    //disable start button
    $('#start').attr("disabled", "disabled");
    start();
}

$(document).ready(function () {
    "use strict";
    $('#red, #blue, #green').attr("disabled", "disabled");
    $('#start').click(hide_start);
    ajaxSetup();
});

function get_duration() {
    "use strict";
    //gets trial duration
    var trial_duration =  Date.now() - start_time;

    //prints duration to screen
    $('#trial_duration').html(trial_duration);
    return trial_duration;
}

// http://stackoverflow.com/questions/10024469/whats-the-best-way-to-retry-an-ajax-request-on-failure-using-jquery/10024557#10024557
function submit_answers() {
    "use strict";
    $.postJSON({
        url: '/trial/',
        tryCount : 0,
        retryLimit : 3,
        data: trials,
        success : function(data) {
            window.location = '/trial/';
        },
        error : function(xhr, textStatus, errorThrown ) {
            if (textStatus == 'timeout') {
                this.tryCount++;
                if (this.tryCount <= this.retryLimit) {
                    //try again
                    $.ajax(this);
                    return;
                }
                return;
            }
            if (xhr.status == 500) {
                //handle error
            } else {
                //handle error
            }
        }
    });
}


function response(clicked_id) {
    "use strict";
    var trial = {
        duration: get_duration(),
        stimulus_color: COLORS[stimColor],
        stimulus_word: stimWord,
        response_color: clicked_id
    };
    trials.push(trial);

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
    //temporarily disable stimulus buttons
    $('#red, #blue, #green').attr("disabled", "disabled");

    if (num_trials == max_trials)
        submit_answers();
    setTimeout(start, 1500);
}

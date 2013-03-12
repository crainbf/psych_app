function delay_redir() {
    "use strict";
    window.location = "/trial/";
}


$(document).ready(function(){
    "use strict";
    setTimeout('delay_redir()', 3000);
});
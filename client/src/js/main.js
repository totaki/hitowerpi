//= vars.js

var Notifier = {
	send: function(msg) {
		document.getElementById(notifierId).innerHTML = msg;
	}
}

//= io.js
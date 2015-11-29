//= vars.js
var clientApp;

var Notifier = {
	send: function(msg) {
		document.getElementById(notifierid).innerHTML = msg;
	}
}

//= io.js
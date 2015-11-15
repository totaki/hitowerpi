var ioStr = function(str) { return 'io-' + str; }

var ClassState = new Object();

ClassState.set = function(elem, state) {
	var cls = elem.classList;
	var chg = function(state) {
		return (state && ioStr('down')) || (!state && ioStr('up'));
	}
	cls.remove(chg(state));
	cls.add(chg(!state));
}

ClassState.create = function(io, pin) {
	var elem = document.createElement('div')
	elem.classList.add(ioStr(io));
	elem.setAttribute('id', ioStr(pin));
	if (io === "outputs") {
		elem.setAttribute('onclick', 'IOs.change(this.id)');
	}
	return elem;
}

var IOs = function () {
	this.address = '/js/devdata/io.json';
}

IOs.prototype.request = function () {
	var ios = this;
	return (function() {
		var req = new XMLHttpRequest();
		req.onreadystatechange = function() {
			if (req.readyState == 4 && req.status == 200) {
				var response = JSON.parse(req.responseText);
				ios.successResponse(response)
			}
		}
		req.open("GET", ios.address, true);
		req.send()
	})();
}

IOs.prototype.get = function (pin) {
}

IOs.prototype.change = function (pin) {
	// This function make post request to server
	// if OK websocket call onSet method
	Notifier.send(pin);
}

IOs.prototype.onChange = function (pin) {
	// This function set output state
}

IOs.prototype.create = function (io, pin, data) {
	var elem = document.createElement('div');
	var status = ClassState.create(io, pin);
	ClassState.set(status, data.state);
	elem.appendChild(status);
	elem.appendChild(document.createElement('div'));
	elem.lastChild.innerHTML = data.name;
	return elem;
}

IOs.prototype.successResponse = function (data) {
	var parent = document.getElementById(workspaceId);
	parent.innerHTML = '';
	for (var key in data) {
		for (var pin in data[key]) {
			parent.appendChild(IOs.create(key, pin, data[key][pin]));
		}
	}
}

var IOs = new IOs();


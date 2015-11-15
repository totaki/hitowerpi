function createDivWithText(text) {
	var elem = document.createElement('div');
	elem.appendChild(document.createElement('p'))
		.appendChild(document.createTextNode(text));
	return elem;
}

var ioplus = function(str) { return 'io-' + str; }

var ioclass = {
	name: ioplus('name'),
	state: ioplus('state'),
	desc: ioplus('desc'),
	up: ioplus('up'),
	down: ioplus('down')
}

function IO(kind, num, data) {
	this.kind = kind;
	this.num = num;
	this.data = data;
}

IO.prototype.createParentElem = function () {
	this.parent = document.createElement('div');
	this.parent.classList.add(ioplus(this.kind));
	this.parent.setAttribute('id', ioplus(this.num));
	return this;
}

IO.prototype.appendNameElem = function () {
	this.parent.appendChild(createDivWithText(this.data.name));
	this.parent.lastChild.classList.add(ioclass.name);
	return this;
}

IO.prototype.appendStateElem = function () {
	this.parent.appendChild(document.createElement('div'));
	this.parent.lastChild.classList.add(
		ioclass.state, 
		(this.data.state && ioclass.up) || (!this.data.state && ioclass.down)
	)
	if (this.kind === "outputs") {
		this.parent.lastChild.setAttribute('onclick', 'ios.change(this)');
	}
	return this;
}

IO.prototype.appendDescElem = function () {
	this.parent.appendChild(createDivWithText(this.data.description));
	this.parent.lastChild.classList.add(ioclass.desc);
	return this;
}

IO.prototype.createDOM = function () {
	this.createParentElem().appendNameElem()
		.appendStateElem().appendDescElem();
	return this.parent;
}

function IOs(address) {
	this.address = address;
}

IOs.prototype.request = function () {
	var req = new XMLHttpRequest();
	var caller = this;
	req.onreadystatechange = function() {
		if (req.readyState == 4 && req.status == 200) {
			var response = JSON.parse(req.responseText);
			caller.successResponse(response)
		}
	}
	req.open("GET", this.address, true);
	req.send();
}

IOs.prototype.get = function (pin) {
}

IOs.prototype.change = function (node) {
	// This function make post request to server
	// if OK websocket call onSet method
	Notifier.send('IO '+ node.parentNode.id +' change state' );
}

IOs.prototype.onChange = function (pin) {
	// This function set output state
}

IOs.prototype.successResponse = function (data) {
	var parent = document.getElementById(workspaceid);
	parent.innerHTML = '';
	for (var kind in data) {
		for (var num in data[kind]) {
			parent.appendChild(new IO(kind, num, data[kind][num]).createDOM());
		}
	}
}

var ios = new IOs('/js/devdata/io.json');

var workspaceid = 'workspace';
var notifierid = 'notifier';
var clientApp;

var Notifier = {
	send: function(msg) {
		document.getElementById(notifierid).innerHTML = msg;
	}
}

function createDivWithText(text) {
	var elem = document.createElement('div');
	if (text) {
		elem.appendChild(document.createElement('p'))
			.appendChild(document.createTextNode(text));
	}
	return elem;
}

var ioplus = function(str) { return 'io-' + str; }
var iominus = function(str) { return str.slice(3); }

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
	if (this.kind === 'outputs') {
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

IO.changeState = function (data) {
	for (var i in data) {
		var elem = document.getElementById(ioplus(i))
			.getElementsByClassName(ioclass.state)[0];
		elem.classList.toggle(ioclass.up);
		elem.classList.toggle(ioclass.down);
	}
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
	req.open('GET', this.address, true);
	req.send();
	clientApp = 'io'
}

IOs.prototype.get = function (pin) {
}

IOs.prototype.change = function (node) {
	var req = new XMLHttpRequest();
	var caller = this;
	req.onreadystatechange = function() {
		if (req.readyState == 4 && req.status == 200) {
			var response = JSON.parse(req.responseText);
			caller.onChange(response)
		}
	}
	req.open('POST', this.address, true);
	req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	req.send('io=' + iominus(node.parentNode.id));
}

IOs.prototype.onChange = function (response) {
	var msg;
	if (response.error) {	msg = response.error;	}
	else {
		msg = response.message;
		if (clientApp === response.app) {
			IO.changeState(response.data);
		}
	}
	Notifier.send(msg);
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

var ios = new IOs('http://localhost:9999/api/0.1/io');
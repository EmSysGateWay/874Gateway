var express = require('express');
var app = express();
var bodyParser = require('body-parser')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ 
  extended: true
})); 

var title = '<h1><meta charset="utf-8"> 一个非常简单的页面</meta></h1>\n';
var report = {
    time: '-',
    "auth_id": "",
    "auth_key": "",
    "device_id": ""
}
var poll = {
    time: '-',
    "auth_id": "",
    "auth_key": "",
    "device_id": ""
}

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/report', function (req, res) {
    res.json(report);
});

app.get('/poll', function (req, res) {
    res.json(poll);
});

app.post('/api/report', function (req, res) {
    console.log(req.body);
    var d = new Date();
    report['time'] =  d.toDateString() + ' ' + d.toTimeString();
    report['auth_id'] = req.body['auth_id'];
    report['auth_key'] = req.body['auth_key'];
    report['device_id'] = req.body['device_id'];
    res.send('OK');
});

app.post('/api/poll', function (req, res) {
    console.log(req.body);
    var d = new Date();
    poll['time'] = d.toDateString() + ' ' + d.toTimeString();
    poll['auth_id'] = req.body['auth_id'];
    poll['auth_key'] = req.body['auth_key'];
    poll['device_id'] = req.body['device_id'];
    res.send('OK');
});

app.listen(80, function () {
    console.log('App listening on port 80!');
});
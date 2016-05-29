var express = require('express');
var app = express();
var bodyParser = require('body-parser')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}));

var title = '<h1><meta charset="utf-8"> 一个非常简单的页面</meta></h1>\n';
var report = {
    "auth_id": "",
    "auth_key": "",
    "device_id": ""
}
var poll = {
    "auth_id": "",
    "auth_key": "",
    "device_id": ""
}

var message = [];

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.post('/report', function (req, res) {
    res.json(report);
});

app.post('/poll', function(req, res){
    message.push(req.body);
    console.log('after poll', message);
})

app.post('/api/report', function (req, res) {
    console.log(req.body);
    var d = new Date();
    report['update_time'] = d.toDateString() + ' ' + d.toTimeString();
    //show report content
    report['auth_id'] = req.body['auth_id'];
    report['auth_key'] = req.body['auth_key'];
    report['device_id'] = req.body['device_id'];
    report['payload'] = req.body['payload'];
    res.send('OK');
});

app.post('/api/poll', function (req, res) {

    if(req.body['device_id'] == '869'){
        if(req.body['payload']['RequestType'] == 'auth' ){
            res.status(200).json({
                code:0,
                ResponseType:'auth',
                DeviceId:'869',
                Ids:[
                    {id:'id1'},
                    {id:'id2'}
                ]
            });
        }
        else if(req.body['payload']['RequestType'] == 'upload' ){
            res.status(200).json({
                code:0,
                ResponseType:'upload',
                DeviceId:'869',
                Success:'y'
            });
        }
        else
            res.sendStatus(403);
    }
    else
        res.sendStatus(403);
});

app.listen(80, function () {
    console.log('App listening on port 80!');
});
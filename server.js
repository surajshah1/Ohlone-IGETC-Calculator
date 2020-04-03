require('babel-register') ({
    presets: ['react']
});

const express = require("express");
const bodyParser = require("body-parser");
const multer = require("multer");
const fs = require('fs');
var upload = multer();
var {PythonShell} = require('python-shell');
var React = require('react');
var ReactDOMServer = require('react-dom/server');
var CalcComponent = require('./calculationoutput.jsx');

var app = express();
var courses = [];
var port = process.env.PORT || 8080;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/views'));
app.use(upload.array());

//home endpoint
app.get('/', (req, res) => {
    fs.writeFile('outputclasses.json', JSON.stringify({}));
    res.render("index.html");
});

//add class endpoint
app.post('/courses', (req, res) => {
    console.log(req.body.course);
    courses.push(req.body.course.toUpperCase());
  });

//calculate endpoint
app.get('/calculation', calculate);

//TODO: make this endpoint
app.delete('/delete', () => {
    courses.pop();
});

//start app on 'port'
app.listen(port,() => {
    console.log("Started on port " + port);
});

/*
app.get('/test', (req,res) => {
    res.sendFile('output.html', {root : __dirname + '/views'});
});
*/

function calculate(req, res) {
    var options = {
        args: [JSON.stringify(courses)]
    };

    console.log(JSON.stringify(courses))
    PythonShell.run('igetccalculation.py', options, function (err, data) {
            if (err) {
                console.log(err)
            }
            courses = []
            console.log("python script output:" + data);
            var output = fs.readFileSync("outputclasses.json");
            var areaobj = JSON.parse(output);
            //console.log(areaobj)
            //clear .json
            fs.writeFileSync("./outputclasses.json", "{}");
            var html = ReactDOMServer.renderToString(React.createElement(CalcComponent, {areaobj}, null));
            res.send(html);
        }
    );
}

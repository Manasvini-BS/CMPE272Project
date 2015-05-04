var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index');
});

router.get('/login', function(req, res) {
	  res.render('login');
});

router.get('/signup', function(req, res) {
	  res.render('signup');
});

router.get('/calculator', function(req, res) {
	  res.render('calculator');
});
router.get('/getDriverId', function(req, res) {
	  
	  var driverId = req.query.driverId;
	  console.log(' Request received  : '+driverId);
	  
		var pythonshell=require('python-shell');
		var result;	
		var option = {
        	mode: 'text',
        	pythonPath: '/usr/bin/python',
        	pythonOptions: ['-u'],
        	args: [driverId]
		};
		pythonshell.run('main.py',option, function(err,results){
        	if(err) throw err;
        	console.log('finish: %j',results);
        	result = results[0];
        	console.log('finish: ',result);
        	console.log('Returninig  : '+result)
			var returnVal = result;
			console.log('Returninig  : '+returnVal)
	  		res.send(returnVal);

		});
	});
module.exports = router;

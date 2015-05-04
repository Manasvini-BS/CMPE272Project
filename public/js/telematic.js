
function getDriverValue(driverId){
	var pythonshell=require('python-shell');

	var option = {
        mode: 'text',
        pythonPath: '/usr/bin/python',
        pythonOptions: ['-u'],
        args: [driverId]
	};
	pythonshell.run('temp.py',option, function(err,results){
        if(err) throw err;
        console.log('finish: %j',results);
	});
	return results[0];
}
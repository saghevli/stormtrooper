var system = require('system');
var args = system.args;
if (system.args.length != 2) {
    console.log('Usage: <site1>');
}

var url = args[1];
var page = require('webpage').create();
page.open(url, function (status) {
      //Page is loaded!
      console.log(url + " successfully loaded");
      phantom.exit();
});

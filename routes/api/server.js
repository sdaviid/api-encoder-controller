const express = require('express');
const router = express.Router();


var authCheck = require('../auth');
var server_controller = require('../../controllers/server');




router.post('/create', authCheck.authenticated, authCheck.validateRoles(['admin', 'server']), server_controller.create);
//router.get('/list', authCheck.authenticated, authCheck.validateRoles(['admin', 'server', 'user']), server_controller.list);


module.exports = router;
var router = require('express').Router();


router.use('/server', require('./api/server'));
router.use('/file', require('./api/file'));

module.exports = router;
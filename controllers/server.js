const Sequelize = require('sequelize');
const utils = require('../utils/utils');
const ServerModel = require('../models/server');

const config = require('../config.json');
const path = require('path');


exports.create = async function(req, res){
  const uri = req.body.uri;
  try{
    const resultCreateFile = await ServerModel.create({uri: uri});
    if(resultCreateFile){
      res.status(200)
          .json(
            {
              status: 200,
              message: null,
              data: resultCreateFile
            }
          )
    }else{
      res.status(400)
          .json(
            {
              status: 400,
              message: 'failed add server'
            }
          )
    }
  }catch(err){
    res.status(500)
        .json(
          {
            status: 500,
            message: 'Exception add server',
            detail: err
          }
        )
  }
}
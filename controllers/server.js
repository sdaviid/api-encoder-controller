const Sequelize = require('sequelize');
const utils = require('../utils/utils');
const ServerModel = require('../models/server');

const service_auth = require('../service/auth');
const service_encoder = require('../service/encoder-server');

const config = require('../config.json');
const path = require('path');


exports.status = async function(req, res){
  try{
    const resultStatusServer = await ServerModel.findAll();
    if(resultStatusServer){
      if(resultStatusServer.length>0){
        service_auth.create_token('cli-web-encoder').then(function(response){
          if(response.status == 200){
            temp = [];
            resultStatusServer.forEach(async function(item){
              let desgracado = await service_encoder.list_line(item.uri, response.data.access_token).then(function(temp_line){
                console.log(temp_line);
                console.log(temp_line.pending_download);
                temp.push({server: item.uri, pending_download: temp_line.pending_download});
                console.log(temp_line);
                return {server: item.uri, pending_download: temp_line.pending_download};
              })
              temp.push(desgracado);
            });
            res.status(200)
              .json(
                {
                  status: 200,
                  message: null,
                  data: temp
                }
              )
          }
        })
      }
      
    }else{
      res.status(400)
        .json(
          {
            status: 400,
            message: 'couldnt get servers status'
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

exports.create = async function(req, res){
  console.log('create');
  const uri = req.body.uri;
  console.log(uri);
  try{
    service_auth.create_token('cli-web-encoder').then(function(token){
      console.log(token);
      if(token.status == 200){
        console.log(token.data.access_token);
        service_encoder.list_line(uri, token.data.access_token).then(function(temp_line){

          if(temp_line.status == 200){
            ServerModel.create({uri: uri}).then(function(resultCreateServer){
              if(resultCreateServer){
                res.status(200)
                    .json(
                      {
                        status: 200,
                        message: null,
                        data: resultCreateServer
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
              
            })
          }else{
            res.status(400)
                .json(
                  {
                    status: 400,
                    message: 'error trying connect to encoder server'
                  }
                )
          }
        })
      }

    });
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
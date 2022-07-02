const axios = require('axios');
const config = require('../config.json');


async function create_token(client_id){
  let payload = {
      "username": config.SERVER_USERNAME,
      "password": config.SERVER_PASSWORD,
      "client_id": client_id
  }
  const response = await axios.post(config.SERVER_AUTH, payload, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
  return response;
}
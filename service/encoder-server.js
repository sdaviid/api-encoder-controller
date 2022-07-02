const axios = require('axios');

async function list_line(uri, access_token){
  const response = await axios.get(uri, {
    headers: {
      'token': access_token
    }
  });
  return response
}


module.exports.list_line = list_line;
const axios = require('axios');

async function list_line(uri, access_token){
  const response = await axios.get(uri, {
    headers: {
      'token': access_token
    },
    proxy: {
      host: '192.168.1.102',
      port: 8888
    }
  });
  return response
}


module.exports.list_line = list_line;
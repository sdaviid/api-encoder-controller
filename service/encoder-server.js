const axios = require('axios');

async function list_line(uri, access_token){
  try{
    const response = await axios.get(`${uri}:55001/api/file/line`, {
      headers: {
        'token': access_token
      },
      timeout: 1000 * 5
    });
    return response
  }catch(err){
    console.log(err);
    return false;
  }
}


module.exports.list_line = list_line;
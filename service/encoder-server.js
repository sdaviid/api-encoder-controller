const axios = require('axios');

async function list_line(uri, access_token){
  try{
    return axios.get(`${uri}:55001/api/file/line`, {
      headers: {
        'token': access_token
      },
      timeout: 1000 * 5
    }).then((response)=>{
      console.log(response);
      return response.data;
    })
  }catch(err){
    console.log(err);
    return false;
  }
}




module.exports.list_line = list_line;
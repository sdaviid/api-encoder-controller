const Sequelize = require('sequelize');
const database = require('../utils/db');

const Server = database.define('server', {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    allowNull: false,
    primaryKey: true
  },
  uri: {
    type: Sequelize.STRING,
    allowNull: false,
  }
},{
  modelName: "Server"
});



module.exports = Server
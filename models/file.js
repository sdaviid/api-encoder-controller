const Sequelize = require('sequelize');
const database = require('../utils/db');

const File = database.define('file', {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    allowNull: false,
    primaryKey: true
  },
  serverId: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false
  }
},{
  modelName: "File"
});



module.exports = File
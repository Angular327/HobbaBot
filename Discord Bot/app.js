//Config
const Discord = require("discord.js");
const intents = new Discord.Intents(32767);
const client = new Discord.Client({ intents });
const config = require("./config.json");
var cron = require('node-cron');

//On Bot Run
client.on('ready', () => {
  //Says the bot logs in
  console.log(`Logged in as ${client.user.tag}!`);

});

//on message in chat this will be read
client.on('messageCreate', message => {
    //if the message is !checkin
    if(message.content == "!checkin") {

    }
});

//Login with the user token
client.login(config.token);
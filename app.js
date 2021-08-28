//Config
const Discord = require("discord.js");
const intents = new Discord.Intents(32767);
const client = new Discord.Client({ intents });
const config = require("./config.json");
var cron = require('node-cron');

cron.schedule('00 12 * * Saturday', () => {
  //get list of all users
  const list = client.guilds.cache.get(config.guildId); 

  //set users to not done role. They can become done by checking in
  list.members.cache.forEach(member => {
    if(!member.user.bot) {
      member.roles.add(config.notDone)
      member.roles.remove(config.done);
    }
  }); 
});

//On Bot Run
client.on('ready', () => {
  //Says the bot logs in
  console.log(`Logged in as ${client.user.tag}!`);

});

//on message in chat this will be read
client.on('messageCreate', message => {
    //if the message is !checkin
    if(message.content == "!checkin") {
      //If the user doesn't already have the done role
      if(!message.member.roles.cache.has(config.done)) {
        //Give the user the done role and remove the not done role
        message.member.roles.add(config.done);
        message.member.roles.remove(config.notDone);

        //Tell the user they have checked in
        message.reply("You have checked in");
      } else {
        //Tell the user they have already checked in
        message.reply("You have already checked in");
      }
    }
});

//Login with the user token
client.login(config.token);
//Config
const Discord = require("discord.js");
const intents = new Discord.Intents(32767);
const client = new Discord.Client({ intents });
const config = require("./config.json");

//Id for Roles to set
const done = "881001258322903131";
const notDone = "881001194586263555";

//On Bot Run
client.on('ready', () => {
  //Says the bot logs in
  console.log(`Logged in as ${client.user.tag}!`);

  //get list of all users
  const list = client.guilds.cache.get(config.guildId); 

  //set users to not done role. They can become done by checking in
  list.members.cache.forEach(member => {
    if(!member.user.bot) {
      member.roles.add(notDone)
      member.roles.remove(done);
    }
  }); 

  //Let's the console know setup compelete
  console.log("Setup Complete")
});

//on message in chat this will be read
client.on('messageCreate', message => {
    //if the message is !checkin
    if(message.content == "!checkin") {
      //If the user doesn't already have the done role
      if(!message.member.roles.cache.has(done)) {
        //Give the user the done role and remove the not done role
        message.member.roles.add(done);
        message.member.roles.remove(notDone);

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
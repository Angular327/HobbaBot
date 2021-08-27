const Discord = require('discord.js');
const client = new Discord.Client();
const Conversion = require('./Conversion');  

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.on('message', message => {
    if(!message.author.bot) {
      //Converts
      let conversion = Conversion.ConvertInput(message.content);
        if(conversion.length > 0)
            message.channel.send(conversion);

    }
});    

client.login('ODgwOTQ4NDk0ODY3NzkxOTIy.YSltOA.Y3091UADJnU1FAXyQUaoMjlw5xQ');
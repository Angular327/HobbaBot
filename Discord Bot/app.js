const { Client, Intents } = require('discord.js');
const { token } = require('./config.json');
const data = require('../Database/data');
const workoutData = data.workouts;  
const client = new Client({ intents: ["GUILDS", "GUILD_MESSAGES", "DIRECT_MESSAGES"] });

client.once('ready', () => {
	console.log('Ready!');
});

client.on('messageCreate', message => {
    //if the message is !checkin
    if(message.content == "!checkin") {
      workoutData.addWorkout(message.author.id, message.author.username, new Date().toLocaleString())
      message.reply("You have checked in");
    }
});

client.login(token);
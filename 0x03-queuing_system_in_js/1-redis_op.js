#!/usr/bin/node

import { createClient } from "redis";

const client = createClient();

// Setup event listeners for successful and unsuccessful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
  // redis.print is a built-in callback function in NodeJs
  // it logs responses or error messages to output in readable format
  client.set(schoolName, value, redis.print());
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, res) => {
    if (err) {
      console.log(`${err}`);
    } else {
      console.log(`${res}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
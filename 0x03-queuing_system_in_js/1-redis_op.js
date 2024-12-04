#!/usr/bin/node

import { createClient } from "redis";

const client = createClient();

// Method 1: Promise (using then & catch)
client.connect().then(() => {
    console.log('Redis client connected to the server');
}).catch((err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
  // redis.print is a built-in callback function in NodeJs
  // it logs responses or error messages to output in readable format
  client.set(schoolName, value, redis.print());
}

function displaySchoolValue(schoolName) {
  client.get(schoolName).then((res) => {
    console.log(`Value: ${res}`)
  }).catch((err) => {
    console.log(`Error: ${err}`)
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
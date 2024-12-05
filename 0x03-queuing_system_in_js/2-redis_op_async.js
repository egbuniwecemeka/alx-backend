#!/usr/bin/node

import { createClient } from "redis";
import { promisify } from 'util';


const client = createClient();
const asyncProm = promisify(client.get).bind(client);

// Connect to the redis server and display a log message on success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Display an error message on unsuccessful login
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Sets key, value pairs to the redis instance
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, client.print);
}

// Retrieves value of a key from redis instance
async function displaySchoolValue(schoolName) {
  try {
    const res = await asyncProm(schoolName);
    console.log(`Value: ${res}`);
  } catch (error) {
    console.log(`Error: ${error}`)
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
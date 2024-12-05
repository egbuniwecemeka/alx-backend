#!/usr/bin/node

import { createClient } from "redis";
import { promisify } from 'util';

// create redis client
const client = createClient();

// Promisify SET
const asynSet = promisify(client.set).bind(client);
// Promisify GET
const asyncGet = promisify(client.get).bind(client);

// Connect to the redis server and display a log message on success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Display an error message on unsuccessful login
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Sets key, value pairs to the redis instance
async function setNewSchool(schoolName, value) {
  try {
    const setResponse = await asynSet(schoolName, value);
    console.log('Reply:', setResponse);
  } catch (error) {
    console.log(`${error}`);
  }
}

// Retrieves value of a key from redis instance
async function displaySchoolValue(schoolName) {
  try {
    const res = await asyncGet(schoolName);
    console.log(`${res}`);
  } catch (error) {
    console.log(`${error}`)
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

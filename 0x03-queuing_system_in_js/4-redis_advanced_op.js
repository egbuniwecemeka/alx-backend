#!/usr/bin/node

// Import createClient 
import { createClient } from "redis";

// Create redis client
const client = createClient();

// Display error message on unsuccessful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
// Display error message on unsuccessful connection
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`)
});

const values = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

// Store values using hSet
for (const [field, value] in Object.entries(values)) {
  const hset = client.hSet('HolbertonSchools', field, value, client.print);
}

// Display stored value using hGetAll
client.hGetAll('HolbertonSchools', (err, res) => {
  if (err) {
    console.error(`${err}`);
  } else {
    console.log(`${res}`);
  }
});

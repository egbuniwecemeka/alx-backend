#!/usr/bin/node

// Import createClient 
import { createClient, print } from "redis";

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

// Store values using hset
for (const [field, value] of Object.entries(values)) {
  client.hset('HolbertonSchools', field, value, print);
}

// Display stored value using hGetAll
client.hgetall('HolbertonSchools', (err, res) => {
  if (err) {
    console.error(`${err}`);
  } else {
    console.log(JSON.stringify(res, null, 2));
  }
});

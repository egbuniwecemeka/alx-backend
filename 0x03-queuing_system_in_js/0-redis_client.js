#!/usr/bin/node
// Connect to redis server
import { createClient } from "redis";

const client = createClient();

// Log message on successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

// Log error message if connection is not successful
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

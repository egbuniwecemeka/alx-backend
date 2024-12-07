#!/usr/bin/node

import { createClient } from "redis";

const client = createClient();

// On connect event, log:
client.on('connect', (err, res) => {
    console.log('Redis client connected to the server');
  }
);

// On error event, log:
client.on('error', () => {
    console.log(`Redis client not connected to the server: ${err}`);
})

// Subscribe to channel
client.subscribe('holberton school channel', (err, message) => {
    if (err) {
        console.log(`Failed to subsribe to channel: ${err}`);
    } else {
        console.log(`Subscribed to ${message} channel(s)`);
    }
});

// Handle incoming messages, listen on message event
client.on('message', (channel, message) => {
    console.log(`Incoming message is: ${message} on channel: ${channel}`)
    if (message == 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
        console.log('Unsubscribed and shutting down client')
    }
});


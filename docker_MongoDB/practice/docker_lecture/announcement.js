// this file is used to illustrate how to use env variables.

const ANNOUNCER = process.env.ANNOUNCER ||'Docker';
const MESSAGE = process.env.MESSAGE||'There is no message';

// create and output the message
const announcement = `this is a message from ${ANNOUNCER}:${MESSAGE}`;
console.log(announcement)
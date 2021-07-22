const randomNumber = Math.floor(Math.random()*20)+1;

console.log(randomNumber)

const fs = require('fs');
fs.writeFileSync('random-number.txt', randomNumber)

/*
command on in terminal: mount the file
 docker run  -it -v "$PWD":/Users/lilycheng/Documents/data_scientist_projects/docker_MongoDB/practice node:8 node /Users/lilycheng/Documents/data_scientist_projects/docker_MongoDB/practice/randomnumber.js 
 docker ps -a
 docker rm <id or name of the container>
 
 */


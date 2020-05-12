#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) throw error;
  else {
    let c = 0;
    const results = JSON.parse(body).results;
    const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes(wedge)) {
        c++;
      }
    }
    console.log(c);
  }
});

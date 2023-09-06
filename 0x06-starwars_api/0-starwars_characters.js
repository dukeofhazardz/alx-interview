#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    }
  }
});

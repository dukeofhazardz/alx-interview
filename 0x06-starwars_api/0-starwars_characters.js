#!/usr/bin/nodejs

const request = require('request');

// Check if a movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieID = process.argv[2];

// URL for the Star Wars API to fetch movie details
const movieURL = `https://swapi.dev/api/films/${movieID}/`;

// Function to fetch characters for a movie
function fetchMovieCharacters (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error('Error:', response.statusCode);
      process.exit(1);
    }

    const movieData = JSON.parse(body);

    movieData.characters.forEach((characterURL) => {
      request(characterURL, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          process.exit(1);
        }

        if (charResponse.statusCode !== 200) {
          console.error('Error:', charResponse.statusCode);
          process.exit(1);
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
}

fetchMovieCharacters(movieURL);

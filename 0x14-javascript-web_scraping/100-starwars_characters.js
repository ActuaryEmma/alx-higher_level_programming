#!/usr/bin/node
// prints all charaters of a star wars movie

const process = require('process');
const path = require('path');
const request = require('request');

if (process.argv.length !== 3) {
  const script = path.basename(process.argv[1]);
  console.log(`Usage: node ${script} <id>`);
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people';

// fetch information from filmUrl
request(filmUrl, (filmErr, filmRes, filmBody) => {
  if (filmErr) {
    console.log(filmErr);
  } else {
    const filmData = JSON.parse(filmBody);
    // extracts characters array from the movie data
    const characterUrls = filmData.characters;
    // console.log(characterUrls);

    // fectch information from peopleUrl
    request(peopleUrl, (peopleErr, peopleRes, peopleBody) => {
      if (peopleErr) {
        console.log(peopleErr);
      } else {
        const peopleData = JSON.parse(peopleBody);
        // extract array of characters objects
        const characters = peopleData.results;
        // console.log(characters);

        // iterate thro characters array checking if characterUrls array contain the character's URL
        for (const character of characters) {
		  for (const charUrl of characterUrls) {
            if (character.url.endsWith(charUrl)) {
              console.log(character.name);
			  break;
            }
		  }
        }
      }
    });
  }
});

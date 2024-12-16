#!/usr/bin/node

const request = require('request');

// Retrieve the Movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as an argument.');
  process.exit(1);
}

// Define the URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the /films/ endpoint
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);

  // Ensure the API returned valid data
  if (!filmData.characters) {
    console.error('Invalid Movie ID or no characters found.');
    return;
  }

  // Fetch and print character names in the order provided
  const characterUrls = filmData.characters;

  // Helper function to fetch character names
  const fetchCharacter = (url, callback) => {
    request(url, (err, response, body) => {
      if (err) return callback(err);
      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  // Iterate over the character URLs and fetch names
  let completedRequests = 0;
  characterUrls.forEach((url, index) => {
    fetchCharacter(url, (err, name) => {
      if (err) {
        console.error(`Error fetching character at ${url}: ${err}`);
        return;
      }

      // Print the character name
      console.log(name);

      completedRequests++;
      if (completedRequests === characterUrls.length) {
        process.exit(0);
      }
    });
  });
});

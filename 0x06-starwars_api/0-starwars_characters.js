#!/usr/bin/node

// Load the 'request' module to handle HTTP requests
const request = require('request');

// Define a constant to store the base URL for the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the script was run with additional arguments (specifically, a film ID)
if (process.argv.length > 2) {
  // Send a request to the API to retrieve data for the specified film based on its ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // Log any request errors encountered
    if (err) {
      console.log(err);
    }
    // Parse the response body to extract the URLs for each character in the film
    const charactersURL = JSON.parse(body).characters;

    // Create an array of Promises, each resolving to a character's name
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Send a request to retrieve individual character data
        request(url, (promiseErr, __, charactersReqBody) => {
          // If there's an error during this request, reject the Promise
          if (promiseErr) {
            reject(promiseErr);
          }
          // Parse the character data and resolve the Promise with the character's name
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Once all character name Promises resolve, print each name on a new line
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

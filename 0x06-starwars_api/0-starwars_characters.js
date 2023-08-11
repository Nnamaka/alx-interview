#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api';
const MOVIE_ID = process.argv[2];
const API_ENDPOINT = URL + '/films/' + MOVIE_ID;

if (MOVIE_ID) {
  request(API_ENDPOINT, (err, clbk, res) => {
    if (!err) {
      const charLink = JSON.parse(res).characters;
      const charNames = charLink.map(
        (url) =>
          new Promise((resolve, reject) => {
            request(url, (promiseErr, __, charactersReqBody) => {
              if (promiseErr) {
                reject(promiseErr);
              }
              resolve(JSON.parse(charactersReqBody).name);
            });
          })
      );

      Promise.all(charNames)
        .then((names) => console.log(names.join('\n')));
    }
  });
}

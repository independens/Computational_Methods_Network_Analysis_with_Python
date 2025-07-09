import { Players } from 'Gatheringstats_players.js';
import { writeFileSync } from 'fs';

// Import the Players dictionary from another JS file (e.g., players.js)

// Convert the Players dictionary to JSON
const playersJSON = JSON.stringify(Players);

// Save the JSON string to a file (Node.js example)

writeFileSync('players.json', playersJSON);
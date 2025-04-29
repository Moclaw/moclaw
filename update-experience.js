const fs = require('fs');

// Set your professional start year here
const startYear = 2021;
const currentYear = new Date().getFullYear();
const years = currentYear - startYear;
const readmePath = './README.md';

let readme = fs.readFileSync(readmePath, 'utf8');
readme = readme.replace(/\*\*\{\{years_of_experience\}\}\*\*/g, `**${years} years of experience**`);
fs.writeFileSync(readmePath, readme);

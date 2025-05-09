const express = require('express');
const { exec } = require('child_process');
const app = express();
const path = require('path');

app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'guietc.html'));
});

app.get('/refresh', (req, res) => {
  exec('python scrape_lech_tickets.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Błąd: ${error.message}`);
      return res.status(500).send('Błąd podczas scrapowania');
    }
    if (stderr) console.error(`stderr: ${stderr}`);
    console.log(`stdout: ${stdout}`);
    res.send('OK');
  });
});

app.listen(3000, () => {
  console.log('Running at http://localhost:3000');
});

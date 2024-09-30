const express = require('express');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.get('/api/python-files', (req, res) => {
  const scriptsDir = path.join('./src/scripts');
  fs.readdir(scriptsDir, (err, files) => {
    if (err) {
      return res.status(500).json({ error: 'Unable to scan directory' });
    }
    const pythonFiles = files.filter(file => file.endsWith('.py'));
    res.json(pythonFiles);
  });
});


app.post('/api/run-python-file', (req, res) => {
    const file = req.query.file;
    const filePath = path.join('./src/scripts', file);
  
    exec(`/usr/bin/python3 ${filePath}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing file: ${error.message}`);
        return res.status(500).json({ error: error.message });
      }
      if (stderr) {
        console.error(`Error output: ${stderr}`);
        return res.status(500).json({ error: stderr });
      }
      console.log(`Output: ${stdout}`);
      res.json({ output: stdout });
    });
  });

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
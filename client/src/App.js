import React, { useState } from 'react';
import './App.css';

function App() {
  const [originalUrl, setOriginalUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(`${process.env.REACT_APP_API_URL}/api/shorten`);
    try {
      const res = await fetch(`${process.env.REACT_APP_API_URL}/api/shorten`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ original_url: originalUrl }),
      });
  
      const data = await res.json();
      if (res.ok) {
        setShortUrl(data.short_url);
      } else {
        alert(data.error)
        console.log(data.error);
      }
    } catch(err) {
      alert('Error contatching server');
      console.log(err);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        URL Shortener
      </header>

      <form onSubmit={handleSubmit}>
        <label htmlFor="longUrl">
            Please enter your long url here: 
        </label>
        <input
          type="text"
          name="longUrl"
          placeholder="e.g. www.google.com"
          value={originalUrl}
          onChange={(e) => setOriginalUrl(e.target.value)}
          required
        />
        <button type="submit">Generate short url</button>
      </form>
      
      {/* todo: a copy url button */}
      {shortUrl && (
        <p>
          Your shortened URL: <a href={shortUrl}>{shortUrl}</a>
        </p>
      )}
    </div>
  );
}

export default App;

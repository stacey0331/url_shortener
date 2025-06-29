import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        URL Shortener
      </header>

      <label htmlfor="longUrl">
          Please enter your long url here: 
      </label>
      <input
        type="url"
        name="longUrl"
        placeholder="e.g. www.google.com"
        required
      />

      <button type="submit">Generate short url</button>
    </div>
  );
}

export default App;

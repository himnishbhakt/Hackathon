:root {
  --bg-color: #121212;
  --card-color: #1e1e1e;
  --text-color: #ffffff;
  --accent-color: #00bcd4;
  --input-bg: #2c2c2c;
  --input-border: #444;
}

body {
  margin: 0;
  font-family: 'Segoe UI', sans-serif;
  background-color: var(--bg-color);
  color: var(--text-color);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  display: flex;
  gap: 2rem;
}

.card {
  background-color: var(--card-color);
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
  width: 300px;
}

h2 {
  margin-top: 0;
  color: var(--accent-color);
  text-align: center;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.75rem;
  margin: 0.5rem 0 1rem;
  background-color: var(--input-bg);
  border: 1px solid var(--input-border);
  border-radius: 6px;
  color: var(--text-color);
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--accent-color);
  border: none;
  border-radius: 6px;
  color: #000;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0097a7;
}

.footer {
  text-align: center;
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #aaa;
}

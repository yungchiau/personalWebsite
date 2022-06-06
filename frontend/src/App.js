import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import "./styles/style.css"

import logo from "./logo.svg";
import "./App.css";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
      });
  }, []);
// This is JSX 
  return (

    <div className="App">
      <header className="App-header">
        ... no changes in this part ...
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;

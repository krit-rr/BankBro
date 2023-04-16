import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(() => {
    axios.get('http://localhost:5000/home').then(response => {
      console.log("SUCCESS", response.data)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>Group 5 Finance</p>
        <div>{getMessage.status === 200 ? 
          <h3>{getMessage.data.about} - {getMessage.data.name}</h3>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;
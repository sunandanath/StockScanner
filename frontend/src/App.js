import React from "react";
import FileUpload from "./components/FileUpload";
import "./App.css";

const App = () => {
  return (
    <div className="App">
      <h1>Nifty Stock Analyzer</h1>
      <FileUpload />
    </div>
  );
};

export default App;

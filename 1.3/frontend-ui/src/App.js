import React from "react";
import "./App.css";
import Header from "./presentational_components/Header/Header";
import Hero from "./presentational_components/Hero/Hero";
import Upload from "./container_components/Upload/Upload";

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <Upload/>
    </div>
  );
}

export default App;

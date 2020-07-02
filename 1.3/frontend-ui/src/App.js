import React from "react";
import "./App.css";
import Header from "./presentational_components/Header";
import Hero from "./presentational_components/Hero";
import Upload from "./presentational_components/Upload";
import Result from "./presentational_components/Result";
import Footer from "./presentational_components/Footer";

function App() {
  return (
    <div className="App">
      <Header/>
      <Hero/>
      <Upload/>
      <Result/>
      <Footer/>
    </div>
  );
}

export default App;

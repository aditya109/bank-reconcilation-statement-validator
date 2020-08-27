import React from "react";
import "./App.css";
import Header from "./presentational_components/Header/Header";
import Hero from "./presentational_components/Hero/Hero";
import Upload from "./container_components/Upload/Upload";
import Footer from "./presentational_components/Footer/Footer";
function App() {
	return (
		<div className="App">
			<Header />
			<Hero />
			<Upload />
			<Footer />
		</div>
	);
}

export default App;

import React from "react";
import {
  BrowserRouter as Router, 
  Route,
} from 'react-router-dom';


import Home from "./pages/Home";

import NavigationBar from './components/NavigationBar';
import Test from './pages/Test';

import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <NavigationBar/>
        <Router>
          <Route exact path="/" component={Home}/>
          <Route exact path="/test" component={Test}/>
        </Router>
      </div>
    );
  }
}

export default App;

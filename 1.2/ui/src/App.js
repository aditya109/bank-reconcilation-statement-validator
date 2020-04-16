import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import './App.css';

import HomePage from './components/HomePage';
import TutorialPage from './components/TutorialPage';
import DFLoadingPage from './components/DFLoadingPage';
import ControlPage from './components/ControlPage';

import WarningPage from './components/WarningPage';

import SearchingPage from './components/SearchingPage';
import Graphs from './components/Graphs';

class App extends React.Component{
  componentDidMount() {
    document.title="Bank Reconcilation Statement Validator";
  }
  render() {
    return (
      <div className = "App">
        <Router >
          
          <Route exact path="/" component = {HomePage}/>   
          <Route exact path="/gr" component = {Graphs}/>   
          <Route exact path="/tutorial" component= {TutorialPage}/>   
          <Route exact path="/loader" component={DFLoadingPage}/>      
          <Route exact path="/control" component={ControlPage}/>  
          
          <Route exact path="/warning" component={WarningPage}/>
          
          <Route exact path="/search" component={SearchingPage}/>
        </Router>
      </div>
    )
  }






}

export default App;

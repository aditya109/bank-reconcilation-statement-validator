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
import ReportPage from './components/ReportPage';
import WarningPage from './components/WarningPage';
import PageOptions from './components/PageOptions';
import SearchingPage from './components/SearchingPage';

class App extends React.Component{
  componentDidMount() {
    document.title="Bank Reconcilation Statement Validator";
  }
  render() {
    return (
      <div className = "App">
        <Router >
          
          <Route exact path="/" component = {HomePage}/>              // ok
          <Route exact path="/tutorial" component= {TutorialPage}/>   // ok
          <Route exact path="/loader" component={DFLoadingPage}/>     // ok 
          <Route exact path="/control" component={ControlPage}/>  
          <Route exact path="/report" component={ReportPage}/>
          <Route exact path="/warning" component={WarningPage}/>
          <Route exact path="/pageoptions" component={PageOptions}/>
          <Route exact path="/search" component={SearchingPage}/>
        </Router>
      </div>
    )
  }






}

export default App;

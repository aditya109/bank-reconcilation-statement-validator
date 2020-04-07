import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import './App.css';

import HomePage from './components/HomePage';
import TutorialPage from './components/TutorialPage';
import DFLoadingPage from './components/DFLoadingPage';
import NavPage from './components/NavPage';
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
          <Route exact path="/" component = {HomePage}/>
          <Route exact path="/tutorial" component= {TutorialPage}/>
          <Route exact path="/loader" component={DFLoadingPage}/>
          <Route exact path="/nav" component={NavPage}/>
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

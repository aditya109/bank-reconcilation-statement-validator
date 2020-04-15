import React from 'react';
import {Redirect} from 'react-router-dom';

class HomePage extends React.Component {
    constructor(){
        super();
        this.state = {
            isChecked:false
        }
        this.handleChecked = this.handleChecked.bind(this);
    }

    handleChecked(e) {
        console.log("click !! ")
        
        this.setState({
            isChecked: !this.state.isChecked
        });

    }

    render() {

        var activateButton; 
        if (this.state.isChecked) {
            activateButton="checked";
        }
        else {
            activateButton="unchecked";
        }
        return (
            <div className="home-page-container">
                <div className="home-page-title-div">
                    <div className="home-page-title">
                        <span className="title-text">
                            BANK RECONCILIATION STATEMENT VALIDATOR
                        </span>
                    </div>
                </div>
                <div className="warning-text-div">
                    <span className="warning-text-low">This is to inform you as an end-user that </span>
                    <span className="warning-text-high">this application is in alpha-phase</span>
                    <span className="warning-text-low"> and is meant for </span>
                    <span className="warning-text-high">automating the laborious work done to detect erroneous transactions done manually</span>
                    <span className="warning-text-low">. So it is an earnest request to </span>
                    <span className="warning-text-high">bear with simple-minded UI or noticeable server-response latencies</span>
                    <span className="warning-text-low">, since the </span>
                    <span className="warning-text-high">focus majored on the use-cases and not on the UI</span>
                    <span className="warning-text-low">. This application is </span>
                    <span className="warning-text-high">not supposed to be hosted on net unless approved by the dev</span>
                    <span className="warning-text-low">. Please do not try to </span>
                    <span className="warning-text-high">tamper with the code or induce malicious code in any manner.</span>
                </div>
                <div className="checkbox-div">
                    <div className="checkbox-text">
                            <label class="checkbox-label">
                                <input type="checkbox" onChange={this.handleChecked}/>
                                <span class="checkbox-custom rectangular"></span>
                            </label>
                            <div class="input-title">If you agree, please check to continue.
                        </div>
                    </div>
                    
                </div>
                <div className="continue-button-div">
                    <div class="example_f" align="center" onClick= {(e) => {this.handleChecked(e)}}>
                        <span>Continue</span>
                    </div>
                </div>
            </div>
        )
    }
}
export default HomePage;
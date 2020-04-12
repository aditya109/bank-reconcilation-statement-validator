import React from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

class DFLoadingPage extends React.Component {
    constructor() {
        super();
        this.state = {
            tabIndex: 0
        };
    }

    render() {
        return (
            <div className="nav-page-container">
                <div className="nav-page-title-div">
                    <div className="nav-page-title-text">
                        <span className="title-text">
                            NavPage
                        </span>
                    </div>
                </div>
                <div className="tabs-panel-container">
                    <Tabs
                        selectedIndex={this.state.tabIndex}
                        onSelect={tabIndex => this.setState({ tabIndex })}
                        selectedTabClassName="sel-tab"
                        disabledTabClassName="dis-tab"
                    >
                        <TabList>
                            <Tab>Cheques Paid In But Not Credited (CPNC)</Tab>
                            <Tab>Credit (Cr)</Tab>
                            <Tab>Debit (Dr)</Tab>
                            <Tab>Cheque Dishonor Action (CDA)</Tab>
                        </TabList>
                        <TabPanel>
                            <div className="input-panel-container">
                                <div className="panel-title-container">
                                    <div className="panel-title">
                                        <span className="panel-title-text">Cheques Paid In But Not Credited (CPNC)</span>
                                    </div>
                                    <div className="panel-content">
                                        <div className="input-div">
                                            <div className="input-1">
                                                <span className="column-input-text">Enter the columnar data for Transaction Dates</span>
                                                <div className="input-text-area">
                                                    <textarea id="w3mission" rows="8" cols="130">
                                                        At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
                                                    </textarea>
                                                </div>
                                            </div>
                                            <div className="input-1">
                                                <span className="column-input-text">Enter the columnar data for Cheques Information</span>
                                                <div className="input-text-area">
                                                    <textarea id="w3mission" rows="8" cols="130">
                                                        At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
                                                    </textarea>
                                                </div>
                                            </div>
                                            <div className="input-1">
                                                <span className="column-input-text">Enter the columnar data for Transaction Amount</span>
                                                <div className="input-text-area">
                                                    <textarea id="w3mission" rows="8" cols="130">
                                                        At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
                                            </textarea>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="btn-div">
                                            <div className="load-btn" align="center">
                                                <span>Load Up Data &#8686;</span>
                                            </div>
                                            <div class="nav-btn" align="right" onClick={(e) => { this.handleChecked(e) }}>
                                                    <span>Navigate to Search Operations</span>
                                            </div>

                                        </div>


                                    </div>
                                </div>
                                {/* <div className="nav-btn-div">
                                                
                                            </div> */}
                            </div>
                        </TabPanel>
                        <TabPanel>

                        </TabPanel>
                        <TabPanel>

                        </TabPanel>
                        <TabPanel>

                        </TabPanel>
                    </Tabs>
                </div>
            </div>
        )
    }
}
export default DFLoadingPage;